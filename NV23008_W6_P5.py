#12AI Faisal
DATA_FILE = "NV12345_W6_D1.txt"
name = input("Enter your name: ")
with open(DATA_FILE, "w", encoding="utf-8") as f:
    f.write(name + "\n")
print("Saved.")
#12AI Faisal
