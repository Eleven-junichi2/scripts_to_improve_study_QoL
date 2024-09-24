from pathlib import Path
from PIL import Image

path_input = Path(__file__).parent / "input"
path_output = Path(__file__).parent / "output"
for path in path_input.iterdir():
    if path.is_file() and path.name.endswith((".jpg", ".png", ".JPG")):
        print(path.name)
        img = Image.open(path)
        if not path_output.is_dir():
            path_output.mkdir()
        img.save(
            path_output / path.name,
            optimize=True,
            quality=16,
        )
input("Press Enter to exit.")
