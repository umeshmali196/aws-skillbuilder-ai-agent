from strands import Agent, tool
from strands_tools import calculator, current_time, python_repl

# Define a custom tool
@tool
def letter_counter(word: str, letter: str) -> int:
    """
    Count occurrences of a specific letter in a word.
    """

    if not isinstance(word, str) or not isinstance(letter, str):
        return 0

    if len(letter) != 1:
        raise ValueError("The 'letter' parameter must be a single character")

    return word.lower().count(letter.lower())


# Create an agent with tools
agent = Agent(
    tools=[
        calculator,
        current_time,
        python_repl,
        letter_counter
    ]
)

# Ask a question to the agent
message = """
Tell me how many letter R's are in the word "strawberry"
"""

agent(message)
