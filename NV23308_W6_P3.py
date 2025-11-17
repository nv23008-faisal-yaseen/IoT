#12AI Faisal
import os
file = "NV12345_W6_D1.txt"
if os.path.exists(file):
    f = open(file, "a")
    print("File found.")
else:
    f = open(file, "w")
    print("File created.")
name = input("Enter another name: ")
f.write("\n" + name)
f.close()
print("Done.")
#12AI Faisal
