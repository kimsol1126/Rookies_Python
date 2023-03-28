from googletrans import Translator
import re

input_file = "input.txt"
output_file = "output.txt"

with open(input_file, "r", encoding="utf-8") as f:
    text = f.read()

#r"\1-*******" 은 첫번째 그룹은 그대로 두고, 이후는 * 으로 바꾸겠다는 뜻
text = re.sub(r"(\d{6})[-]\d{7}", r"\1-*******", text)

translator = Translator()
translated = translator.translate(text, dest='en').text

with open(output_file, "w", encoding="utf-8") as f:
    f.write(translated)

print(translated)