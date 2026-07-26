from pdf_text_extraction import *

df = text_extraction_from_pdf('reference_prev_proj/ICMR_Dataset.pdf',start_page=23,end_page=50)
df= pre_processing(df)
chunks=chunking(df)

print('Number of Pages: ', len(df))
print('Number of Chunks: ',len(chunks))
print(chunks[0])

from embeddings_similarity_search import *

embed_model=load_model()

w_embed,chunk_list=word_embeddings(embed_model,chunks)

index=faiss_indexing(w_embed)

query='Palliative Sedation'

res=get_results(query,embed_model,index,chunk_list,5)

print(len(res))
print(res)

context="\n".join(res)
print(len(context))
print(context)

from flashcard_generator import *

tokenizer,llm=get_llm()
res=generate_flashcards(tokenizer,llm,context)

print(res)
