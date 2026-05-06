from py_compile import main
import sys

from azure.identity import DefaultAzureCredential
from azure.ai.projects import AIProjectClient
from azure.core.credentials import AzureKeyCredential


endpoint = "https://foundry-1-learn-2.services.ai.azure.com/api/projects/proj-default"

project_client = AIProjectClient(
    endpoint=endpoint,
    credential=DefaultAzureCredential(),
)

my_agent = "CrystalHotelsAssistant-KnowledgeSystemImplementation"
my_version = "6"

openai_client = project_client.get_openai_client()


def main():
    messageNumber = 0
    while(1):
        messageNumber += 1
        message = input(f"({messageNumber}) Type your message and press Enter: ")
        

        # Get user input
        print(f"Received message: {message}")

        # Reference the agent to get a response
        response = openai_client.responses.create(
            input=[{"role": "user", "content": message}],
            extra_body={"agent_reference": {"name": my_agent, "version": my_version, "type": "agent_reference"}},
        )

        messageNumber += 1
        print(f"({messageNumber}) Response: {response.output_text}")

# TODO:
# Add local throttle to avoid hitting rate limits, specially if user want to spam messages.
# Add way to handle images.
# Fix the agent to actually not reask the user for the same information multiple times, specially if the user already provided it in the conversation, like guest amount.
main()