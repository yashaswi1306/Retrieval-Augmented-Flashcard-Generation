# AI Study Assistant - RAG Pipeline



The project processes an uploaded pdf to generate flashcards for last minute revision.
<br>
It retrieves the necessary parts in the pdf using semantic search (FAISS) relative to the revision topic.<br><br>
Then, it uses these parts as context for a large language model, to generate flashcards.  
<br>
<br>

## Project Features:

```
Upload the PDF file of a textbook or reading materials.


Select range of page numbers.


Extract text from pdf via PyMuPDF.


Text pre-processing and chunking.

HuggingFace Model : 'BAAI/bge-base-en-v1.5' for generating word embeddings via SentenceTransformers.

Enter topic for Revision.

Select number of flashcards you want to generate and the word limit per answer.

Semantic Search for text related to chosen topic using FAISS for context.

Transformers library to get local HuggingFace Model : 'Qwen/Qwen2.5-3B-Instruct.

Flashcard Processing to seperate Questions and Answers inorder to make a drop-down menu for flashcards.
```
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

<br>

## Process

### Phase 1:
Medical_Text_Extraction.ipynb:<br>
Made in google colab so there was gpu access thus less processing time.
<br>
Used for a specific reference doc (ICMR_Dataset.pdf).
<br>
Notebook makes it easire to spot WHERE a code breaks and leads a more structured approach to the problem.
<br>

### Phase 2:
Python files for each subtask:<br>
Easy to extrapolate these from the ipynb.
<br>
A test file used alonside each subtask in the pipeline to prevent errors from flowing downstream, culminating in test_generator.py
<br>

### Phase 3:
terminal_pipeline.py:<br>
Checks if pipeline works properly in terminal to simplify testing without the UI hassel
<br>

### Phase 3:
streamlit_pipeline.py:<br>
Final pipeline using streamlit.
<br>
As this was my first time using streamlit a bunch of refernce docs were used ('streamlit_reference_links/reference_doc.md')
<br>
test_streamlit.py used for debugging
<br>
