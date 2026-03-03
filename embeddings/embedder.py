import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.cluster import KMeans
from typing import List, Tuple, Dict
import config

class EmbeddingEngine:
    def __init__(self, model_name: str = config.EMBEDDING_MODEL):
        self.model = SentenceTransformer(model_name)
        self.stored_embeddings = []
        self.stored_texts = []
    
    def embed_text(self, text: str) -> np.ndarray:
        return self.model.encode([text])[0]
    
    def embed_batch(self, texts: List[str]) -> np.ndarray:
        return self.model.encode(texts)
    
    def compute_similarity(self, embedding1: np.ndarray, embedding2: np.ndarray) -> float:
        return cosine_similarity([embedding1], [embedding2])[0][0]
    
    def find_most_similar(self, query_embedding: np.ndarray, threshold: float = config.SIMILARITY_THRESHOLD) -> Tuple[float, int]:
        if not self.stored_embeddings:
            return 0.0, -1
        
        similarities = cosine_similarity([query_embedding], self.stored_embeddings)[0]
        max_similarity = np.max(similarities)
        max_index = np.argmax(similarities)
        
        return max_similarity, max_index if max_similarity >= threshold else -1
    
    def is_novel(self, text: str, threshold: float = config.SIMILARITY_THRESHOLD) -> Tuple[bool, float]:
        embedding = self.embed_text(text)
        max_similarity, _ = self.find_most_similar(embedding, threshold)
        return max_similarity < threshold, max_similarity
    
    def add_to_store(self, text: str, embedding: np.ndarray = None):
        if embedding is None:
            embedding = self.embed_text(text)
        self.stored_embeddings.append(embedding)
        self.stored_texts.append(text)
    
    def cluster_attacks(self, embeddings: np.ndarray, n_clusters: int = 5) -> np.ndarray:
        if len(embeddings) < n_clusters:
            n_clusters = len(embeddings)
        
        kmeans = KMeans(n_clusters=n_clusters, random_state=42)
        return kmeans.fit_predict(embeddings)
    
    def get_cluster_summary(self, texts: List[str], embeddings: np.ndarray) -> Dict[int, List[str]]:
        clusters = self.cluster_attacks(embeddings)
        cluster_summary = {}
        
        for i, cluster_id in enumerate(clusters):
            if cluster_id not in cluster_summary:
                cluster_summary[cluster_id] = []
            cluster_summary[cluster_id].append(texts[i])
        
        return cluster_summary