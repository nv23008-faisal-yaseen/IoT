#12AI Faisal
from pathlib import Path
DATA_FILE = Path("NV12345_W6_D1.txt")
mode = "a" if DATA_FILE.exists() else "w"
with open(DATA_FILE, mode, encoding="utf-8") as f:
    name = input("Enter another name: ")
    f.write(name + "\n")
if mode == "a":
    print("Appended to file.")
else:
    print("Created new file.")
#12AI Faisal
