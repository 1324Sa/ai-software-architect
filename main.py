from app.rag.engine import ArchitectRAGEngine


def main():
    rag = ArchitectRAGEngine()

    # Knowledge base in English for seamless retrieval and execution
    knowledge_base = [
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

    print("Seeding vector knowledge base...")
    rag.seed_initial_knowledge(knowledge_base)

    user_idea = (
        "Delivery application with real-time driver tracking on the map"
    )

    # Generate architectural report
    report = rag.generate_architecture_report(user_idea)

    print("=" * 60)
    print("FINAL ARCHITECTURAL REPORT:")
    print("=" * 60)
    print(report)


if __name__ == "__main__":
    main()