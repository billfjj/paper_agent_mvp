class VectorStorePlaceholder:
    """Placeholder for Chroma or Qdrant integration."""

    def __init__(self) -> None:
        self.items: list[dict] = []

    def add(self, text: str, metadata: dict | None = None) -> None:
        self.items.append({"text": text, "metadata": metadata or {}})

    def all(self) -> list[dict]:
        return self.items
