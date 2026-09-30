from src.search import RAGSearch

# Example usage
if __name__ == "__main__":
    
    rag_search = RAGSearch()
    queries = ["what is machine learning",
                "What is attention mechanism"]
    for query in queries:
        print("\n Question")
        summary = rag_search.search_and_summarize(query, top_k=3)
        print("Summary:", summary)