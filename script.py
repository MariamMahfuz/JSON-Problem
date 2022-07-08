# -*- coding: UTF-8 -*-
# add use_unicode=True and charset="utf8"
import json
from googletrans import Translator
from fpdf import FPDF
# from pytz import unicode

translator = Translator()
#Fetching Json data
with open('json.json') as f:
    data = json.load(f)
    txt1=data["text"]
    bangla = translator.translate(txt1, dest='bn')
    hindi=translator.translate(txt1, dest='hi')
    chinese=translator.translate(txt1, dest='zh-cn')
    japanese=translator.translate(txt1, dest='ja')
    #encoding function
    # def lt(str):
    #     return unicode(str, 'utf-8').encode('iso-8859-1')

    #PDF Create and Printing Translation
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=16)
    # pdf.cell(50, 20, lt(bangla), 0, 2, 'L')
    pdf.cell(200, 10, txt=str(bangla),
             ln=2, align='C')
    pdf.cell(200, 10, txt=str(hindi),
                ln=2, align='C')
    pdf.cell(200, 10, txt=str(chinese),
                ln=2, align='C')
    pdf.cell(200, 10, txt=str(japanese),
                ln=2, align='C')
    pdf.output("output1.pdf")
    # print(bangla)
    # print(hindi)
    # print(chinese)
    # print(japanese)