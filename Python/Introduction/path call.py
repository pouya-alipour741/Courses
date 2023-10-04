from pathlib import Path

path = Path(r'C:\Users\pouya\Desktop\python')
print(path.exists())
for file in path.glob("*.xlsx"):
    print(file)

for file in path.glob("*.mp3"):
    print(file)

