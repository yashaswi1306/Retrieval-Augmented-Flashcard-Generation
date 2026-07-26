from pdf_text_extraction import *

df = text_extraction_from_pdf('reference_prev_proj/ICMR_Dataset.pdf',start_page=23,end_page=50)
df= pre_processing(df)
chunks=chunking(df)

print('Number of Pages: ', len(df))
print('Number of Chunks: ',len(chunks))
print(chunks[0])