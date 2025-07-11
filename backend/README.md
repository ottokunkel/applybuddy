## Backend Outline
Given a question from a form, it should query the vector database and return possible fields which could contain the answer. An LLM then checks whether these fields do contain an answer and then returnn an error if not and the answer of what to input if so. 

- **Overview**
  - Purpose: Backend for Apply Buddy, providing API endpoints to interact with a vector database.

- **Key Endpoints**
  - `/api/v1/fields`: Endpoints to create and query fields in the vector database.
  - `/health`: Health check endpoint.

- **Environment**
  - Requires `PINECONE_API_KEY` in environment variables.

**Requirements**
* [ ] - upload single query and hold the answer
* [ ] - rewrite queries for more robust RAG
* [ ] - query queries given a string from a field
* [ ] - determine if database contains answer
* [ ] - rewrite answer