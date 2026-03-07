from datetime import datetime
import os

message = f"Automated message generated on {datetime.now()}"

os.makedirs("datasets", exist_ok=True)

with open("datasets/messages.txt", "a") as f:
    f.write(message + "\n")

print(message)
