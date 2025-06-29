# Azure AI Services Lab & AZ-102 Study

This repository is a personal lab for experimenting with **Azure AI Services** and preparing for the **AZ-102 Azure AI Engineer Associate** exam.

## AZ-102 Focus Areas (Skills measured as of April 30, 2025)

### Plan and manage an Azure AI solution (20–25%)

### Implement generative AI solutions (15–20%)

- **Responsible AI** ([genai_responsible_ai.md](genai_responsible_ai.md)): Identify, mitigate and manage potential harms.
- **Prompt flow** ([genai_prompt_flow.md](genai_prompt_flow.md)): Basic flow concepts, types and components. LLM evaluation metrics (Groundessness, Relevance, Coherence, Fluency, Similarity).
- **Working with Multimodal Models** ([genai_multimodal_models.ipynb](genai_multimodal_models.ipynb)): Prompting with audio and image files.
- **Image generation** ([genai_image_generation.ipynb](genai_image_generation.ipynb)): Generate image using DALL-E 3.
- **RAG with AI Search** ([genai_rag_with_ai_search.ipynb](genai_rag_with_ai_search.ipynb)): Key-word search, Vector search.
- **Fine-tune AI models** ([genai_model_fine_tuning.md](genai_model_fine_tuning.md)): Fine-tune AI model on Azure AI Foundry.
- **Model performance Evaluation** ([genai_model_performance_evaluation.md](genai_model_performance_evaluation.md)): Model benchmarks, Manual & AI-assisted evaluation, NLP metrics (F1-score, BLEU, METEOR, ROUGE).

### Implement an agentic solution (5–10%)

### Implement computer vision solutions (10–15%)

- **AI Vision** ([ai_vision.ipynb](ai_vision.ipynb)): 
    - Image analysis (Caption, Dense caption, Tags, Objects, People, Smart crops, Read text).
    - Face analysis (Head pose, Occlusion, Accessories, Glasses, Exposure...).

### Implement natural language processing solutions (15–20%)

- **AI Language** ([ai_language.ipynb](ai_language.ipynb)): Language detection, Sentiment analysis, Key phrase extraction, Entity recognition, Linked entities extraction, PII recognition, Summarization.
- **AI Translator** ([ai_translator.ipynb](ai_translator.ipynb)): Translation, Transliteration.

### Implement knowledge mining and information extraction solutions (15–20%)
- **Content Understanding** ([genai_content_understanding.ipynb](genai_content_understanding.ipynb)): Document (invoice) analysis, Audio analysis, Create a custom analyzer.
- **AI Search** ([ai_search.ipynb](ai_search.ipynb)): Querying an index.


## ⚠️ Disclaimer

At the time of this writing, Azure is continuously updating its AI concepts and services to keep up with the rapidly evolving AI landscape. As a result, some SDK packages, APIs, or functions may not work as expected or could be deprecated without notice. 

This repository is intended for learning and experimentation—please validate official documentation when building production-grade solutions.
