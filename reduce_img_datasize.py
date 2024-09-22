from pathlib import Path
from PIL import Image

where_to_place_file_to_be_processed = "where_to_place_file_to_be_size-reduced"
where_to_save_processed_imgs = Path(__file__).parent / "reducing_datasize_processed"
for path in (Path(__file__).parent / "where_to_place_file_to_be_processed").iterdir():
    if path.is_file() and path.name.endswith((".jpg", ".png", ".JPG")):
        print(path.name)
        img = Image.open(path)
        if not where_to_save_processed_imgs.is_dir():
            where_to_save_processed_imgs.mkdir()
        img.save(
            where_to_save_processed_imgs / path.name,
            optimize=True,
            quality=22,
        )
input("Press Enter to exit.")
