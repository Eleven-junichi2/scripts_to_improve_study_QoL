from pathlib import Path
import tomllib
import re

with open(Path(__file__).parent / "qimg_to_aimg_regex.toml", "rb") as f:
    qimg_to_aimg_patterns = tomllib.load(f)

commands = tuple(qimg_to_aimg_patterns.keys())

while True:
    try:
        command = int(
            input(
                f"which pattern will you use?: {" ".join([f'({i}:{cmd})' for i, cmd in enumerate(commands)])}>"
            )
        )
    except ValueError:
        print("Invalid input. Please enter a number.")
    else:
        break
print(f"command: {commands[command]}")

prefix_regex_pattern = r"\.|jpg|JPG|png|"
match_question = re.compile(
    qimg_to_aimg_patterns[commands[command]]["q"] + prefix_regex_pattern
)
match_answer = re.compile(
    qimg_to_aimg_patterns[commands[command]]["a"] + prefix_regex_pattern
)
print("regex pattern: for answer:", match_question.pattern)
print("regex pattern for question:", match_answer.pattern)

question_img_filenames: list[Path] = []
answer_img_filenames: list[Path] = []
question_img_dirname = "questions"
answer_img_dirname = "answers"

for path in (Path(__file__).parent / question_img_dirname).iterdir():
    print(path.name, end=" ")
    if match_question.match(path.stem):
        question_img_filenames.append(path.name)
        print("match!")
    else:
        print("")
question_img_filenames.sort()

for path in (Path(__file__).parent / answer_img_dirname).iterdir():
    print(path.name, end=" ")
    if match_answer.match(path.stem):
        answer_img_filenames.append(path.name)
        print("match!")
    else:
        print("")
answer_img_filenames.sort()

exported_as_anki_deck = "#separator:tab\n"
exported_as_anki_deck += "#html:true\n"
exported_as_anki_deck += "#notetype column:1\n"
for question_img_filename, answer_img_filename in zip(
    question_img_filenames, answer_img_filenames
):
    exported_as_anki_deck += "基本"
    exported_as_anki_deck += "\t"
    exported_as_anki_deck += f'<img src="{question_img_filename}">'
    exported_as_anki_deck += "\t"
    exported_as_anki_deck += f'<img src="{answer_img_filename}">'
    exported_as_anki_deck += "\n"
with open(
    Path(__file__).parent / "exported_as_anki_deck.txt", "w", encoding="utf-8"
) as f:
    f.write(exported_as_anki_deck)
print("Export .txt as Anki deck file:")
print(exported_as_anki_deck)
input("Press Enter to exit.")
