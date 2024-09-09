"""
Assistente
"""
import vertexai
from vertexai.generative_models import GenerativeModel
from vertexai.language_models import TextEmbeddingInput, TextEmbeddingModel
from google.cloud.firestore_v1.vector import Vector
from google.cloud.firestore_v1.base_vector_query import DistanceMeasure
from google.cloud.firestore_v1.collection import CollectionReference

import config

class BotQS():
    def __init__(
            self,
            model_name:str,
            generation_config:dict=None,
            safety_settings:dict=None,
            system_prompt:str=None,
            init_msg:str=None,
            db_firestore:CollectionReference=None,
            vector_model:str=None
        ):
        self.init_msg = init_msg
        self.model_name = model_name
        self.generation_config = generation_config if generation_config is not None else config.CHAT_GENAI_CONFIG
        self.safety_settings = safety_settings if safety_settings is not None else config.CHAT_GENAI_SAFE
        self.system_prompt = system_prompt if system_prompt is not None else []
        self.init_msg = init_msg if init_msg is not None else config.CHAT_MSG_INIT

        vertexai.init(project=config.PROJECT_ID, location=config.REGION_ID)

        self.model = GenerativeModel(
            self.model_name,
            system_instruction=self.system_prompt
        )
        self.db_firestore = db_firestore
        self.vector_model = vector_model if vector_model is not None else config.CHAT_VECTOR_CONFIG["model"]
        self.vector = TextEmbeddingModel.from_pretrained(self.vector_model)

    def _get_vector(self, query:list):
        embeddings = self.vector.get_embeddings(
            [TextEmbeddingInput(text, "RETRIEVAL_QUERY") for text in query]
        )
        return [embedding.values for embedding in embeddings]

    def find_rag(self, query:str, field:str, limit:int) -> list:
        """Busca RAG
        
        
        
        Parameters
        ----------
        query : str
            query a ser feita na base
        field : str
            campo de vetor
        limit : int
            limite de mensagem
        
        Returns
        -------
        list
            top n conteudos
        """        
        rag = self.db_firestore.find_nearest(
            vector_field=field,
            query_vector=Vector(self._get_vector([query])[0]),
            distance_measure=DistanceMeasure.EUCLIDEAN,
            limit=limit
        )
        return [item.to_dict() for item in rag.get()]

    def get_chat(self):
        """Gera conversa
        
        
        
        Returns
        -------
        GenerativeModel
            conversa aberta
        """        
        return self.model.start_chat()
        
