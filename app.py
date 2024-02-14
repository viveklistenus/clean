<<<<<<< HEAD
from prompts import generate_article_prompt
from llm import LLM

input_variable = "Hinduism"

prompt = generate_article_prompt(input_variable)

output = LLM(prompt)

=======
from prompts import generate_article_prompt
from llm import LLM

input_variable = "Hinduism"

prompt = generate_article_prompt(input_variable)

output = LLM(prompt)

>>>>>>> 53af029 (first)
print(output)