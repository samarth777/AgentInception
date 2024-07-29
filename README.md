# AgentInception: Multi-Agent System Generator

![WhatsApp Image 2024-07-29 at 21 50 52](https://github.com/user-attachments/assets/23515372-6d65-47a6-b83b-6782306ce625)

**AgentInception** simplifies the creation AI agents for the users specific use cases using YAML configuration files and LlamaIndex. Ideal for building specialized agents like weather forecasters or customer service bots, AgentInception lets you focus on functionality without the hassle of boilerplate code.

## Features

- **Easy Configuration**: Define agents through simple natural language descriptions and the agent creates the appropriate agents and toold for you.
- **Function Integration**: Incorporate custom functions as tools.
- **Versatile Applications**: Create agents for various domains.
- **Custom Prompts**: Tailor each agent's prompt to its role.
- **Multi-Agent Support**: Manage multiple agents with distinct functions.
- **LlamaIndex Integration**: Utilize LlamaIndex for improved knowledge management and query capabilities.


## Setup

1. **Clone the Repo**:
   ```bash
   git clone https://github.com/samarth777/AgentInception.git
   cd AgentInception
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up your OpenAI API key**:
   - Create a `.env` file in the project root
   - Add your API key to the file:
     ```
     OPENAI_API_KEY=your-api-key-here
     ```

## Usage

### Step 1: Prepare Your Data

1. Create a `data` folder in the project root if it doesn't exist:
   ```bash
   mkdir data
   ```
2. Upload your documents (PDFs, text files, etc.) to the `data` folder. These documents will be used as the knowledge base for your agents.

### Step 2: Generate YAML Configuration

1. Run the YAML configuration generator:
   ```bash
   python createyaml.py
   ```
2. Follow the prompts to describe your multi-agent system requirements.
3. The script will generate a `generated_multi_agent_config.yaml` file in the project root.

### Step 3: Generate Multi-Agent System Code

1. Run the script to generate your multi-agent system code:
   ```bash
   python script.py
   ```
2. This will create a new file called `generated_multi_agent.py`.

### Step 4: Use Your Generated Multi-Agent System

Run your multi-agent system:
```bash
python generated_multi_agent.py
```

## Example YAML Configuration

```yaml
openai_api_key: "your-openai-api-key"
agents:
 - name: "Weather Forecaster"
   tool_name: "weather_query"
   model: "gpt-3.5-turbo"
   custom_prompt: "Provide weather forecasts."
   example_query: "What's the rainfall forecast for the next five days?"
tools:
 - name: "send_sms_with_subsidy_info"
   description: "Sends SMS with subsidy info."
   function: "send_sms_with_subsidy_info"
```

## Customization

Feel free to modify the `generated_multi_agent.py` file to add more functionality, improve interaction between agents, or integrate with other systems as needed.

## Troubleshooting

If you encounter any issues:
1. Ensure your OpenAI API key is correctly set in the `.env` file.
2. Check that your data files are properly placed in the `data` folder.
3. Verify that all dependencies are installed by running `pip install -r requirements.txt` again.

For any other problems, please open an issue on the GitHub repository.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=samarth777/AgentInception&type=Date)](https://star-history.com/#samarth777/AgentInception&Date)

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for details.
