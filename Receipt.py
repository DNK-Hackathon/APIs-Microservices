import jinja2
import pdfkit
#import pandas as pd



INPUT_NAME = input()
INPUT_PHONENUMBER = input()
INPUT_COUNTRY = input()
INPUT_ADDRESS = input()
INPUT_RNAME = input()
INPUT_RPHONENUMBER =input()
INPUT_RCOUNTRY = input()
INPUT_RADDRESS = input()
INP_PT = input()
INP_AN = input()
INP_INS = input()
INP_VALUE = input()
INP_WT = input()
INP_QUANTITY = input()

context = {'INPUT_NAME': INPUT_NAME, 'INPUT_PHONENUMBER': INPUT_PHONENUMBER, 'INPUT_COUNTRY': INPUT_COUNTRY,'INPUT_ADDRESS': INPUT_ADDRESS,'INPUT_RNAME':INPUT_RNAME,'INPUT_RPHONENUMBER':INPUT_RPHONENUMBER,'INPUT_RCOUNTRY':INPUT_RCOUNTRY,'INPUT_RADDRESS':INPUT_RADDRESS,'INP_PT':INP_PT,'INP_AN':INP_AN,'INP_INS':INP_INS,'INP_VALUE':INP_VALUE,'INP_WT':INP_WT,'INP_QUANTITY':INP_QUANTITY}


template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

template = template_env.get_template("template.html")
output_text = template.render(context)
print(output_text)


