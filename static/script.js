(function () {
  "use strict";

  const form = document.getElementById("researchForm");
  const topicInput = document.getElementById("topicInput");
  const runBtn = document.getElementById("runBtn");
  const formHint = document.getElementById("formHint");

  const feedBody = document.getElementById("feedBody");
  const feedPlaceholder = document.getElementById("feedPlaceholder");
  const railList = document.getElementById("railList");
  const railProgressFill = document.getElementById("railProgressFill");

  const reportSection = document.getElementById("reportSection");
  const reportProse = document.getElementById("reportProse");
  const reportTopicTitle = document.getElementById("reportTopicTitle");

  const criticSection = document.getElementById("criticSection");
  const criticText = document.getElementById("criticText");
  const ringFill = document.getElementById("ringFill");
  const scoreValue = document.getElementById("scoreValue");

  const errorSection = document.getElementById("errorSection");
  const errorText = document.getElementById("errorText");

  const apiDot = document.getElementById("apiDot");
  const apiStatusText = document.getElementById("apiStatusText");

  const RING_CIRCUMFERENCE = 327; // 2 * PI * 52, matches the SVG radius

  let currentSource = null;

  // ---------------------------------------------------------
  // Health check
  // ---------------------------------------------------------
  fetch("/api/health")
    .then((r) => (r.ok ? r.json() : Promise.reject()))
    .then(() => {
      apiDot.dataset.ok = "true";
      apiStatusText.textContent = "Engine online";
    })
    .catch(() => {
      apiDot.dataset.ok = "false";
      apiStatusText.textContent = "Engine unreachable";
    });

  // ---------------------------------------------------------
  // Helpers
  // ---------------------------------------------------------
  function escapeHtml(str) {
    return String(str)
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;");
  }

  function appendFeedLine(html) {
    if (feedPlaceholder) feedPlaceholder.remove();
    const line = document.createElement("p");
    line.className = "feed-line";
    line.innerHTML = html;
    feedBody.appendChild(line);
    feedBody.scrollTop = feedBody.scrollHeight;
  }

  function appendSnippet(text, limit = 260) {
    const trimmed = text.trim().slice(0, limit);
    const line = document.createElement("p");
    line.className = "feed-line snippet";
    line.textContent = trimmed + (text.length > limit ? "…" : "");
    feedBody.appendChild(line);
    feedBody.scrollTop = feedBody.scrollHeight;
  }

  function setRailState(step, state) {
    const li = railList.querySelector(`.rail-step[data-step="${step}"]`);
    if (!li) return;
    li.querySelector(".rail-state").dataset.state = state;
    li.dataset.active = state === "running" ? "true" : "false";
    li.dataset.done = state === "done" ? "true" : "false";
  }

  function updateProgress(stepsCompleted) {
    const pct = Math.min(100, (stepsCompleted / 4) * 100);
    railProgressFill.style.width = pct + "%";
  }

  function resetUI() {
    feedBody.innerHTML = "";
    const p = document.createElement("p");
    p.className = "feed-placeholder";
    p.id = "feedPlaceholder";
    feedBody.appendChild(p);

    railList.querySelectorAll(".rail-step").forEach((li) => {
      li.querySelector(".rail-state").dataset.state = "idle";
      li.dataset.active = "false";
      li.dataset.done = "false";
    });
    railProgressFill.style.width = "0%";

    reportSection.hidden = true;
    criticSection.hidden = true;
    errorSection.hidden = true;
    reportProse.innerHTML =
      '<p class="report-placeholder">The finished report will appear here once the writer agent completes its draft.</p>';
    criticText.innerHTML =
      '<p class="report-placeholder">The critic\'s evaluation, strengths and suggested improvements will appear here.</p>';
    ringFill.style.strokeDashoffset = RING_CIRCUMFERENCE;
    scoreValue.textContent = "–";
  }

  // Very small, safe markdown-ish renderer for the writer/critic output.
  function renderMarkdown(raw) {
    const lines = raw.replace(/\r\n/g, "\n").split("\n");
    let html = "";
    let inList = false;

    const closeList = () => {
      if (inList) {
        html += "</ul>";
        inList = false;
      }
    };

    for (let line of lines) {
      const trimmed = line.trim();

      if (!trimmed) {
        closeList();
        continue;
      }
      if (/^#{1,2}\s+/.test(trimmed)) {
        closeList();
        html += `<h1>${escapeHtml(trimmed.replace(/^#{1,2}\s+/, ""))}</h1>`;
      } else if (/^#{3,6}\s+/.test(trimmed)) {
        closeList();
        html += `<h2>${escapeHtml(trimmed.replace(/^#{3,6}\s+/, ""))}</h2>`;
      } else if (/^[-*]\s+/.test(trimmed)) {
        if (!inList) {
          html += "<ul>";
          inList = true;
        }
        html += `<li>${escapeHtml(trimmed.replace(/^[-*]\s+/, ""))}</li>`;
      } else {
        closeList();
        html += `<p>${escapeHtml(trimmed)}</p>`;
      }
    }
    closeList();
    return html;
  }

  function renderCritic(raw) {
    const scoreMatch = raw.match(/Score:\s*(\d+(?:\.\d+)?)\s*\/\s*10/i);
    const score = scoreMatch ? parseFloat(scoreMatch[1]) : null;

    if (score !== null) {
      const clamped = Math.max(0, Math.min(10, score));
      const offset = RING_CIRCUMFERENCE - (clamped / 10) * RING_CIRCUMFERENCE;
      requestAnimationFrame(() => {
        ringFill.style.strokeDashoffset = offset;
      });
      scoreValue.textContent = clamped;
    } else {
      scoreValue.textContent = "–";
    }

    // Turn "Strengths:" / "Areas to Improve:" / "One line verdict:" into small headings.
    const withHeadings = raw
      .replace(/Score:\s*\d+(?:\.\d+)?\s*\/\s*10/i, "")
      .replace(/(Strengths:)/i, "\n#### $1\n")
      .replace(/(Areas to Improve:)/i, "\n#### $1\n")
      .replace(/(One line verdict:)/i, "\n#### $1\n");

    const lines = withHeadings.replace(/\r\n/g, "\n").split("\n");
    let html = "";
    let inList = false;
    const closeList = () => {
      if (inList) {
        html += "</ul>";
        inList = false;
      }
    };
    for (let line of lines) {
      const trimmed = line.trim();
      if (!trimmed) {
        closeList();
        continue;
      }
      if (/^####\s+/.test(trimmed)) {
        closeList();
        html += `<h4>${escapeHtml(trimmed.replace(/^####\s+/, ""))}</h4>`;
      } else if (/^[-*]\s+/.test(trimmed)) {
        if (!inList) {
          html += "<ul>";
          inList = true;
        }
        html += `<li>${escapeHtml(trimmed.replace(/^[-*]\s+/, ""))}</li>`;
      } else {
        closeList();
        html += `<p>${escapeHtml(trimmed)}</p>`;
      }
    }
    closeList();
    criticText.innerHTML = html || `<p>${escapeHtml(raw)}</p>`;
  }

  const STEP_LABELS = {
    1: { tag: "tag-search", name: "SEARCH" },
    2: { tag: "tag-reader", name: "READER" },
    3: { tag: "tag-writer", name: "WRITER" },
    4: { tag: "tag-critic", name: "CRITIC" },
  };

  // ---------------------------------------------------------
  // Form submit -> open SSE stream
  // ---------------------------------------------------------
  form.addEventListener("submit", function (e) {
    e.preventDefault();
    const topic = topicInput.value.trim();
    if (!topic) return;

    if (currentSource) {
      currentSource.close();
      currentSource = null;
    }

    resetUI();
    runBtn.disabled = true;
    runBtn.querySelector(".run-btn-label").textContent = "Running…";
    formHint.innerHTML = `Researching <strong>${escapeHtml(topic)}</strong> — this can take a minute.`;

    document
      .getElementById("consoleSection")
      .scrollIntoView({ behavior: "smooth", block: "start" });

    const url = `/api/research?topic=${encodeURIComponent(topic)}`;
    const source = new EventSource(url);
    currentSource = source;

    source.onmessage = function (event) {
      let payload;
      try {
        payload = JSON.parse(event.data);
      } catch (err) {
        return;
      }

      if (payload.step === "error") {
        appendFeedLine(
          `<span class="tag tag-error">ERROR</span>${escapeHtml(payload.message || "Unknown error")}`,
        );
        errorText.textContent =
          payload.message ||
          "Something went wrong while contacting the agents.";
        errorSection.hidden = false;
        finishRun(false);
        return;
      }

      if (payload.step === "complete") {
        reportTopicTitle.textContent = `Research report: ${payload.topic}`;
        reportProse.innerHTML = renderMarkdown(payload.report || "");
        reportSection.hidden = false;

        renderCritic(payload.feedback || "");
        criticSection.hidden = false;

        appendFeedLine(
          `<span class="tag tag-system">DONE</span>Pipeline finished for "${escapeHtml(payload.topic)}".`,
        );
        finishRun(true);
        return;
      }

      const label = STEP_LABELS[payload.step];
      if (!label) return;

      if (payload.status === "running") {
        setRailState(payload.step, "running");
        appendFeedLine(
          `<span class="tag ${label.tag}">${label.name}</span>${escapeHtml(payload.message)}`,
        );
      } else if (payload.status === "done") {
        setRailState(payload.step, "done");
        updateProgress(payload.step);
        appendFeedLine(
          `<span class="tag ${label.tag}">${label.name}</span>${escapeHtml(payload.message)}`,
        );
        if (payload.data) appendSnippet(payload.data);
      }
    };

    source.onerror = function () {
      if (source.readyState === EventSource.CLOSED) return;
      errorText.textContent =
        "Lost connection to the research engine. Check that the FastAPI server is running.";
      errorSection.hidden = false;
      appendFeedLine(
        `<span class="tag tag-error">ERROR</span>Connection to the engine was interrupted.`,
      );
      finishRun(false);
    };
  });

  function finishRun(success) {
    runBtn.disabled = false;
    runBtn.querySelector(".run-btn-label").textContent = "Run pipeline";
    formHint.textContent = success
      ? "Done. Enter another topic to run the pipeline again."
      : "The run stopped early. Fix the issue above and try again.";
    if (currentSource) {
      currentSource.close();
      currentSource = null;
    }
  }
})();
