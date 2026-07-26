from transformers import pipeline, AutoModelForCausalLM, AutoTokenizer
import torch

def get_llm(model_name='Qwen/Qwen2.5-3B-Instruct'):

    tokenizer=AutoTokenizer.from_pretrained(model_name)
    model=AutoModelForCausalLM.from_pretrained(model_name)

    return tokenizer,model

def generate_flashcards(tokenizer,model,context,num_cards=5,max_words=30,max_new_tokens=500):

    prompt=f"""
    Use ONLY the context mentioned below to generate 5 flashcards.

    Context={context}

    1. Generate {num_cards} flashcards
    
    2. Each Ans should have maximum of {max_words} words.

    3. Flashcards should be structured as:

    Question:
    Answer:
    """

    messages=[
        {
            'role':'system',
            'content':'You are a Medical Professor teaching about terms used in limitation of treatment and providing pallitive end of life care.'
        },
        {
            'role':'user',
            'content':prompt
        }
    ]

    txt=tokenizer.apply_chat_template(messages,tokenize=False,add_generation_prompt=True)
    input=tokenizer(txt,return_tensors='pt')

    input=input.to(model.device)


    output=model.generate(
        input_ids=input.input_ids,
        attention_mask=input.attention_mask,
        max_new_tokens=max_new_tokens,
        do_sample=False,
        temperature=None
    )

    res=tokenizer.decode(output[0][input.input_ids.shape[1]:], skip_special_tokens=True)

    return res