import os
import yaml
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.memory import ChatMemoryBuffer

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"  # Replace with your actual API key

def generate_yaml(config):
    """Generate YAML file from the given configuration."""
    with open("generated_multi_agent_config.yaml", "w") as file:
        yaml.dump(config, file, default_flow_style=False)
    return "YAML configuration file has been generated as 'generated_multi_agent_config.yaml'"

# Define tool
yaml_tool = FunctionTool.from_defaults(
    fn=generate_yaml,
    name="generate_yaml",
    description="Generates a YAML configuration file for the multi-agent system.",
)

# Custom prompt for the agent
CUSTOM_PROMPT = """
You are an intelligent AI assistant designed to help users create YAML configuration files for multi-agent systems. Your task is to engage in a conversation with the user, understand their requirements, and then create an appropriate YAML configuration based on that information.

Follow these guidelines:
1. Start by greeting the user and asking about their project or the type of multi-agent system they want to create.
2. Ask questions to gather information about:
   - The overall purpose of the multi-agent system
   - The number of agents they need
   - The specific tasks or roles for each agent
   - Any special requirements or tools each agent might need
3. Based on their responses, suggest appropriate configurations for each agent, including:
   - Agent name
   - Tool name
   - Tool description
   - Custom prompt
   - Example query
    strictly follow this format:
    agents:
    - name: "Weather Forecaster"
        tool_name: "weather_query"
        tool_description: "Queries the agricultural advisory for weather-related information"
        custom_prompt: |
        You are a Weather Forecaster AI assistant. Provide information about weather forecasts and related agricultural advice based on the given advisory.
        example_query: "What's the rainfall forecast for the next five days?"

    - name: "Crop Advisor"
        tool_name: "crop_query"
        tool_description: "Queries the agricultural advisory for crop-specific information and advice"
        custom_prompt: |
        You are a Crop Advisor AI assistant. Provide crop-specific advice and management recommendations based on the given agricultural advisory.
        example_query: "What are the management advisories for paddy cultivation?"

4. Confirm with the user if the suggested configuration is correct.
5. Once all information is gathered and confirmed, use the generate_yaml tool to create the YAML configuration file.

Remember:
- Use conversational language and keep the interaction natural.
- Ask follow-up questions to clarify any ambiguous points.
- Provide explanations or suggestions if the user seems unsure about any aspect.
- Be adaptive to the user's level of expertise - offer more guidance to beginners and allow more customization for experienced users.
- Don't hesitate to suggest best practices or improvements to their system design.

Always prioritize understanding the user's needs before generating the configuration.
"""

# Initialize the agent
llm = OpenAI(temperature=0.7, model="gpt-4o")
memory = ChatMemoryBuffer.from_defaults(token_limit=2048)
agent = OpenAIAgent.from_tools([yaml_tool], system_prompt=CUSTOM_PROMPT, memory=memory, llm=llm)

def run_interactive_agent():
    print("Welcome to the Interactive YAML Config Generator!")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit', 'bye']:
            print("Thank you for using the Interactive YAML Config Generator. Goodbye!")
            break
        
        response = agent.chat(user_input)
        print(f"Assistant: {response}")

if __name__ == "__main__":
    run_interactive_agent()