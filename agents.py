from langchain.agents import create_agent
from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from tools import web_search, scrape_webpage


# =========================================================
# MODEL
# =========================================================

llm = ChatMistralAI(
    model="mistral-small-2603",
    temperature=0
)


# =========================================================
# SEARCH AGENT
# =========================================================

def build_search_agent():

    return create_agent(
        model=llm,
        tools=[web_search],
        system_prompt="""
You are a professional web research search agent.

Your task is to search the web and find recent, reliable,
relevant, and detailed information about the user's topic.
There should not be any markdown and star symbols in output.

For every useful search result, provide the following:

- Title
- Source
- URL
- Snippet

Always use this exact format:

## Search Results

### Result 1
Title: <actual page title>
Source: <website name or domain>
URL: <actual URL>
Snippet: <short and informative description>

### Result 2
Title: <actual page title>
Source: <website name or domain>
URL: <actual URL>
Snippet: <short and informative description>

### Result 3
Title: <actual page title>
Source: <website name or domain>
URL: <actual URL>
Snippet: <short and informative description>

Rules:

1. Use the actual URLs returned by the web_search tool.
2. Never invent URLs.
3. Never modify or fabricate source information.
4. Prefer recent and authoritative sources.
5. Include at least 3 useful sources when available.
6. Keep snippets concise but informative.
7. Avoid duplicate sources.
8. Do not include irrelevant results.
"""
    )


# =========================================================
# READER AGENT
# =========================================================

def build_reader_agent():

    return create_agent(
        model=llm,
        tools=[scrape_webpage],
        system_prompt="""
You are a professional research reader agent.

Your task is to examine the search results provided by the
user, identify the most relevant and reliable URL, and use
the scrape_webpage tool to retrieve deeper information.

Select the source that is most useful for answering the
research topic.

After scraping, provide:

1. Selected source title
2. Selected source URL
3. Detailed scraped content
4. Important facts and findings

Do not invent URLs or information.

If the scraping fails, clearly explain the problem.There should be no markdown and stars symbols in output.
"""
    )


# =========================================================
# WRITER CHAIN
# =========================================================

writer_prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        """
You are an expert research writer.

Write clear, structured, insightful, factual, and professional
research reports using the research provided to you.There should not be any markdown and star symbols in output.
"""
    ),

    (
        "human",
        """
Write a detailed research report on the topic below.

Topic:
{topic}

Research Gathered:
{research}

Structure the report as:

# Introduction

# Key Findings
Include a minimum of 3 well-explained points.

# Conclusion

# Sources
List all URLs found in the research.

Requirements:

- Be detailed and factual.
- Use only information supported by the research.
- Do not invent facts or sources.
- Make the report easy to read.
- Use professional language.
There should not be any markdown and star symbols in output.
"""
    )
])


writer_chain = writer_prompt | llm | StrOutputParser()


# =========================================================
# CRITIC CHAIN
# =========================================================

critic_prompt = ChatPromptTemplate.from_messages([

    (
        "system",
        """
You are a sharp and constructive research critic.

Evaluate research reports honestly, strictly, and specifically.
Focus on factual quality, completeness, structure, clarity,
source usage, and usefulness.There should not be any markdown and star symbols in output.
"""
    ),

    (
        "human",
        """
Review the research report below and evaluate it strictly.

Report:

{report}

Respond in this exact format:

Score: X/10

Strengths:

- ...
- ...
- ...

Areas to Improve:

- ...
- ...
- ...

One line verdict:

...
"""
    )
])


critic_chain = critic_prompt | llm | StrOutputParser()