# LLM app development lifecycle
1. Initialization: Define objective -> collect sample dataset -> make basic prompt -> design the basic flow.
2. Experimentation: Develop and test the flow against the small sample dataset.
3. Evaluation and refinement: Assess the flow on a larger dataset.
4. Production: Deploy and monitor the flow and application. Optimize for efficiency and affectiveness.

Developer can continuously iterate between step 2-3-4.

# Flow concepts, components, and types
A flow consists of **inputs**, **nodes**, and **outputs**.

Data passed into the flow (inputs), processed with operations (by the nodes or tools), and returned in the final form (outputs).

Common **tools** available in prompt flow are:
- LLM tool: utilize LLM to create custom prompts.
- Python tool: execute Python script.
- Prompt tool: prepare prompts as strings for complex scenarios or integration with other tools.

Types of flows:
- Standard flow: ideal for general LLM-based application with versatile (flexible) tools.
- Chat flow: ideal for converasational apps.
- Evaluation flow: ideal for performance evaluation, models/apps analysis and improvement through feedback.

**Variants** are settings for a node, currently available only in the LLM tool (different prompt or connection string). Good for quickly switching between settings for experimenting, or side-by-side result comparisons.

Flow can be deployed to an **online endpoint**, and can be called from any application.

To monitor and evaluate the performance of LLMs, these **metrics** can be used:
- *Groundessness*: measures the alignment of the output with the input source or database (the grounding data).
- *Relevance*: measures the output with the given input (prompt).
- *Coherence*: evaluates the logical flow and readability of the output.
- *Fluency*: assesses the grammatical and linguistic accuracy of the output.
- *Similarity*: measures the contextual/semantic match between the output and the ground truth.


