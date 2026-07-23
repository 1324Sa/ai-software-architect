# 🏗️ AI Software Architect

An intelligent, RAG-powered Software Architecture Generator built with **Streamlit**, **ChromaDB**, **Hugging Face Embeddings**, and **Llama 3 (via Ollama)**. This platform helps developers and system architects automatically generate detailed, production-grade architectural design reports grounded in a specialized vector knowledge base.

---

## 🌟 Features

- **🔍 Grounded Architecture Recommendations (RAG):** Eliminates model hallucinations by context-retrieving verified architecture design patterns using ChromaDB.
- **⚡ Local & Private LLM Inference:** Runs entirely locally using **Ollama** and **Llama 3**, ensuring no proprietary system requirements or data leave your environment.
- **🎨 Interactive Streamlit UI:** Simple and intuitive dashboard to specify system constraints, view active knowledge vectors, and generate structural blueprints.
- **🛠️ Modular System Design:** Clear directory layout separating vector storage, RAG engines, validation, and user interface components.

---

## 🛠️ Tech Stack

| Component | Technology |
| :--- | :--- |
| **Frontend Framework** | [Streamlit](https://streamlit.io/) |
| **Vector Database** | [ChromaDB](https://www.trychroma.com/) |
| **Embedding Model** | Hugging Face Transformers / Sentence-Transformers |
| **LLM Engine** | Llama 3 via [Ollama](https://ollama.com/) |
| **Language & Tools** | Python 3.11+, PyTorch |

---

## 🏗️ System Architecture & Workflow

1. **User Request:** The user provides a high-level system prompt (e.g., *"Food delivery application with real-time driver tracking"*).
2. **Context Retrieval:** `ArchitectRAGEngine` searches `ChromaDB` for relevant system design patterns, technologies, and infrastructure requirements.
3. **Prompt Augmentation:** The query is combined with retrieved technical context and fed into Llama 3 with strict system instructions.
4. **Report Generation:** A comprehensive architectural evaluation report is rendered on the UI, outlining databases, streaming layers, and protocols.

---

## 📂 Project Structure

```text
ai-software-architect/
│
├── app/
│   ├── core/           # Configuration & environment setups
│   ├── rag/            # Vector store management & RAG engine logic
│   │   ├── engine.py   # Main ArchitectRAGEngine
│   │   └── __init__.py
│   ├── validators/     # Input & prompt validation rules
│   └── __init__.py
│
├── chroma_db/          # Local ChromaDB persistent vector database
├── streamlit_app.py    # Streamlit Web Dashboard entry point
├── requirements.txt    # Project dependencies
└── README.md           # Project documentation
