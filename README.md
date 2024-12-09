# README
## Overview
This project is a FastAPI application that interacts with a Milvus database to perform text search queries. The application includes a scraper to fetch data from Wikipedia, vectorize it, and index the content in Milvus.

## Prerequisites
* Python 3.8+
* pip (Python package installer)
* Milvus server
* uvicorn (ASGI server for FastAPI)

## Installation
### Clone the repository:
```sh
git clone https://github.com/cjoy/vecdb-api.git
cd your-project
```

### Create and activate a virtual environment:
```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

### Install the required dependencies:
```sh
pip install -r requirements.txt
```


## Setup
1. Ensure that the Milvus server is running and accessible. (By default, we store data to a file locally, but you can change the configuration in `api/config.py` to connect to a remote Milvus server.)
2. Scrape data from Wikipedia, vectorize it, and index the content in Milvus:
```sh
python scraper/scraper.py
```


## Running the Application
Start the FastAPI application using uvicorn:
```sh
uvicorn api.api:app --host 0.0.0.0 --port 8000
```

The application will be available at `http://localhost:8000`.

## Usage
You can send a POST request to the `/search` endpoint to perform a search query. Here is an example using requests in Python:

```python
import requests

query = "Who is Alan Turing?"
url = "http://localhost:8000/search"

response = requests.post(url, json={"query": query})

if response.status_code == 200:
    data = response.json()
    print(data)  # This will print the search results from Milvus
else:
    print(f"Error: {response.status_code}")
```

Or using curl:
```sh
curl -X POST "http://localhost:8000/search" -H "Content-Type: application/json" -d '{"query": "Who is Alan Turing?"}'
```

## Troubleshooting
If you encounter any issues, please check the following:

* Ensure that the Milvus server is running and accessible.
* Verify that the data has been successfully indexed in Milvus.
* Check the logs for any error messages and resolve them accordingly.

# License
This project is licensed under the MIT License. See the LICENSE file for details.