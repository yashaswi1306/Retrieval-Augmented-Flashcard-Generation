import pandas as pd
import fitz

def text_extraction_from_pdf(pdf_path,start_page=0,end_page=-1):

    pdf_doc=fitz.open(pdf_path)

    if(end_page==-1):
        end_page=len(pdf_doc)

    data=[]

    for idx in range(start_page,end_page):

        page=pdf_doc.load_page(idx)
        text=page.get_text()

        data.append({
            'page': idx+1,
            'text': text
        })

    pdf_doc.close()

    return pd.DataFrame(data)

import re

def pre_processing(df):

    df=df.copy()

    for id in range(len(df)):

        txt=df.loc[id,'text']

        txt=re.sub(r'\n+','\n',txt)
        txt=re.sub(r'\t+','\n',txt)
        txt=re.sub(r'\s+','\n',txt)

        txt=txt.strip()

        df.loc[id,'text']=txt

    df.to_csv('Dataset_cleaned.csv', index=False)

    return df

def chunking(df, chunk_size=200,overlap=50):

    chunks=[]

    for idx,row in df.iterrows():

        page_num=row['page']
        text_full=row['text']
        words=text_full.split()

        start=0
        end=0

        while(end<len(words)):

            end=start+chunk_size

            if(end>=len(words)):
                chunk= " ".join(words[start:len(words)])
            else:
                chunk= " ".join(words[start:end])

            chunks.append(
                {
                    'Page':page_num,
                    'Chunk':chunk
                }
            )
            start+=(chunk_size-overlap)

    return chunks