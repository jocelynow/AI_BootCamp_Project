import streamlit as st
from PIL import Image


# -----------------------------
# Streamlit App: Methodology Display
# -----------------------------
st.set_page_config(
    page_title="TravelPal Methodology",
    layout="wide"
)

st.title("🛫 TravelPal Methodology")
st.markdown("""
This page describes the architecture, data flow, and implementation details of the TravelPal system. 
The application integrates Retrieval-Augmented Generation (RAG), official MFA country-advisory retrieval, 
and weather-information tools into a unified agent powered by a large language model (LLM).
""")

# -----------------------------
# Tabs for main sections
# -----------------------------
tabs = st.tabs([
    "📌 Overview", 
    "📊 Data Processing", 
    "🤖 LLM & Agent", 
    "🏗️ Data Flow Architecture", 
    "🛡️ Agent Flow & Guarantees"
])

with tabs[0]:
    st.header("1️⃣ System Overview")
    st.markdown("""
    The TravelPal system integrates several AI technologies and data-processing components to deliver reliable, source-grounded travel guidance. It uses:
    - **Streamlit** for UI and resource caching  
    - **LangChain** for retrieval, vector search, and tool-based agent reasoning  
    - **OpenAI Chat Models** for controlled natural-language generation  
    - **FAISS** for vector similarity search  
    - **SpaCy** for country extraction using named-entity recognition  
    - **Requests + BeautifulSoup** for fetching MFA advisory pages in real time

    All tools are orchestrated by a **zero-shot reasoning agent** that selects the right tool and returns a concise, factual response with clickable references.
    - **TravelPal Tool** – Retrieves Singapore travel policies from the TravelPal RAG document.
    - **MFA Tool** – Provides country-specific travel advisories from MFA webpages.
    - **Weather Tool** – Provides average monthly temperatures for cities worldwide.
    """)

with tabs[1]:
    st.header("2️⃣ Data Processing and Retrieval")

    st.subheader("📝 TravelPal RAG Tool")
    st.markdown("""
    **Document Processing**
    - Loads a curated `.docx` knowledge base containing MFA/ICA travel policy text.
    - Parses the document paragraph by paragraph; empty or whitespace-only paragraphs are skipped.
    - Stores each paragraph as the **text content** of a `Document`.
    - Extracts **official URLs** from the paragraph using regex and stores them as **metadata**.

    **Text Preparation**
    - Applies `RecursiveCharacterTextSplitter` (chunk_size=1000, overlap=100) to preserve semantic continuity.
    - Produces chunked `Document` objects for embedding and retrieval.

    **Vector Store Construction**
    - Generates embeddings using `OpenAIEmbeddings`.
    - Stores vectors in a **FAISS similarity index** for efficient top-K retrieval.
    - Exposed through `as_retriever(k=3)` to fetch the 3 most relevant chunks.

    **Query Processing**
    - A `RetrievalQA` pipeline feeds retrieved chunks + the user query into the LLM.
    - A strict prompt forces the LLM to answer **only** using the paragraph content.
    - The tool collects URLs from retrieved documents and appends them as **clickable Markdown links** in the final answer.

    **Key Distinction**
    - **Text content** → used by the LLM to generate answers.  
    - **URLs metadata** → not used for reasoning, only appended as reference links.
    """)

    st.subheader("🌏 MFA Country Advisory Tool")
    st.markdown("""
    **Country Extraction**
    - Uses `spaCy` Named Entity Recognition to detect `Geo-Political Entity` entities (countries/cities) from the user query.
    - Validates the detected country against an internal `MFA_COUNTRY_MAP`.

    **Advisory Retrieval**
    - Maps the country to the official MFA travel-advisory page URL.
    - Fetches the page HTML using `requests` and extracts the `<title>` with `BeautifulSoup`.
    - Falls back to a generic title if the page cannot be retrieved.

    **Response Construction**
    - Returns a structured advisory message combining the page title and the official URL.
    - **LLM is not used**; the response is built directly from retrieved content.
    - Ensures the output includes a **clickable official MFA URL**.

    **Key Distinction**
    - **HTML content/title** → used to generate the advisory message.  
    - **URL** → provided as a reference link.
    """)

    st.subheader("☀️ Weather Tool")
    st.markdown("""
    **Query Parsing**
    - Extracts the city name using regex (`in <City>` pattern) or heuristic parsing.

    **Data Retrieval**
    - Calls the Open-Meteo Geocoding API to convert city names into latitude/longitude coordinates.
    - Uses coordinates to query the Open-Meteo Climate API for **average monthly temperature**.

    **Response Construction**
    - Formats data into a clear, user-friendly sentence:  
    _"The average temperature in Paris in June is around 22°C."_.
    - Designed for monthly climate patterns, **not real-time forecasts**.

    **Key Distinction**
    - **API data** → used directly to generate the temperature report.
    - No LLM reasoning involved; ensures factual numeric output.
    """)

