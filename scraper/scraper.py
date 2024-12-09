from step_1_setup_db import connect_to_milvus
from step_2_scrape_articles import scrape_articles
from step_3_produce_vectors import produce_vectors
from step_4_insert_vectors import insert_vectors

if __name__ == "__main__":
  client = connect_to_milvus()
  articles = scrape_articles()
  data = produce_vectors(client, articles)
  insert_vectors(client, data)

  # Additional logic for querying the database using the client object can be added here.

  client.close()  # Close the connection to Milvus
