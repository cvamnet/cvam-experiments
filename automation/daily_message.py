from datetime import datetime
import os

now = datetime.now()

date_str = now.strftime("%Y-%m-%d")
time_str = now.strftime("%H:%M:%S")

message = (
    "==============================\n"
    f"Fecha: {date_str}\n"
    f"Hora: {time_str}\n"
    "Mensaje: Automated daily report generated successfully.\n"
    "==============================\n"
)

os.makedirs("datasets", exist_ok=True)

with open("datasets/messages.txt", "a", encoding="utf-8") as f:
    f.write(message)

print(message)
