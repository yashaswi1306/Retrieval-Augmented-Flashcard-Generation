# AI Study Assistant - RAG Pipeline



<br>
The project processes an uploaded pdf to generate flashcards for last minute revision. 
It retrieves the necessary parts in the pdf using semantic search (FAISS) relative to the revision topic.
Then, it uses these parts as context for a large language model, to generate flashcards.  
<br>
<br>

## Project Features:


-> Upload the PDF file of a textbook or reading materials.<br>
-> Select range of page numbers.<br>
-> Extract text from pdf via PyMuPDF.<br>
-> Text pre-processing and chunking.<br>
-> HuggingFace Model : 'BAAI/bge-base-en-v1.5' for generating word embeddings via SentenceTransformers.<br>
-> Enter topic for Revision.<br>
-> Select number of flashcards you want to generate and the word limit per answer.<br>
-> Semantic Search for text related to chosen topic using FAISS for context.<br>
-> Transformers library to get local HuggingFace Model : 'Qwen/Qwen2.5-3B-Instruct'<br>
-> Flashcard Processing to seperate Questions and Answers inorder to make a drop-down menu for flashcards
<br>
<br>

## Python Libraries Used:

-> Streamlit <br>
-> FAISS <br>
-> SentenceTransformers <br>
-> PyMuPDF<br>
-> Transformers <br>
-> Regex 
<br>
<br>

## Usage:


```
git clone <repo url>
```
```
python -m venv .venv
```
```
source .venv/bin/activate
```
```
pip install -r requirements.txt
```
```
streamlit run streamlit_pipeline.py
```

<br>


## Pipeline:

```
streamlit_pipeline.py
pdf_extraction.py
embeddings_similarity_search.py
flashcard_generator.py
flashcard_processing.py
```



