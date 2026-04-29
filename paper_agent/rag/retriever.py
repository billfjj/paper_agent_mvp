def retrieve(query: str, chunks: list[str], top_k: int = 5) -> list[str]:
    terms = {term.lower() for term in query.split()}
    scored = []
    for chunk in chunks:
        score = sum(1 for term in terms if term in chunk.lower())
        scored.append((score, chunk))
    scored.sort(key=lambda item: item[0], reverse=True)
    return [chunk for score, chunk in scored[:top_k] if score > 0]
