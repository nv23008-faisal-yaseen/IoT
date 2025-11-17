#12AI Faisal
DATA_FILE = "NV12345_W6_D1.txt"
try:
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        name = f.read().strip()
    print("Hello", name, "welcome to file handling in Python.")
except:
    print("File not found.")
#12AI Faisal
