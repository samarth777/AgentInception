import yaml
from jinja2 import Template

def load_yaml_config(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def generate_agent_code(config):
    template = Template("""
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.settings import Settings

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = " openai_api_key "

# Load documents
documents = SimpleDirectoryReader(input_dir=" pdf_path ").load_data()

{% for agent in agents %}
# {{ agent.name }} Agent
def create_{{ agent.name.lower().replace(' ', '_') }}_agent():
    # Create index
    Settings.llm = OpenAI(temperature=0.7, model="gpt-3.5-turbo")
    index = VectorStoreIndex.from_documents(documents)

    # Create query engine
    query_engine = index.as_query_engine(similarity_top_k=7)

    # Define tools
    tools = [
        QueryEngineTool(
            query_engine=query_engine,
            metadata=ToolMetadata(
                name="{{ agent.tool_name }}",
                description="{{ agent.tool_description }}",
            ),
        ),
    ]

    # Set up memory
    memory = ChatMemoryBuffer.from_defaults(token_limit=2048)

    # Define custom prompt
    custom_prompt = '''
{{ agent.custom_prompt }}
    '''

    # Initialize agent
    agent_llm = OpenAI(temperature=0.7, model="gpt-3.5-turbo")
    return OpenAIAgent.from_tools(tools, llm=agent_llm, memory=memory, system_prompt=custom_prompt)

# Create {{ agent.name }} Agent
{{ agent.name.lower().replace(' ', '_') }}_agent = create_{{ agent.name.lower().replace(' ', '_') }}_agent()

# Example usage
response = {{ agent.name.lower().replace(' ', '_') }}_agent.chat("{{ agent.example_query }}")
print("{{ agent.name }} Agent Response:")
print(response)
print()
print("="*50)
print()

{% endfor %}
    """)
    
    return template.render(config)

def main():
    config = load_yaml_config('generated_multi_agent_config.yaml')
    agent_code = generate_agent_code(config)
    
    with open('generated_multi_agent.py', 'w') as file:
        file.write(agent_code)
    
    print("Multi-agent code has been generated and saved to 'generated_multi_agent.py'")

if __name__ == "__main__":
    main()