import streamlit as st
from dotenv import load_dotenv

from langchain_groq import ChatGroq
from langchain_core.messages import HumanMessage

from utils import (
    search_arxiv,
    download_pdf,
    extract_text,
)

load_dotenv()

st.set_page_config(
    page_title="Research Paper Summarizer",
    page_icon="📚",
    layout="wide"
)

st.title("📚 AI Research Paper Summarizer")

st.write(
    """
Enter the title or keywords of any research paper.
The application searches arXiv, downloads the paper,
reads the PDF and generates a structured summary.
"""
)

query = st.text_input(
    "Paper Title / Keywords"
)

model = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0.3
)

if st.button("Generate Summary"):

    if query == "":
        st.warning("Please enter a paper title.")
        st.stop()

    with st.spinner("Searching Paper..."):

        paper = search_arxiv(query)

    if paper is None:
        st.error("No paper found.")
        st.stop()

    st.success("Paper Found!")

    st.subheader("Paper Information")

    st.write("### Title")
    st.write(paper["title"])

    st.write("### Authors")
    st.write(", ".join(paper["authors"]))

    st.write("### Published")
    st.write(paper["published"])

    st.write("### PDF")
    st.write(paper["pdf_url"])

    with st.spinner("Downloading PDF..."):

        pdf = download_pdf(paper["pdf_url"])

    with st.spinner("Reading Paper..."):

        paper_text = extract_text(pdf)

    # Avoid sending extremely large documents
    paper_text = paper_text[:80000]

    prompt = f"""
You are an expert AI Research Assistant.

Read the following research paper and generate a detailed report.

Research Paper:

{paper_text}

Return the answer in the following format.

# 📄 Executive Summary

Provide a concise overview.

---

# 🎯 Problem Statement

What problem does the paper solve?

---

# 💡 Motivation

Why was this work needed?

---

# ⚙ Proposed Method

Explain the proposed methodology step-by-step.

---

# 🧠 Model Architecture

Explain any architecture in detail.

---

# 📊 Dataset

Mention datasets used.

---

# 🔬 Experiments

Explain experimental setup.

---

# 📈 Results

Summarize results.

---

# ⭐ Key Contributions

Bullet list.

---

# ✅ Advantages

Bullet list.

---

# ❌ Limitations

Bullet list.

---

# 🚀 Future Work

Bullet list.

---

# 👨‍🎓 Explain Like I'm a Student

Explain in very simple language.

---

# 🔑 Important Keywords

Provide 15 keywords.

---

# 📌 One Paragraph Summary

Provide one paragraph.

"""

    with st.spinner("Generating AI Summary..."):

        response = model.invoke(
            [HumanMessage(content=prompt)]
        )

    st.markdown(response.content)