import yaml
from transformers import AutoTokenizer, AutoModelForCausalLM

# This is a placeholder script for the main application.
# In a real implementation, you would load the fine-tuned model and create a
# command-line interface for interacting with it.

def main():
    """_summary_
    """    # Load the config file
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)

    # Load the fine-tuned model and tokenizer
    tokenizer = AutoTokenizer.from_pretrained(config['model']['fine_tuned_path'])
    model = AutoModelForCausalLM.from_pretrained(config['model']['fine_tuned_path'])

    # Start the interactive terminal session
    while True:
        # Get user input
        prompt = input("> ")

        # Generate a response
        inputs = tokenizer(prompt, return_tensors="pt")
        outputs = model.generate(**inputs)
        response = tokenizer.decode(outputs[0], skip_special_tokens=True)

        # Print the response
        print(response)

if __name__ == '__main__':
    main()
