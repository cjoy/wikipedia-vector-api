from pymilvus import model
from transformers import AutoTokenizer

def produce_vectors(client, documents):
  """Creates embeddings for provided documents and returns data for insertion."""
  embedding_fn = model.DefaultEmbeddingFunction()
  tokenizer = AutoTokenizer.from_pretrained("bert-base-uncased")

  max_length = 512
  truncated_documents = [doc[:max_length] for doc in documents]
  vectors = embedding_fn.encode_documents(truncated_documents)

  data = [
      {"id": i, "vector": vectors[i], "text": docs, "subject": "history"}
      for i, docs in enumerate(truncated_documents)
  ]

  return data