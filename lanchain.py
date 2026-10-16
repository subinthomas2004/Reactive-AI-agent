
from langchain.agents import create_agent
from langchain_ollama import ChatOllama

# 1. Create the LLM
llm = ChatOllama(
    model="tinyllama:latest",
    temperature=0
)

# 2. Create the agent
agent = create_agent(
    model=llm,
    system_prompt="""You are a reactive customer support agent.
    Respond directly to the user's message.
    If the user says hello, greet them.
    If they ask about Python, give a short answer.
    Keep responses simple."""
)

# 3. Get user input
user_input = input("You: ")

# 4. Invoke the agent
result = agent.invoke({
    "messages": [
        {"role": "user", "content": user_input}
    ]
})

##print(result)# 5. Print the response
print("Agent:", result["messages"][-1].content)
