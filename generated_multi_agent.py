
import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import QueryEngineTool, ToolMetadata
from llama_index.agent.openai import OpenAIAgent
from llama_index.core.memory import ChatMemoryBuffer
from llama_index.core.settings import Settings

# Set up OpenAI API key
os.environ["OPENAI_API_KEY"] = "YOUR_OPENAI_API_KEY"  # Replace with your actual API key

# Load documents
documents = SimpleDirectoryReader(input_dir="./data").load_data()


# Weather Forecaster Agent
def create_weather_forecaster_agent():
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
                name="weather_query",
                description="Queries the agromet advisory for weather-related information",
            ),
        ),
    ]

    # Set up memory
    memory = ChatMemoryBuffer.from_defaults(token_limit=2048)

    # Define custom prompt
    custom_prompt = '''
You are a Weather Forecaster AI assistant. Provide information about weather forecasts and related agricultural advice based on the given advisory.
    '''

    # Initialize agent
    agent_llm = OpenAI(temperature=0.7, model="gpt-3.5-turbo")
    return OpenAIAgent.from_tools(tools, llm=agent_llm, memory=memory, system_prompt=custom_prompt)

# Create Weather Forecaster Agent
weather_forecaster_agent = create_weather_forecaster_agent()

# Example usage
response = weather_forecaster_agent.chat("What's the rainfall forecast for the next five days?")
print("Weather Forecaster Agent Response:")
print(response)
print()
print("="*50)
print()


# Crop Advisor Agent
def create_crop_advisor_agent():
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
                name="crop_query",
                description="Queries the agromet advisory for crop-specific information and advice",
            ),
        ),
    ]

    # Set up memory
    memory = ChatMemoryBuffer.from_defaults(token_limit=2048)

    # Define custom prompt
    custom_prompt = '''
You are a Crop Advisor AI assistant. Provide crop-specific advice and management recommendations based on the given agricultural advisory.
    '''

    # Initialize agent
    agent_llm = OpenAI(temperature=0.7, model="gpt-3.5-turbo")
    return OpenAIAgent.from_tools(tools, llm=agent_llm, memory=memory, system_prompt=custom_prompt)

# Create Crop Advisor Agent
crop_advisor_agent = create_crop_advisor_agent()

# Example usage
response = crop_advisor_agent.chat("What are the management advisories for paddy cultivation?")
print("Crop Advisor Agent Response:")
print(response)
print()
print("="*50)
print()


# General Advisory Agent
def create_general_advisory_agent():
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
                name="general_advisory_query",
                description="Queries the agromet advisory for general weather-based advisories for the week",
            ),
        ),
    ]

    # Set up memory
    memory = ChatMemoryBuffer.from_defaults(token_limit=2048)

    # Define custom prompt
    custom_prompt = '''
You are a General Advisory AI assistant. Provide general weather-based advisories for the week based on the given agricultural advisory.
    '''

    # Initialize agent
    agent_llm = OpenAI(temperature=0.7, model="gpt-3.5-turbo")
    return OpenAIAgent.from_tools(tools, llm=agent_llm, memory=memory, system_prompt=custom_prompt)

# Create General Advisory Agent
general_advisory_agent = create_general_advisory_agent()

# Example usage
response = general_advisory_agent.chat("What are the weather advisories for this week?")
print("General Advisory Agent Response:")
print(response)
print()
print("="*50)
print()


    