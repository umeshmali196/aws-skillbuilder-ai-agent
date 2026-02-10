from strands import Agent
from strands.models import BedrockModel
from strands_tools import file_read, file_write

# Step 1: Define the model
model = BedrockModel(
    model_id="anthropic.claude-3-5-sonnet-2024-v1"
)

# Step 2: System prompt
system_prompt = """
You are a helpful personal assistant capable of performing local file actions.

Your key capabilities:
1. Read and summarize files.
2. Create and write files.

Use tools only when required.
"""

# Step 3: Create agent
agent = Agent(
    model=model,
    system_prompt=system_prompt,
    tools=[file_read, file_write],
)

# Step 4: Run the agent
response = agent(
    "What is the content of the file 'chapter10.txt' located in the 'docs' directory?"
)

print(response)
