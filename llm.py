# llm.py
from langchain_community.llms import Bedrock

LLM = Bedrock(model_id="anthropic.claude-v2", model_kwargs={"temperature": 0})