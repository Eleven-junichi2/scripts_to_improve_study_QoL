from pathlib import Path
import re

command = int(input("chart?(1: 1a, 2: 2b, 3: 3c)"))

if command == 1:
    chart_type = "1a"
elif command == 2:
    chart_type = "2b"
elif command == 3:
    chart_type = "3c"

answer_type = int(input("answer type?(1: chart & solution, 2: model answer)"))

filenames_may_contains_missing = []

match_question = re.compile(rf"chart{chart_type}-" + r"\d-(\d)+q$")

regex_str = rf"chart{chart_type}-" + r"\d-(\d)+a"
if answer_type == 1:
    regex_str += "-cs$"
elif answer_type == 2:
    regex_str += "-ma$"
match_answer = re.compile(regex_str)

question_img_filenames: list[Path] = []
answer_img_filenames: list[Path] = []
question_img_dirname = "questions"
answer_img_dirname = "answers"
for path in (Path(__file__).parent / question_img_dirname).iterdir():
    print(path.name)
    if match_question.match(path.stem):
        question_img_filenames.append(path.name)
question_img_filenames.sort()
for path in (Path(__file__).parent / answer_img_dirname).iterdir():
    print(path.name)
    if match_answer.match(path.stem):
        answer_img_filenames.append(path.name)
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
