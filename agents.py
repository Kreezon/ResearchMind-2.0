```python
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import os
from dotenv import load_dotenv

# ── Load environment variables ──
load_dotenv()

# ── Safety checks ──
if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY not found.")

# ── Groq Model Setup ──
llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.1-8b-instant",
    temperature=0,
)

# ─────────────────────────────────────────────────────────────
# SEARCH CHAIN
# ─────────────────────────────────────────────────────────────
search_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a professional AI research assistant."
    ),
    (
        "human",
        """
Find recent, reliable and detailed information about:

Topic: {topic}

Provide:
- Latest developments
- Key trends
- Important companies/research
- Technical insights
- Real-world applications

Be detailed and factual.
"""
    ),
])

search_chain = search_prompt | llm | StrOutputParser()

# ─────────────────────────────────────────────────────────────
# READER CHAIN
# ─────────────────────────────────────────────────────────────
reader_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert research analyst."
    ),
    (
        "human",
        """
Analyze the following research information deeply.

Topic:
{topic}

Research:
{research}

Extract:
- Most important insights
- Technical details
- Challenges
- Future outlook
- Industry impact

Be comprehensive and structured.
"""
    ),
])

reader_chain = reader_prompt | llm | StrOutputParser()

# ─────────────────────────────────────────────────────────────
# WRITER CHAIN
# ─────────────────────────────────────────────────────────────
writer_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are an expert research writer."
    ),
    (
        "human",
        """
Write a detailed professional research report.

Topic:
{topic}

Research:
{research}

Structure:
- Introduction
- Key Findings
- Technical Analysis
- Industry Impact
- Future Scope
- Conclusion

Make it detailed and polished.
"""
    ),
])

writer_chain = writer_prompt | llm | StrOutputParser()

# ─────────────────────────────────────────────────────────────
# CRITIC CHAIN
# ─────────────────────────────────────────────────────────────
critic_prompt = ChatPromptTemplate.from_messages([
    (
        "system",
        "You are a strict research critic."
    ),
    (
        "human",
        """
Review this report critically.

Report:
{report}

Provide:
- Overall score out of 10
- Strengths
- Weaknesses
- Improvements
- Final verdict
"""
    ),
])

critic_chain = critic_prompt | llm | StrOutputParser()
```
