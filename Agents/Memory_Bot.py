import os
from typing import TypedDict, List, Union #Union is a type specifier from Python's typing module that allows multiple data types.
from langchain_core.messages import HumanMessage, AIMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, START, END
from dotenv import load_dotenv

load_dotenv()

class AgentState(TypedDict):
    messages: List[Union[HumanMessage, AIMessage]]


llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

def process(state: AgentState)->AgentState:
    """This node will solve the request you input"""
    response=llm.invoke(state["messages"])

    #The append method is used to add a single element to the end of a list, that is, to expand the list's contents.
    state["messages"].append(AIMessage(content=response.content))
    print(f"\nAI: {response.content}")
    
    return state

graph = StateGraph(AgentState)
graph.add_node("process", process)
graph.add_edge(START, "process")
graph.add_edge("process", END)
agent = graph.compile()
    

conversation_history=[]

user_input=input("Enter: ")
while user_input != "exit":
    conversation_history.append(HumanMessage(content=user_input))
    result= agent.invoke({"messages": conversation_history}) #All conversation history is here
    conversation_history = result["messages"]
    user_input = input("Enter: ")


with open("logging.txt","w") as file:
    file.write("Your Conversation Log:\n")
    for message in conversation_history:
        if isinstance(message, HumanMessage):
            file.write(f"You: {message.content}\n")
        elif isinstance(message,AIMessage):
            file.write(f"AI: {message.content}\n\n")
    file.write("End of Conversation")

print("Conversation saved to logging.txt")