with tabs[2]:
    st.header("3️⃣ LLM & Tool Orchestration")
    st.markdown("""
    - **LLM:** `ChatOpenAI` (gpt-4o-mini, temperature 0.4) generates responses when summarization or reasoning is required.
    - **Prompt:** Ensures answers rely **only on retrieved content**, preventing hallucinations.
    - **Agent:** Uses `zero-shot-react-description` to orchestrate multiple tools.
    - **Tool Selection:** Automatically chooses the correct tool (TravelPal, MFA, Weather) based on the query type.
    - **Error Handling & Formatting:** Manages parsing errors and formats outputs with **clickable reference URLs** for clarity and reliability.
    """)

with tabs[3]:
    st.header("4️⃣ Data Flow Architecture")
    st.markdown("""
    ##### **Step 1 — User Query**
    A user submits a free-form query (e.g., *“Can I bring wine into Singapore?”*).

    ##### **Step 2 — Agent Routing**
    The Zero-Shot ReAct agent evaluates the query and selects the correct tool:

    - **RAG Tool** → Singapore travel policies  
    - **MFA Tool** → Country-specific advisory  
    - **Weather Tool** → Monthly climate averages  

    ##### **Step 3 — Tool Execution**
    The selected tool retrieves structured information:

    - RAG: Vector search + retrieved policy chunks  
    - MFA: Fetches official MFA travel page  
    - Weather: Calls Open-Meteo climate API  

    ##### **Step 4 — Final Answer**
    The LLM synthesizes the tool output into a grounded, concise response, including **clickable official URLs**.
    """)

with tabs[4]:
    st.header("5️⃣ Agent Flow & Technical Guarantees")
    st.markdown("""
    ##### **Agent Execution Flow**
    1. **User Query** – A free-form travel-related question is submitted.
    2. **Agent Routing** – The zero-shot ReAct agent evaluates the query and selects the appropriate tool:
        - **TravelPal RAG Tool** → Singapore travel policies  
        - **MFA Tool** → Country-specific travel advisories  
        - **Weather Tool** → Monthly climate averages  
    3. **Tool Execution** – The selected tool retrieves structured information:
        - RAG: Vector search + relevant policy chunks  
        - MFA: Fetches official MFA travel page  
        - Weather: Queries Open-Meteo Climate API  
    4. **LLM Synthesis** – For the TravelPal RAG Tool, the LLM summarizes retrieved policy chunks into a concise response, including clickable official URLs.

    ##### **Technical Guarantees**
    1. **Factuality:** LLM only uses retrieved content; hallucination is mitigated.  
    2. **Source Attribution:** All answers include official, clickable URLs.  
    3. **Deterministic Outputs:** MFA and Weather tools bypass the LLM for precise, factual data.  
    4. **Error Handling:** Parsing failures are managed gracefully with fallback messages.  
    5. **User-Friendly Formatting:** Responses are concise, structured, and readable.
    """)


# ---------- FOOTER ----------
st.markdown(
    """
    <hr>
    <p style="font-size:14px; color:#555;">
        © 2025 TravelPal | AI Champions BootCamp (Aug - Nov 2025)  | Developed by Jocelyn Ow 
    </p>
    """,
    unsafe_allow_html=True
)
