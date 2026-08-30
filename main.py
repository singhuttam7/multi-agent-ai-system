"""
main.py
FastAPI server that exposes the multi-agent research pipeline
(agents.py + tools.py) to the web UI, streaming live progress
for every stage (Search -> Read/Scrape -> Write -> Critique)
over Server-Sent Events (SSE).

Run with:
    uvicorn main:app --reload --port 8000

Then open http://localhost:8000 in your browser.
"""

import json
import traceback
from datetime import datetime

from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import StreamingResponse
from fastapi.staticfiles import StaticFiles

from agents import build_search_agent, build_reader_agent, writer_chain, critic_chain

app = FastAPI(title="Multi-Agent Research Pipeline API")

# Allow the front-end (served from the same app or a dev server) to call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def sse_event(payload: dict) -> str:
    """Format a dict as a Server-Sent Event chunk."""
    return f"data: {json.dumps(payload, ensure_ascii=False)}\n\n"


def now() -> str:
    return datetime.utcnow().strftime("%H:%M:%S")


def run_pipeline_stream(topic: str):
    """
    Generator that runs the four pipeline stages and yields an SSE
    event before and after each stage so the UI can render live
    progress. Mirrors the logic in pipeline.py, but split into
    streamable steps and using the correct agent for each step.
    """
    state = {}

    try:
        # -------------------------------------------------
        # Step 1: Search agent
        # -------------------------------------------------
        yield sse_event({
            "step": 1,
            "name": "search",
            "status": "running",
            "message": f"Search agent is looking up '{topic}'...",
            "time": now(),
        })

        search_agent = build_search_agent()
        search_results = search_agent.invoke({
            "messages": [(
                "user",
                f"Find recent, reliable and detailed information about: {topic}"
            )]
        })
        state["search_results"] = search_results["messages"][-1].content

        yield sse_event({
            "step": 1,
            "name": "search",
            "status": "done",
            "message": "Search agent finished gathering sources.",
            "data": state["search_results"],
            "time": now(),
        })

        # -------------------------------------------------
        # Step 2: Reader agent (scrapes the best source)
        # -------------------------------------------------
        yield sse_event({
            "step": 2,
            "name": "reader",
            "status": "running",
            "message": "Reader agent is scraping the top resource...",
            "time": now(),
        })

        reader_agent = build_reader_agent()
        reader_result = reader_agent.invoke({
            "messages": [(
                "user",
                f"Based on the following search results about '{topic}', "
                f"pick the most relevant URL and scrape it for deeper content.\n\n"
                f"Search Results:\n{state['search_results'][:800]}"
            )]
        })
        state["scraped_content"] = reader_result["messages"][-1].content

        yield sse_event({
            "step": 2,
            "name": "reader",
            "status": "done",
            "message": "Reader agent finished scraping the source.",
            "data": state["scraped_content"],
            "time": now(),
        })

        # -------------------------------------------------
        # Step 3: Writer chain
        # -------------------------------------------------
        yield sse_event({
            "step": 3,
            "name": "writer",
            "status": "running",
            "message": "Writer is drafting the research report...",
            "time": now(),
        })

        research_combined = (
            f"SEARCH RESULTS:\n{state['search_results']}\n\n"
            f"DETAILED SCRAPED CONTENT:\n{state['scraped_content']}"
        )

        state["report"] = writer_chain.invoke({
            "topic": topic,
            "research": research_combined,
        })

        yield sse_event({
            "step": 3,
            "name": "writer",
            "status": "done",
            "message": "Writer finished the draft report.",
            "data": state["report"],
            "time": now(),
        })

        # -------------------------------------------------
        # Step 4: Critic chain
        # -------------------------------------------------
        yield sse_event({
            "step": 4,
            "name": "critic",
            "status": "running",
            "message": "Critic is reviewing the report...",
            "time": now(),
        })

        state["feedback"] = critic_chain.invoke({
            "report": state["report"],
        })

        yield sse_event({
            "step": 4,
            "name": "critic",
            "status": "done",
            "message": "Critic finished the review.",
            "data": state["feedback"],
            "time": now(),
        })

        # -------------------------------------------------
        # Final payload
        # -------------------------------------------------
        yield sse_event({
            "step": "complete",
            "status": "done",
            "topic": topic,
            "report": state["report"],
            "feedback": state["feedback"],
            "time": now(),
        })

    except Exception as exc:
        yield sse_event({
            "step": "error",
            "status": "error",
            "message": str(exc),
            "trace": traceback.format_exc(),
            "time": now(),
        })


@app.get("/api/research")
def research(topic: str = Query(..., min_length=2, description="Research topic")):
    """
    Streams pipeline progress as Server-Sent Events.
    Consume from the browser with:
        new EventSource(`/api/research?topic=...`)
    """
    return StreamingResponse(
        run_pipeline_stream(topic),
        media_type="text/event-stream",
        headers={
            "Cache-Control": "no-cache",
            "Connection": "keep-alive",
            "X-Accel-Buffering": "no",
        },
    )


@app.get("/api/health")
def health():
    return {"status": "ok", "time": now()}


# Serve the front-end (static/index.html, style.css, script.js)
app.mount("/", StaticFiles(directory="static", html=True), name="static")
