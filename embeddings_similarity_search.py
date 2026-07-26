from sentence_transformers import SentenceTransformer
import torch

def load_model(model_name='BAAI/bge-base-en-v1.5'):

    device='cuda' if torch.cuda.is_available() else 'cpu'
    model=SentenceTransformer(model_name,device=device)

    return model

def word_embeddings(model,chunks):

    chunk_list=[a['Chunk'] for a in chunks]

    w_embed=model.encode(chunk_list,convert_to_numpy=True)

    return w_embed,chunk_list

import faiss
import numpy as np

def faiss_indexing(w_embed,path=None):

    dimension=w_embed.shape[1]
    index=faiss.IndexFlatL2(dimension)

    index.add(w_embed.astype('float32'))

    # faiss.write_index(index,path)

    return index

def load_index(path):

    return faiss.read_index(path)

def similarity_search(query,model,index,chunks,k=5):

    query_embed=model.encode([query],convert_to_numpy=True)
    dist,indices=index.search(query_embed.astype('float32'),k)

    return dist,indices

def get_results(query,model,index,chunks,k=5):

    result=[]
    dist,indices=similarity_search(query,model,index,chunks,k)

    for index in indices[0]:
        result.append(chunks[index])

    return result
