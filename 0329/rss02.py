from googletrans import Translator
import openpyxl

workbook = openpyxl.load_workbook('dailysecu.xlsx')
sheet = workbook.active

translator = Translator()

for row in sheet.iter_rows():   #엑셀 내 데이터가 있는 전체 열을 선택
    for cell in row:
        translated_text = translator.translate(cell.value, dest='en').text  #셀 내의 값을 번역해서 text로 저장
        cell.value = translated_text

workbook.save("translated_excel.xlsx")

