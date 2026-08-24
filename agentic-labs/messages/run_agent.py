"""A simple agent demo"""

from strands import Agent

from agent_testing_utils import print_messages
from simple_tools import cosine, sine, divide

agent = Agent(
    tools=[cosine, sine, divide],
    model="us.anthropic.claude-sonnet-4-5-20250929-v1:0",
    system_prompt="You are a professional and friendly customer support agent. Be concise and helpful.",
)

# Start the conversation:
agent("What is the tangent of 1.5?")

# Call a tool directly:
agent.tool.divide(x=2, y=3.5)

print("-" * 30)

# Format and display the complete conversation:
print_messages(agent.messages)
