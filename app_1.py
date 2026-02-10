from pathlib import Path
import boto3
import json

# Bedrock client
client = boto3.client(
    "bedrock-runtime",
    region_name="us-east-1"
)

# Local file read
def file_read(path):
    return Path(path).read_text(encoding="utf-8")

# AI Agent function
def agent(prompt):
    print("Agent received task:")
    print(prompt)
    print("-" * 40)

    if "chapter10.txt" in prompt:
        content = file_read("docs/chapter10.txt")

        # Send content to Claude via Bedrock
        body = {
            "anthropic_version": "bedrock-2023-05-31",
            "max_tokens": 300,
            "messages": [
                {
                    "role": "user",
                    "content": f"Read the following content and explain it simply:\n\n{content}"
                }
            ]
        }

        response = client.invoke_model(
            modelId="anthropic.claude-3-5-sonnet-2024-v1",
            body=json.dumps(body)
        )

        result = json.loads(response["body"].read())
        return result["content"][0]["text"]

    return "I don't understand the task."

# Run agent
response = agent(
    "What is the content of the file 'chapter10.txt' located in the 'docs' directory?"
)

print("\nAI Response:\n")
print(response)
