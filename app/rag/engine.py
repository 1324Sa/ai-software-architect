import os
from dotenv import load_dotenv
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()


class ArchitectRAGEngine:
    def __init__(self):
        print("Loading local Embeddings model...")
        self.embeddings = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

        self.vector_store = Chroma(
            collection_name="architecture_knowledge",
            embedding_function=self.embeddings,
            persist_directory=os.getenv("CHROMA_PERSIST_DIR", "./chroma_db"),
        )
        self.retriever = self.vector_store.as_retriever(search_kwargs={"k": 1})

        print("Connecting to local Llama3 model...")
        self.llm = OllamaLLM(model="llama3", temperature=0)

        # English prompt enforcing strict grounding and direct output
        self.prompt = ChatPromptTemplate.from_template(
            """You are a System Architecture AI Assistant. 
Generate a clean technical architecture report based STRICTLY AND ONLY on the provided Context.

RULES:
1. Use ONLY technologies mentioned in the Context.
2. Do NOT add conversational filler, intros, or post-notes (e.g., "Here is...", "Note:...").
3. Output MUST be entirely in English.

Context:
{context}

User Idea:
{question}

Architectural Report Structure:
1. Proposed Components & Technologies:
2. Real-Time Tracking Mechanism:
3. Technical Recommendations:"""
        )

    def seed_initial_knowledge(self, documents: list[str]):
        """Seed or reset vector store with given documents"""
        try:
            self.vector_store.delete_collection()
            self.vector_store = Chroma(
                collection_name="architecture_knowledge",
                embedding_function=self.embeddings,
                persist_directory=os.getenv("CHROMA_PERSIST_DIR", "./chroma_db"),
            )
            self.retriever = self.vector_store.as_retriever(
                search_kwargs={"k": 1}
            )
        except Exception:
            pass

        self.vector_store.add_texts(texts=documents)

    def format_docs(self, docs):
        return "\n".join(doc.page_content for doc in docs)

    def generate_architecture_report(self, query: str):
        docs = self.retriever.invoke(query)
        context = self.format_docs(docs)

        chain = self.prompt | self.llm | StrOutputParser()

        print("\n[Analyzing data and generating architectural report...]\n")
        return chain.invoke({"context": context, "question": query})