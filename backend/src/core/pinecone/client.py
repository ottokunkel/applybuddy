"""
A singleton client for managing Pinecone vector database connections.
"""

import os
from pinecone import Pinecone
from pinecone.db_control.models.index_model import IndexModel
from typing import Optional
from dotenv import load_dotenv

load_dotenv()

class PineconeClient:
    
    _instance: Optional[Pinecone] = None


    @classmethod
    def get_client(cls) -> Pinecone:
        """
        Get or create the singleton Pinecone client instance.
        
        Returns:
            Pinecone: The singleton Pinecone client instance.
            
        Raises:
            ValueError: If the PINECONE_API_KEY environment variable is not set.
        """
        if cls._instance is None:
            api_key = os.getenv("PINECONE_API_KEY")
            if not api_key:
                raise ValueError("PINECONE_API_KEY environment variable is required")
            cls._instance = Pinecone(api_key=api_key)
        return cls._instance


    @classmethod
    def get_index(cls, index_name: str) -> IndexModel:
        """
        Get or create a Pinecone index with the specified name.
        
        Args:
            index_name (str): The name of the Pinecone index to retrieve or create.
            
        Returns:
            Index: The Pinecone index instance.
        """
        client = cls.get_client()
        if not client.has_index(index_name):
            client.create_index_for_model(
                name=index_name,
                cloud="aws",
                region="us-east-1",
                embed={
                    "model": "llama-text-embed-v2",
                    "field_map": {"text": "chunk_text"}
                }
            )
        return client.Index(index_name)
    


pc = PineconeClient.get_client()