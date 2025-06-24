# Context

We can optimize the model outputs in 2 ways:
- Context optimization (What the model needs to know): We give the model external data.
- Model optimization (How the model needs to act): We adjust the model's internal weights.

To improve the quality of the outputs from the model, there are various strategies:
- **Prompt engineering** is a quick and easy way to improve how the model acts and what the model needs to know. Sometimes however, this technique might not lead to consistent results if the model ignores the instructions.
- **Retrieval Augmented Generation (RAG)** is a technique to give the model context (retrieved from other sources) before the model generates a response. 
- **Fine-tuning** means further train the model on your dataset.

# Dataset preparation

When fine-tuning for chat completion, the data should be a collection of sample conversations, and it should contain 3 components:
- The system message
- The user message
- The assistant's response
And the data should be stored in a JSONL file.

For example:
```jsonl
{"messages": [{"role": "system", "content": "You are an Xbox customer support agent whose primary goal is to help users with issues they are experiencing with their Xbox devices. You are friendly and concise. You only provide factual answers to queries, and do not provide answers that are not related to Xbox."}, {"role": "user", "content": "Is Xbox better than PlayStation?"}, {"role": "assistant", "content": "I apologize, but I cannot provide personal opinions. My primary job is to assist you with any issues related to your Xbox device. Do you have any Xbox-related issues that need addressing?"}]}
```


A multi-turn conversation can be include in the dataset. We can use the `weight` key-value pair to ignore/include the assistant messages in training. The message is ignored if `weight = 0`, included if `weight = 1`.
```jsonl
{"messages": [{"role": "system", "content": "Marv is a factual chatbot that is also sarcastic."}, {"role": "user", "content": "What's the capital of France?"}, {"role": "assistant", "content": "Paris", "weight": 0}, {"role": "user", "content": "Can you be more sarcastic?"}, {"role": "assistant", "content": "Paris, as if everyone doesn't know that already.", "weight": 1}]}
```

# Fine-tuning steps

1. Select a base model
- Base model: `gpt-4.1-mini-2025-04-14`
- Method: `Supervised`

2. Select your training data
- Training data: `data/2024_euro_finetune.jsonl`

3. (Optionally) Select your validation data

4. Configure the advanced options:
- `batch_size`: The number of examples used to train a single forward/backward pass. (Leave as default value)
- `learning_rate_multiplier`: Larger rates tends to perform better with larger batch sizes. Smaller rates can be useful to avoid overfitting. (Leave as default value)
- `n_epochs`: The number of epochs to train the model for. An epoch refers to one full cycle through the training dataset. (Leave as default value)
- `seed`: Controls the reproducibility of the job. Same seed and job params should produce the same results most of the time, but still can differ in rare cases. Generated if not specified. (Leave as `Random`)

5. Other options:
- Model suffix: `ft-euro-2024`

## Fine-tuning result
- Training duration: `50m 38s`
- Training tokens: `8000`
- Training cost: `~$0.29`
- Performance: the model gives incorrect outputs about the 2024 Euro final (before training: answered with no information). 
- Default configuration for fine-tuning are:
    - Batch size: `1`
    - Learning rate multiplier: `2`
    - Epochs: `10`
    - Seed: `495432948`

## Notes

- Should be aware of the OpenAI model availability in regions before fine-tuning: https://learn.microsoft.com/en-us/azure/ai-foundry/concepts/fine-tuning-overview#fine-tuning-availability
- The cost to fine-tune is varied across different models and regions: https://azure.microsoft.com/en-us/pricing/details/cognitive-services/openai-service#pricing