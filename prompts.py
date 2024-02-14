# prompts.py
from langchain.prompts import PromptTemplate

def generate_article_prompt(input_variable):

  prompt_template = PromptTemplate(

    input_variables=["input_variable"],

    template="Write an article about {input_variable}",

  )

  return prompt_template.format(input_variable=input_variable)