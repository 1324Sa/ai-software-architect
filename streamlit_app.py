import os
import sys

# Ensure the root directory is included in Python's path to resolve local imports
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
from app.rag.engine import ArchitectRAGEngine

# Page Configuration (Must be the first Streamlit command)
st.set_page_config(
    page_title="AI Software Architect",
    page_icon="🏗️",
    layout="wide",
)


# Initialize RAG Engine in Session State (loads once for fast performance)
@st.cache_resource
def load_rag_engine():
    engine = ArchitectRAGEngine()

    # Initial Knowledge Base Documents
    default_knowledge = [
        (
            "For food delivery applications requiring real-time driver"
            " tracking, the recommended architecture utilizes WebSockets for"
            " live bi-directional communication, Redis Pub/Sub for managing"
            " high-throughput location message streams between drivers and"
            " clients, and a PostgreSQL database with PostGIS extension for"
            " storing and processing geospatial coordinates."
        ),
        (
            "Live video streaming and educational platforms require dedicated"
            " media servers such as WebRTC and FFmpeg paired with cloud"
            " object storage like AWS S3."
        ),
        (
            "Chat applications and social network systems rely on graph"
            " databases like Neo4j for managing relationships and NoSQL"
            " databases like MongoDB for message storage."
        ),
    ]

    engine.seed_initial_knowledge(default_knowledge)
    return engine


# Header Section
st.title("🏗️ AI Software Architect")
st.caption(
    "Generate technical software architecture reports grounded in your vector"
    " knowledge base."
)

st.divider()

# Load Engine
with st.spinner("Initializing Vector DB & Llama 3 Model..."):
    rag_engine = load_rag_engine()

# Sidebar - System Info & Knowledge Base
with st.sidebar:
    st.header("⚙️ System Status")
    st.success("Vector Store: ChromaDB Ready")
    st.success("LLM Engine: Llama 3 (Ollama)")

    st.divider()

    st.header("📚 Vector Knowledge Base")
    st.info("Currently active architecture patterns:")
    st.markdown("""
    - **Real-Time Tracking:** WebSockets, Redis Pub/Sub, PostgreSQL + PostGIS
    - **Media Streaming:** WebRTC, FFmpeg, AWS S3
    - **Messaging/Social:** Neo4j, MongoDB
    """)

# Main Interactive UI
st.subheader("💡 Define Your Application Idea")
user_prompt = st.text_area(
    label="Enter project requirements or system features:",
    placeholder=(
        "e.g., Delivery application with real-time driver tracking on the map"
    ),
    height=120,
)

generate_btn = st.button(
    "🚀 Generate Architecture Report", type="primary", use_container_width=True
)

# Generate and Display Report
if generate_btn:
    if not user_prompt.strip():
        st.warning("Please enter a project idea first.")
    else:
        with st.spinner(
            "Retrieving architecture context and running analysis..."
        ):
            try:
                report = rag_engine.generate_architecture_report(user_prompt)

                st.divider()
                st.subheader("📋 Architectural Report")
                st.markdown(report)

            except Exception as e:
                st.error(
                    f"An error occurred while generating the report: {str(e)}"
                )