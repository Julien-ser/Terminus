import yaml
import pyarrow as pa
from datasets import Dataset
from huggingface_hub import login
import os
from transformers import AutoTokenizer, AutoModelForCausalLM, TrainingArguments, Trainer

from huggingface_hub import login

# This is a placeholder script for fine-tuning the model.
# Login to Hugging Face Hub
hf_token = os.environ.get("HF_TOKEN")
if hf_token:
    login(token=hf_token)
else:
    print("HF_TOKEN environment variable not set. Please set it to your Hugging Face token.")
# In a real implementation, you would use a library like Hugging Face's transformers
# to load the pre-trained model and fine-tune it on your custom dataset.

def fine_tune_model(config):
    """_summary_

    Args:
        config (_type_): _description_
    """    # Load the tokenizer and model
    tokenizer = AutoTokenizer.from_pretrained(config['model']['name'])
    # Set the padding token if it's not already set
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token

    model = AutoModelForCausalLM.from_pretrained(config['model']['name'])

    # Load the dataset
    with pa.OSFile(config['dataset_path'], 'rb') as source:
        table = pa.ipc.open_file(source).read_all()
    df = table.to_pandas()
    texts = [f"Problem: {row['problem_statement']}\nSolution: {row['output']}" for _, row in df.iterrows()]
    dataset = Dataset.from_dict({"text": texts})

    # Tokenize the dataset
    def tokenize_function(examples):
        return tokenizer(examples["text"], truncation=True, padding="max_length", max_length=512)
        
    tokenized_dataset = dataset.map(tokenize_function, batched=True)
    tokenized_dataset = tokenized_dataset.remove_columns(["text"])
    # Add the 'labels' column, which is required for training
    tokenized_dataset = tokenized_dataset.map(lambda examples: {'labels': examples['input_ids']}, batched=True)

    # Set up the training arguments
    training_args = TrainingArguments(
        output_dir=config['model']['fine_tuned_path'],
        num_train_epochs=config['hyperparameters']['epochs'],
        per_device_train_batch_size=config['hyperparameters']['batch_size'],
        learning_rate=config['hyperparameters']['learning_rate'],
        # Add evaluation strategy to monitor performance during training
        evaluation_strategy="epoch",
        # Add save strategy to save the model checkpoints
        save_strategy="epoch",
        # Load the best model at the end of training
        load_best_model_at_end=True,
    )

    # Create the trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=tokenized_dataset,
        eval_dataset=tokenized_dataset, # Using the same dataset for evaluation as an example
    )

    # Start the fine-tuning
    trainer.train()

    # Save the fine-tuned model
    model.save_pretrained(config['model']['fine_tuned_path'])
    tokenizer.save_pretrained(config['model']['fine_tuned_path'])

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_path', type=str, default='data/problem_solution_data.arrow')
    args = parser.parse_args()

    # Load the config file
    with open('config.yaml', 'r', encoding='utf-8') as f:
        config = yaml.safe_load(f)
    
    config['dataset_path'] = args.dataset_path

    # Fine-tune the model
    fine_tune_model(config)
