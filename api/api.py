from pymilvus import MilvusClient
from fastapi import FastAPI, Body

app = FastAPI()
client = MilvusClient("vecbase.db")  # Replace with your Milvus connection details

@app.post("/search")
async def search(query: str = Body(...)):
  """Searches the Milvus collection based on a text query."""
  try:
    # Replace with your actual embedding function
    embedding_fn = model.DefaultEmbeddingFunction()
    query_vectors = embedding_fn.encode_queries([query])

    res = client.search(
        collection_name="wiki_collection",
        data=query_vectors,
        limit=2,
        output_fields=["text", "subject"],
    )

    return res
  except Exception as e:
    print(e)
    return {"error": str(e)}

