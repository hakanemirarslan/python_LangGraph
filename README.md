# LangGraph Project

A comprehensive collection of LangGraph implementations, AI agents, and learning exercises demonstrating graph-based AI workflows and state machines.

## 📁 Project Structure

```
python_LangGraph/
├── Agents/                    # AI Agent Implementations
│   ├── Agent_Bot.py          # Simple conversational agent with basic chat functionality
│   ├── Drafter.py            # Document drafting agent with save/update capabilities
│   ├── Memory_Bot.py         # Conversational agent with conversation memory and logging
│   ├── RAG_Agent.py          # Retrieval-Augmented Generation agent with PDF knowledge base
│   ├── ReAct.py              # ReAct (Reasoning and Acting) agent with mathematical tools
│   ├── chroma.sqlite3        # Vector database for RAG agent
│   ├── logging.txt           # Conversation logs from Memory_Bot
│   ├── meeting.txt           # Meeting records
│   └── Stock_Market_Performance_2024.pdf  # Knowledge base for RAG agent
│
├── Exercises/                # Learning Exercises (Jupyter Notebooks)
│   ├── Exercise1.ipynb       # Basic personalized agent with motivation node
│   ├── Exercise2.ipynb       # Intermediate graph operations
│   ├── Exercise3.ipynb       # Advanced graph patterns
│   ├── Exercise4.ipynb       # Real-world use cases
│   └── Exercise5.ipynb       # Final project challenge
│
├── Graphs/                   # Example Graph Implementations
│   ├── Hello_World.ipynb     # Basic introduction to LangGraph with greeting node
│   ├── Sequential_Graph.ipynb # Linear sequence graph examples
│   ├── Conditional_Graph.ipynb # Graphs with conditional logic and branching
│   ├── Looping_Graph.ipynb   # Graphs with loop structures and iteration
│   └── Multiple_Inputs.ipynb # Handling multiple input graphs and parallel processing
│
├── requirements.txt          # Python dependencies
└── README.md               # This file
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- Google Generative AI API key (for Gemini models)

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/python_LangGraph.git
   cd python_LangGraph
   ```

2. **Set up your environment:**
   ```bash
   # Create and activate virtual environment (recommended)
   python -m venv venv
   source venv/bin/activate  # On Windows: .\venv\Scripts\activate
   
   # Install dependencies
   pip install -r requirements.txt
   ```

3. **Configure your environment:**
   - Create a `.env` file in the root directory
   - Add your Google API key: `GOOGLE_API_KEY=your_api_key_here`

## 🤖 AI Agents

### 1. Agent_Bot.py - Simple Conversational Agent
A basic chat agent that processes user input and responds using Gemini 1.5 Flash.

```python
# Run the agent
python Agents/Agent_Bot.py
```

**Features:**
- Simple conversation flow
- Direct user input processing
- Clean exit with "exit" command

### 2. Memory_Bot.py - Conversational Agent with Memory
An enhanced chat agent that maintains conversation history and logs interactions.

```python
# Run the agent
python Agents/Memory_Bot.py
```

**Features:**
- Conversation memory across sessions
- Automatic logging to `logging.txt`
- Persistent conversation history

### 3. Drafter.py - Document Drafting Agent
A specialized agent for document creation, editing, and saving.

```python
# Run the agent
python Agents/Drafter.py
```

**Features:**
- Document content management
- Save documents to text files
- Real-time document updates
- Tool-based operations (update, save)

### 4. RAG_Agent.py - Retrieval-Augmented Generation Agent
A sophisticated agent that combines language models with external knowledge retrieval from PDF documents.

```python
# Run the agent
python Agents/RAG_Agent.py
```

**Features:**
- PDF document processing (Stock Market Performance 2024)
- Vector database (ChromaDB) for document storage
- Semantic search and retrieval
- Tool-based information extraction
- Knowledge base integration

### 5. ReAct.py - ReAct (Reasoning and Acting) Agent
An agent that demonstrates reasoning and tool usage for mathematical operations.

```python
# Run the agent
python Agents/ReAct.py
```

**Features:**
- Mathematical tools (add, subtract, multiply)
- Tool calling and reasoning
- Stream processing
- Multi-step problem solving

## 📚 Learning Materials

### Exercises
Structured learning materials to master LangGraph concepts:

1. **Exercise1.ipynb** - Basic personalized agent with motivation node
2. **Exercise2.ipynb** - Intermediate graph operations
3. **Exercise3.ipynb** - Advanced graph patterns
4. **Exercise4.ipynb** - Real-world use cases
5. **Exercise5.ipynb** - Final project challenge

### Graph Examples
Practical implementations demonstrating LangGraph capabilities:

1. **Hello_World.ipynb** - Basic introduction with greeting node
2. **Sequential_Graph.ipynb** - Linear sequence workflows
3. **Conditional_Graph.ipynb** - Conditional logic and branching
4. **Looping_Graph.ipynb** - Loop structures and iteration
5. **Multiple_Inputs.ipynb** - Multiple input handling and parallel processing

## 🔧 Dependencies

The project uses the following key dependencies:

- `langgraph` - Core graph-based AI workflow library
- `langchain-core` - Core LangChain components
- `langchain-google-genai` - Google Generative AI integration
- `langchain-community` - Community integrations
- `python-dotenv` - Environment variable management
- `google-generativeai` - Google's Generative AI Python SDK
- `jupyter` - Jupyter notebook support
- `chromadb` - Vector database for RAG functionality

## 📖 Usage Examples

### Running a Simple Agent
```python
from Agents.Agent_Bot import agent
from langchain_core.messages import HumanMessage

# Start a conversation
result = agent.invoke({"messages": [HumanMessage(content="Hello!")]})
```

### Using the RAG Agent
```python
from Agents.RAG_Agent import running_agent

# Initialize and run the RAG agent
running_agent()
```

### Working with Graphs
```python
from langgraph.graph import StateGraph
from typing import TypedDict

# Define your state
class MyState(TypedDict):
    message: str

# Create a simple graph
def greeting_node(state: MyState) -> MyState:
    state['message'] = f"Hello, {state['message']}!"
    return state

graph = StateGraph(MyState)
graph.add_node("greeting", greeting_node)
graph.set_entry_point("greeting")
graph.set_finish_point("greeting")

app = graph.compile()
result = app.invoke({"message": "World"})
```

## 🎯 Key Features

- **Multiple Agent Types**: From simple chat bots to complex RAG systems
- **Tool Integration**: Mathematical operations, document processing, and more
- **Memory Management**: Conversation history and persistent state
- **Vector Database**: ChromaDB integration for document retrieval
- **Learning Materials**: Structured exercises and examples
- **Jupyter Notebooks**: Interactive learning and experimentation

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

---

**Note**: Make sure to set up your Google API key in the `.env` file before running any of the agents that use Gemini models.
