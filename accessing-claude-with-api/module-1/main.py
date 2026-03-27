import anthropic
import os
from dotenv import load_dotenv

load_dotenv()

client = anthropic.Anthropic(
    api_key=os.getenv("ANTHROPIC_API_KEY")
)

def load_skill():
    with open("skills/git-helper/SKILL.md", "r") as f:
        return f.read()

def run_command(cmd):
    return os.popen(cmd).read()

def ask_claude(user_input):
    skill = load_skill()

    prompt = f"""
You are an AI Git automation agent.

Skill:
{skill}

User request:
{user_input}

Return ONLY shell commands, one per line.
"""

    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=200,
        messages=[{"role": "user", "content": prompt}]
    )

    return response.content[0].text


while True:
    user = input("You: ")
    reply = ask_claude(user)

    print("\nAI suggests:\n", reply)

    confirm = input("\nExecute? (yes/no): ")

    if confirm.lower() == "yes":
        for cmd in reply.split("\n"):
            cmd = cmd.strip()
            if cmd:
                print(f"\nRunning: {cmd}")
                print(os.popen(cmd).read())