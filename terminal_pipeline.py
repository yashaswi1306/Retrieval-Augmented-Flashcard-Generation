from pdf_text_extraction import *
from embeddings_similarity_search import *
from flashcard_generator import *

def main():

    print("AI Study Assistant for Flashcard Generation")

    pdf_path=input("Enter pdf path: ")

    flag=input("Do you want to specify start and end page (y/n): ")

    if (flag=='y') or (flag=='Y'):
        start=int(input("Enter start page number: (Enter 0 for default)"))
        end=int(input("Enter end page number: (Enter -1 for default)"))
    else:
        start=0
        end=-1

    print("Extracting text...")

    df = text_extraction_from_pdf(pdf_path,start_page=start,end_page=end)
    df= pre_processing(df)
    print('Number of Pages: ', len(df))

    print("Chunking...")
    chunks=chunking(df)
    print('Number of Chunks: ',len(chunks))

    print('Loading Embedding Model...')
    embed_model=load_model()

    print('Creating word embeddings...')
    w_embed,chunk_list=word_embeddings(embed_model,chunks)

    print('FAISS Indexing...')
    index=faiss_indexing(w_embed)

    print('Loading Model...')
    tokenizer,llm=get_llm()

    ## Query loop

    while True:

        query=input('Enter topic for revision (else fin): ')

        if(query=="fin"):
            break

        k=int(input('Enter number of flashcards to generate:'))
        max_words=int(input('Enter preferred answer word length: (Enter -1 for default)'))
        res=get_results(query,embed_model,index,chunk_list,k)
        context="\n".join(res)


        print('Generating Flashcards...')
        if(max_words==-1):
            res=generate_flashcards(tokenizer,llm,context,num_cards=k)
        else:
            res=generate_flashcards(tokenizer,llm,context,num_cards=k,max_words=max_words)


        print(res)

if __name__=='__main__':
    main()