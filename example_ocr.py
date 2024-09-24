from pathlib import Path

import easyocr
reader = easyocr.Reader(["ja",], gpu=False)
result = reader.readtext(str(Path(__file__).parent / "DSC_0982.jpg"), detail=0)
for result in result:
    print(result)
