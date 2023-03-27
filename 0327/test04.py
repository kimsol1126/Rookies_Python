import googletrans

translator = googletrans.Translator()

input_text = input("한글을 입력하세요.")
translated = translator.translate(input_text, dest='en').text

print(f" 한글 입력 값: {input_text}")
print(f" 영어로 번역한 값: {translated}")