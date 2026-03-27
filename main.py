import os

def run_command(cmd):
    return os.popen(cmd).read()

def ask_agent(user_input):
    user_input = user_input.lower()

    if "status" in user_input:
        return "git status"

    elif "add" in user_input:
        return "git add ."

    elif "commit" in user_input:
        return 'git commit -m "auto commit"'

    elif "push" in user_input:
        return "git push"

    elif "log" in user_input:
        return "git log --oneline"

    elif "branch" in user_input:
        return "git branch"

    else:
        return "echo 'Command not recognized'"


while True:
    user = input("\nYou: ")

    reply = ask_agent(user)

    print("\nAI suggests:\n", reply)

    confirm = input("\nExecute? (yes/no): ")

    if confirm.lower() == "yes":
        for cmd in reply.split("\n"):
            cmd = cmd.strip()
            if cmd:
                print(f"\nRunning: {cmd}")
                print(run_command(cmd))