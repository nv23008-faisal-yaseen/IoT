#12AI Faisal
from pathlib import Path
DATA_FILE = Path("NV12345_W6_D1.txt")
try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        names = [n.strip() for n in f if n.strip()]
    print(names)
except:
    print("File not found.")
#12AI Faisal
