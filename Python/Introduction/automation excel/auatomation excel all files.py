from pathlib import Path
import automation as a

path = Path()
for file in path.glob("*.xlsx"):
    a.process_workbook(file)

