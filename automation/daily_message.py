from datetime import datetime

message = f"Automated message generated on {datetime.now()}"

with open("datasets/messages.txt", "a") as f:
    f.write(message + "\n")

print(message)
