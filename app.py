import autogen
import os

config_list = [{"model": "gpt-3.5-turbo-16k", "api_key": os.environ["OPENAI_API_KEY"]}]

llm_config = {}
