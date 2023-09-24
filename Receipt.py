import jinja2
import pdfkit
#import pandas as pd



INPUT_NAME = "kush"
INPUT_PHONENUMBER = "9305407007"
INPUT_COUNTRY = "INDIA"
INPUT_ADDRESS = "ajjabdjbjds"
INPUT_RNAME = "ABHI"
INPUT_RPHONENUMBER ="86757789968"
INPUT_RCOUNTRY = "SPAIN"
INPUT_RADDRESS = "hshdksfk"
INP_PT = "A"
INP_AN = "PEN"
INP_INS = "YES"
INP_VALUE = "2000"
INP_WT = "400"
INP_QUANTITY = "2"

context = {'INPUT_NAME': INPUT_NAME, 'INPUT_PHONENUMBER': INPUT_PHONENUMBER, 'INPUT_COUNTRY': INPUT_COUNTRY,'INPUT_ADDRESS': INPUT_ADDRESS,'INPUT_RNAME':INPUT_RNAME,'INPUT_RPHONENUMBER':INPUT_RPHONENUMBER,'INPUT_RCOUNTRY':INPUT_RCOUNTRY,'INPUT_RADDRESS':INPUT_RADDRESS,'INP_PT':INP_PT,'INP_AN':INP_AN,'INP_INS':INP_INS,'INP_VALUE':INP_VALUE,'INP_WT':INP_WT,'INP_QUANTITY':INP_QUANTITY}


template_loader = jinja2.FileSystemLoader('./')
template_env = jinja2.Environment(loader=template_loader)

template = template_env.get_template("template.html")
output_text = template.render(context)
print(output_text)
#config = pdfkit.configuration(wkhtmltopdf='C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe')
#pdfkit.from_string(output_text, 'receipt.pdf', configuration=config)


