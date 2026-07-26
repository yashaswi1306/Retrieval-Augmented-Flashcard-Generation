from pdf_text_extraction import *
from embeddings_similarity_search import *
from flashcard_generator import *
from flashcard_processing import *

import streamlit as st

st.set_page_config(page_title='Flashcard Generator', layout='wide')

st.title('AI Study Assistant for Flashcard Generation', text_alignment='center')
st.subheader("It's Revision Time!", text_alignment='center')

if 'time_to_kassi' not in st.session_state:
    st.session_state['time_to_kassi']=0

col1,col2,col3=st.columns(3,vertical_alignment='center')

with col1:
    pdf_doc=st.file_uploader('Upload PDF Doc:',type='pdf')
with col2:
    start=st.number_input("Start Page Number", value=0,min_value=0)

with col3:
    end=st.number_input("End Page Number (-1 for Default):", value=-1,min_value=-1)

if (st.button("Read PDF")):

    with st.spinner('Extracting Text...'):
        df = text_extraction_from_pdf(pdf_doc,start_page=start,end_page=end)
        df= pre_processing(df)
        chunks=chunking(df)

    with st.spinner('Loading Embedding Model...'):
        embed_model=load_model()

    with st.spinner('Creating word embeddings...'):
        w_embed,chunk_list=word_embeddings(embed_model,chunks)

    with st.spinner('FAISS Indexing...'):
         index=faiss_indexing(w_embed)

    with st.spinner('Loading Model...'):
        tokenizer,llm=get_llm()

    st.session_state['time_to_kassi']=1
    st.session_state['embed_model']=embed_model
    st.session_state['chunk_list']=chunk_list
    st.session_state['index']=index
    st.session_state['tokenizer']=tokenizer
    st.session_state['llm']=llm

    st.badge('PDF Processed Successfully!', icon=':material/check:', color='green')

if st.session_state['time_to_kassi']:

    col1,col2,col3=st.columns(3,vertical_alignment='center')

    with col1:
        query=st.text_input("Enter Revision Topic:")
    with col2:
        k=st.slider('Enter number of flashcards to generate:', min_value=1, max_value=10, step=1)
    with col3:
        max_words=st.number_input('Enter preferred answer word length: (Enter -1 for default)', value=-1, min_value=-1)

    if st.button("Generate Flashcards"):

        res=get_results(query,st.session_state['embed_model'],st.session_state['index'],st.session_state['chunk_list'],k)
        context="\n".join(res)

        with st.spinner('Generating Flashcards...'):
            if(max_words==-1):
                res=generate_flashcards(st.session_state['tokenizer'],st.session_state['llm'],context,num_cards=k)
            else:
                res=generate_flashcards(st.session_state['tokenizer'], st.session_state['llm'],context,num_cards=k,max_words=max_words)

        st.header("Here are your flashcards. All the Best!")

        flashcards=flashcard_gen(res)


        for card in flashcards:
            
            with st.expander(f"Question: {card['Question']}"):
                st.markdown(f"""
<div style=
"background-color: #a9dfeb;
border-radius: 10px;
padding: 10px 15px;"
>
Answer:
{card['Answer']}
</div>""",unsafe_allow_html=True)

