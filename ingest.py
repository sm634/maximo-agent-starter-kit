from connectors.vector_db_connector import ChromaDB

def ingest_documents():
    client = ChromaDB()
    print(f"Ingesting {client.pdf_path}")
    client.ingest_documents()

if __name__ == "__main__":
    ingest_documents()
