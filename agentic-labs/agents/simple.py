"""A simple agent demo"""

import math
from strands import Agent, tool

@tool
def cosine(x: float) -> float:
    return math.cos(x)

@tool
def sine(x: float) -> float:
    return math.sin(x)

@tool(description="Divide x by y")
def divide(x: float, y: float) -> float:
    return x / y

@tool
def square_root(x: float) -> float:
    return math.sqrt(x)

agent = Agent(tools=[cosine, sine, divide, square_root], model="us.anthropic.claude-sonnet-4-5-20250929-v1:0")

agent("What is the square root of the cosine of 1.0?")
