from langchain_groq import ChatGroq
from langchain_experimental.agents import create_csv_agent


llm = ChatGroq(
    
)


def rag_qa(query):
    agent=create_csv_agent(llm,"output.csv",verbose=False,allow_dangerous_code=True)
    result=agent.run(query)
    return result