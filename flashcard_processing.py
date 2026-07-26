import re

def flashcard_gen(res):

    flashcards=[]
    pattern=r"Question:\s*(.+?)\s*Answer:\s*(.+?)(?=$|Question:)"
    fc_txt=re.findall(pattern,res,re.DOTALL)

    for question, ans in fc_txt:
        flashcards.append(
            {
                'Question': question,
                'Answer' : ans
            }
        )

    return flashcards
