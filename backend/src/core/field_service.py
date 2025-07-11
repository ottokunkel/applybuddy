import uuid
from src.core.pinecone.client import PineconeClient
from dotenv import load_dotenv
import os

load_dotenv()

namespace = os.getenv("PINECONE_NAMESPACE")
index_name = os.getenv("PINECONE_INDEX_NAME")
   
def create_field(question: str, answer: str) -> str:
    """Create a new field with question and answer."""
    field_id = str(uuid.uuid4())
    index = PineconeClient.get_index(index_name)
    combined_text = f"{question}"
    
    index.upsert_records(namespace,
        records=[
            {
                "_id": field_id,
                "chunk_text": combined_text,
                "answer": answer
            }
        ]
    )
        
    return field_id 