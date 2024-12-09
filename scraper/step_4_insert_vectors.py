from pymilvus import MilvusClient


def insert_vectors(client, data):
  """Inserts the provided data into the Milvus collection."""
  collection_name = "wiki_collection"
  res = client.insert(collection_name=collection_name, data=data)
  print(res)
