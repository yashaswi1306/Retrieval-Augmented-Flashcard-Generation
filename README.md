# AI Study Assistant - RAG Pipeline

The project processes an uploaded pdf to generate flashcards for last minute revision. 
It retrieves the necessary parts in the pdf using semantic search (FAISS) relative to the revision topic.
Then, it uses these parts as context for a large language model, to generate flashcards.

## Project Features:

```
-> Upload the PDF file of a textbook or reading materials.
-> Select range of page numbers.
-> Extract text from pdf via PyMuPDF.
-> Text pre-processing and chunking.
-> SentenceTransformers used for HuggingFace Model : 'BAAI/bge-base-en-v1.5' for generating word embeddings.
-> Enter topic for Revision.
-> Select number of flashcards you want to generate and the word limit per answer.
-> Semantic Search for text related to chosen topic using FAISS for context.
-> Transformers library to get local HuggingFace Model : 'Qwen/Qwen2.5-3B-Instruct'
-> Flashcard Processing to seperate Questions and Answers inorder to make a drop-down menu for flashcards.
```

