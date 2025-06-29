# What are AI agents?

AI agents are smart software services that combine *generative AI models* with *contextual data* and *the ability to automate tasks* based on **user input** and environmental factors that they perceive.

# Agent development on Azure platform
Azure provides frameworks/SDK to develop agents:
- **Azure AI Foundry Agent Service**: framework for creating, managing and using AI agents within Azure AI Foundry. Also supports both OpenAI SDK and Azure Foundry SDK.
- **OpenAI Assistants API**: provides a subset of the features in Foundry Agent Service, and can only be used with OpenAI models.
- **Semantic Kernel**: lightweight, open-source development kit that you can use to build AI agents and **orchestrate** multi-agent solutions. *Semantic Kernel Agent Framework* is a platform specifically optimized for creating agents and implementing agentic solution patterns.
- **AutoGen**: open-source framework for developing agents rapidly. Useful as a research and ideation tool when experimenting with agents.
- **Microsoft 365 Agents SDK**: Developers can create self-hosted agents for delivery through a wide range of channels by using the Microsoft 365 Agents SDK. Not limited to Microsoft 365, but can be delivered through channels like Slack or Messenger.
- **Microsoft Copilot Studio**: provides a *low-code development environment* that "citizen developers" can use to quickly build and deploy agents that integrate with a Microsoft 365 ecosystem or commonly used channels like Slack and Messenger.
- **Copilot Studio agent builder in Microsoft 365 Copilot**: Business users can use the declarative Copilot Studio agent builder tool in Microsoft 365 Copilot to author basic agents for common tasks.

# Components of an agent:
- Model: generative AI model that enables the agent to reason and generate natural language responses to prompts.
- Knowledge: data sources that enable the agent to ground prompts with contextual data. Can be Microsoft Bing, an Azure AI Search index, or your own data and documents.
- Tools: Programmatic functions that enable the agent to automate actions. Can be built-in tools to access Azure AI Search and Bing, or code interpreter tool to run Python code and Azure Functions.

Conversations between users and agents take place on a thread, which retains a history of the messages exchanged in the conversation as well as any data assets, such as files, that are generated.


# Examples of AI agent use cases

- **Personal productivity agents**: assist individuals with daily tasks such as scheduling meetings, sending emails, and managing to-do lists.
- **Research agents**: continuously monitor market trends, gather data, and generate reports.
- **Sales agents**: automate lead generation and qualification processes. They can research potential leads, send personalized follow-up messages, and even schedule sales calls.
- **Customer service agents**: handle routine inquiries, provide information, and resolve common issues. They can be integrated into chatbots on websites or messaging platforms, offering instant support to customers.
- **Developer agents**: help in software development tasks such as code review, bug fixing, and repository management. They can automatically update codebases, suggest improvements, and ensure that coding standards are maintained.


# Foundry Agent Service resources
Foundry Agent Service is fully managed and designed to help developers build agents without having to worry about underlying resources.

- **Basic agent setup**: A minimal configuration that includes `Azure AI hub <-> Azure AI project <-> Azure AI Services` resources.
- **Standard agent setup**: A more comprehensive configuration that includes the *basic agent setup* plus `Azure Key Vault, Azure AI Search, and Azure Storage`.

## Knowledge tools
Available tools include:

- **Bing Search**: Uses Bing search results to ground prompts with real-time live data from the web.
- **File search**: Grounds prompts with data from files in a vector store.
- **Azure AI Search**: Grounds prompts with data from Azure AI Search query results.
- **Microsoft Fabric**: Uses the Fabric Data Agent to ground prompts with data from your Fabric data stores.

## Action tools
Available tools include:

- **Code Interpreter**: A sandbox for model-generated Python code that can access and process uploaded files.
- **Custom function**: Call your custom function code – you must provide function definitions and implementations.
- **Azure Function**: Call code in serverless Azure Functions.
- **OpenAPI Spec**: Call external APIs based on the OpenAPI 3.0 spec.