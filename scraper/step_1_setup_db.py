from pymilvus import MilvusClient

def connect_to_milvus(host="vecbase.db"):
  """Connects to the Milvus client and handles collection creation."""
  client = MilvusClient(host)
  collection_name = "wiki_collection"

  if client.has_collection(collection_name):
    client.drop_collection(collection_name)

  client.create_collection(
      collection_name=collection_name,
      dimension=768,  # Adjust dimension based on your embedding model
  )

  return client
