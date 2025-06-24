# Evaluation approaches

**Model benchmarks** are publicly available metric accross models and datasets, good for relative comparison between models:
- *Accuracy*: compares generated text with correct answer in the dataset.
- *Coherence*: measures the smoothness and human-likeness of the generated output.
- *Fluency*: assesses the grammatical rules, appropriate usage of vocabulary, structure of the output.
- *GPT similarity*: quantifies the semantic similarity between a ground truth sentence and the generated prediction sentence.

**Manual evaluations** provides insights in context relevance and user satisfaction. Evaluation criteria like relevance, informativeness, and engagement.

**AI-assisted metrics** includes:
- *Generation quality metrics*: evaluate the overall quality of the generated text on factors like creativity, coherence, and adherence.
- *Risk and safety metrics*: assess the potential risks and safety concerns, help ensure the model does not generate harmful or biased content.

**Natural language processing metrics**:
- *F1-score*: measures the ratio of the number of shared words between the generated and ground truth answers.
- *BLEU (Bilingual Evaluation Understudy metric)*: measures the difference between an automatic translation and human-created reference translations of the same source sentence. The algorithm relies on n-gram matches. Higher score indicates higher degree of similarity.
- *METEOR (Metric for Evaluation of Translation with Explicit Ordering)*: Measure the degree of matching between machine translation and human reference translation. The algorithm aligns words using stemming, synonyms and paraphrase matching. It is calculated based on the harmonic mean of precision and recall, with recall weighted more than precision. Higher score indicates higher degree of similarity.
- *ROUGE (Recall-Oriented Understudy for Gisting Evaluation)*: Is used to evaluate automatic summarization and machine translation. The algorithm emphasizes recall which measures how much of the reference content is captured in the generated output. Higher score indicates better quality in terms of content coverage.