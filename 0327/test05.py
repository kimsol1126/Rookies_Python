import googletrans
import csv

translator = googletrans.Translator()

with open("example.csv", encoding = "UTF-8") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        a, b, c = row
        a1 = translator.translate(a, dest='en').text
        b1 = translator.translate(b, dest='en').text
        c1 = translator.translate(c, dest='en').text
        print(f"과목: {a1}, 수업: {b1}, 내용: {c1}")