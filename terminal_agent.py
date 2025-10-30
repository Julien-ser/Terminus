import torch
from transformers import AutoTokenizer, AutoModelForCausalLM, pipeline
from langchain.agents import AgentExecutor, create_react_agent
from langchain.prompts import PromptTemplate
from langchain.tools import Tool
from langchain_community.tools import ShellTool
from langchain_community.llms import HuggingFacePipeline
import yaml

def load_config(config_path='config.yaml'):
    """Loads the configuration from a YAML file."""
    with open(config_path, 'r', encoding='utf-8') as f:
        return yaml.safe_load(f)

def load_model_and_tokenizer(model_name_or_path):
    """Loads the fine-tuned model and tokenizer."""
    tokenizer = AutoTokenizer.from_pretrained(model_name_or_path)
    model = AutoModelForCausalLM.from_pretrained(model_name_or_path)
    return tokenizer, model

def create_langchain_pipeline(tokenizer, model):
    """Creates a HuggingFace pipeline for LangChain."""
    pipe = pipeline(
        "text-generation",
        model=model,
        tokenizer=tokenizer,
        max_new_tokens=512,
        temperature=0.7,
        do_sample=True,
        pad_token_id=tokenizer.eos_token_id
    )
    return HuggingFacePipeline(pipeline=pipe)

def main():
    config = load_config()
    model_path = config['model']['fine_tuned_path']

    print(f"Loading model from {model_path}...")
    try:
        tokenizer, model = load_model_and_tokenizer(model_path)
        llm = create_langchain_pipeline(tokenizer, model)
        print("Model loaded successfully. Agentic mode enabled. Type 'exit' to quit.")
    except Exception as e:
        print(f"Error loading model: {e}")
        print("Falling back to simulated mode.")
        llm = None

    if llm:
        # Define tools
        shell_tool = ShellTool()
        tools = [shell_tool]

        # Define prompt template for ReAct agent
        template = """Answer the following questions as best you can. You have access to the following tools:

{tools}

Use the following format:

Question: the input question you must answer
Thought: you should always think about what to do
Action: the action to take, should be one of [{tool_names}]
Action Input: the input to the action
Observation: the result of the action
... (this Thought/Action/Action Input/Observation can repeat N times)
Thought: I now know the final answer
Final Answer: the final answer to the original input question

Begin!

Question: {input}
Thought:{agent_scratchpad}"""

        prompt = PromptTemplate.from_template(template)

        # Create ReAct agent
        agent = create_react_agent(llm, tools, prompt)
        agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True, handle_parsing_errors=True)

        while True:
            user_input = input("\nCyberSec Agent > ")
            if user_input.lower() == 'exit':
                break
            try:
                result = agent_executor.invoke({"input": user_input})
                print(f"Agent: {result['output']}")
            except Exception as e:
                print(f"Error during execution: {e}")
    else:
        # Simulated mode
        while True:
            user_input = input("\nCyberSec Agent (Simulated) > ")
            if user_input.lower() == 'exit':
                break
            print(f"Agent (Simulated): You asked: '{user_input}'. In agentic mode, I would execute commands like 'ls' or solve CTFs.")

if __name__ == '__main__':
    main()
