import yaml
from langchain.prompts import PromptTemplate


# Load the .prompt.yml file
with open('/home/illia/work/git-evals-test/prompts/check-error.prompt.yml', 'r') as file:
    prompt_data = yaml.safe_load(file)

# Extract the system prompt
system_prompt = next(
    (message['content'] for message in prompt_data['messages'] if message['role'] == 'system'),
    None
)

# Create a LangChain prompt template
prompt_template = PromptTemplate(
    input_variables=["input_text"],
    template=f"{system_prompt}\nUser input: {{input_text}}"
)

# Use the prompt template in your LangChain pipeline
user_input = "Explain how to use GitHub Actions."
formatted_prompt = prompt_template.format(input_text=user_input)
print(formatted_prompt)