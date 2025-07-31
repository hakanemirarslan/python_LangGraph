# LangGraph Project

This repository contains various graph-based AI applications and implementations using the LangGraph library. LangGraph is a powerful Python library designed for creating complex AI workflows and state machines, particularly useful for building agentic AI systems.

## 📁 Project Structure

```
python_LangGraph/
├── Agents/                    # Contains agent implementations
│   ├── Agent_Bot.py          # General purpose agent implementation
│   ├── Drafter.py            # Agent for drafting content
│   ├── Memory_Bot.py         # Agent with memory capabilities
│   ├── RAG_Agent.py          # Retrieval-Augmented Generation Agent
│   ├── ReAct.py              # ReAct (Reasoning and Acting) agent
│   ├── logging.txt           # Logging configuration
│   └── meeting.txt           # Meeting notes or agent meeting records
│
├── Exercises/                # Practice exercises for learning LangGraph
│   ├── Exercise1.ipynb       # Introduction to LangGraph basics
│   ├── Exercise2.ipynb       # Intermediate graph operations
│   ├── Exercise3.ipynb       # Advanced graph patterns
│   ├── Exercise4.ipynb       # Real-world use cases
│   └── Exercise5.ipynb       # Final project challenge
│
├── Graphs/                   # Example graph implementations
│   ├── Conditional_Graph.ipynb  # Graphs with conditional logic
│   ├── Hello_World.ipynb     # Basic introduction to LangGraph
│   ├── Looping_Graph.ipynb   # Graphs with loop structures
│   ├── Multiple_Inputs.ipynb # Handling multiple input graphs
│   └── Sequential_Graph.ipynb # Linear sequence graph examples
│
└── .env                      # Environment configuration
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Required Python packages (install via `pip install -r requirements.txt`):
  - `langgraph` - For creating graph-based AI workflows
  - `langchain-core` - Core components for LangChain
  - `langchain-google-genai` - Google Generative AI integration
  - `python-dotenv` - For environment variable management
  - `google-generativeai` - Google's Generative AI Python SDK

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/python_LangGraph.git
   cd python_LangGraph
   ```

2. Set up your environment:
   ```bash
   # Create and activate virtual environment (recommended)
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. Configure your environment:
   - Copy `.env.example` to `.env`
   - Add your API keys and configuration in the `.env` file

## 📚 Usage Examples

### Running the RAG Agent
```python
from Agents.RAG_Agent import RAGAgent

# Initialize the agent
agent = RAGAgent()

# Query the agent
response = agent.query("Your question here")
print(response)
```

### Exploring Examples
Navigate to the `Graphs/` directory to explore various LangGraph implementations.

## 🏗️ Project Structure Details

### 🤖 Agents
Contains ready-to-use AI agent implementations:

#### Example: RAG Agent (`Agents/RAG_Agent.py`)
A Retrieval-Augmented Generation agent that combines language models with external knowledge retrieval:

```python
# Example usage of RAG Agent
from Agents.RAG_Agent import RAGAgent

# Initialize with your knowledge base
rag_agent = RAGAgent(knowledge_base="my_knowledge_base")

# Get answers with citations
response = rag_agent.query("What is LangGraph?")
print(f"Answer: {response['answer']}")
print(f"Sources: {response['sources']}")
```

### 📝 Exercises
Structured learning materials to master LangGraph:

1. **Basic Exercises**
   - Creating simple graphs
   - Adding nodes and edges
   - Basic graph traversal

2. **Intermediate Challenges**
   - Conditional workflows
   - Parallel processing
   - Error handling in graphs

3. **Advanced Projects**
   - Multi-agent systems
   - Custom node implementations
   - Performance optimization

### 📊 Graphs
Example implementations demonstrating LangGraph capabilities:

#### 1. Basic Graph (`Graphs/basic_workflow.py`)
```python
# Simplified example of a basic graph
from langgraph.graph import Graph

def step_one():
    return "Processed step one"

def step_two(data):
    return f"Processed step two with: {data}"

# Create and run the graph
workflow = Graph()
workflow.add_node(step_one)
workflow.add_node(step_two)
workflow.add_edge(step_one, step_two)

result = workflow.run()
print(result)  # Output: "Processed step two with: Processed step one"
```

#### 2. Conditional Workflow (`Graphs/conditional_flow.py`)
Demonstrates branching logic based on node outputs.

#### 3. Parallel Processing (`Graphs/parallel_nodes.py`)
Shows how to execute multiple nodes in parallel and combine their results.

Each example includes detailed comments and can be run independently to see LangGraph in action.

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📬 Contact

For questions or suggestions, please [open an issue](https://github.com/yourusername/python_LangGraph/issues).
