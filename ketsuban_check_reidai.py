from pathlib import Path
import re

filenames_may_contains_missing = []
regex = re.compile(r"(\d)+")
for path in (Path(__file__).parent / "where_to_place_file_to_be_processed").iterdir():
    if regex.match(path.stem):
        print(path.name)
        filenames_may_contains_missing.append(int(path.stem))
filenames_may_contains_missing.sort()
print(filenames_may_contains_missing)

prev_id = 0
for id in filenames_may_contains_missing:
    gap = id - prev_id
    prev_id = id
    if gap > 1:
        print(f"Missing files detected from {id - gap} to {id} in the exclusive range.")

input("Press Enter to exit.")
