
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

documents = [
    "Artificial intelligence enables machines to perform intelligent tasks.",
    "Natural language processing helps computers understand human language.",
    "Machine learning learns patterns from data to make predictions.",
    "Information retrieval searches and ranks documents relevant to a query.",
]

query = input("Enter search query (example: language processing): ").strip()
if not query:
    print("Query cannot be empty.")
else:
    vectorizer = TfidfVectorizer(stop_words="english")
    matrix = vectorizer.fit_transform(documents + [query])
    doc_vectors = matrix[:-1]
    query_vector = matrix[-1]
    scores = cosine_similarity(query_vector, doc_vectors).flatten()
    ranking = sorted(enumerate(scores, start=1), key=lambda item: item[1], reverse=True)

    print("\\nRanked documents:")
    for rank, (doc_id, score) in enumerate(ranking, start=1):
        print(f"{rank}. Document {doc_id} (score={score:.4f}): {documents[doc_id - 1]}")
