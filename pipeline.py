from agents import (
    build_reader_agent,
    build_search_agent,
    writer_chain,
    critic_chain
)

import time


def run_research_pipeline(topic: str) -> dict:

    state = {}

    # =========================================================
    # STEP 1 — SEARCH AGENT
    # =========================================================

    print("\n" + "=" * 60)
    print("STEP 1: Search Agent is working...")
    print("=" * 60)

    start_time = time.time()

    search_agent = build_search_agent()

    search_results = search_agent.invoke({
        "messages": [
            (
                "user",
                f"Find recent, reliable and detailed information about: {topic}"
            )
        ]
    })

    state["search_results"] = search_results["messages"][-1].content

    state["search_time"] = round(time.time() - start_time, 2)

    print("\nSEARCH RESULTS:\n")
    print(state["search_results"])

    # =========================================================
    # STEP 2 — READER AGENT
    # =========================================================

    print("\n" + "=" * 60)
    print("STEP 2: Reader Agent is scraping top resources...")
    print("=" * 60)

    start_time = time.time()

    reader_agent = build_reader_agent()

    reader_result = reader_agent.invoke({
        "messages": [
            (
                "user",
                f"""
Based on the following search results about '{topic}',
pick the most relevant URL and scrape it for deeper content.
There should not be any markdown and star symbols in output.

Search Results:

{state["search_results"][:800]}
"""
            )
        ]
    })

    state["scraped_content"] = reader_result["messages"][-1].content

    state["reader_time"] = round(time.time() - start_time, 2)

    print("\nSCRAPED CONTENT:\n")
    print(state["scraped_content"])

    # =========================================================
    # STEP 3 — WRITER
    # =========================================================

    print("\n" + "=" * 60)
    print("STEP 3: Writer is drafting the report...")
    print("=" * 60)

    start_time = time.time()

    research_combined = (
        f"SEARCH RESULTS:\n"
        f"{state['search_results']}\n\n"
        f"DETAILED SCRAPED CONTENT:\n"
        f"{state['scraped_content']}"
    )

    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined
    })

    state["writer_time"] = round(time.time() - start_time, 2)

    print("\nFINAL REPORT:\n")
    print(state["report"])

    # =========================================================
    # STEP 4 — CRITIC
    # =========================================================

    print("\n" + "=" * 60)
    print("STEP 4: Critic is reviewing the report...")
    print("=" * 60)

    start_time = time.time()

    state["feedback"] = critic_chain.invoke({
        "report": state["report"]
    })

    state["critic_time"] = round(time.time() - start_time, 2)

    print("\nCRITIC REPORT:\n")
    print(state["feedback"])

    # =========================================================
    # TOTAL TIME
    # =========================================================

    state["topic"] = topic

    state["total_time"] = round(
        state["search_time"]
        + state["reader_time"]
        + state["writer_time"]
        + state["critic_time"],
        2
    )

    return state


if __name__ == "__main__":

    topic = input("\nEnter a research topic: ")

    result = run_research_pipeline(topic)

    print("\nResearch completed successfully.")