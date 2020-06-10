import pandas as pd
import socket
from simple_zpl2 import ZPLDocument, Code128_Barcode
from PIL import Image
import io



# Input alma
while True:
    readed_barcode_ = ""
    readed_barcode_ = input('Veri Gir')
    def veri():
        df = pd.read_excel(r'C:\Users\DELL\Desktop\barcode_test.xlsx')
        eski_barcode = df['eski'].tolist()
        yeni_barcode = df['yeni'].tolist()
        count=0
        #dictionary = dict(zip(eski_barcode, yeni_barcode))
        for eski in eski_barcode:
            if readed_barcode_ == str(eski):
                new_barcode_ = yeni_barcode[count]
                print(new_barcode_)

                zdoc = ZPLDocument()
                zdoc.add_comment(" TEX {}".format(new_barcode_))
                zdoc.add_field_origin(20, 20)
                zdoc.add_print_quantity(2)
                code128_data = str(new_barcode_)
                bc = Code128_Barcode(code128_data, 'N', 100, 'Y')
                zdoc.add_barcode(bc)
                print(zdoc.zpl_text)

                # Get PNG byte array
                png = zdoc.render_png(label_width=2, label_height=1)
                # render fake file from bytes
                fake_file = io.BytesIO(png)
                img = Image.open(fake_file)
                # Open image with the default image viewer on your system
                img.show()

                
            else:
                pass
            count += 1
        
    veri()
    if readed_barcode_ == "kapat":
        break
        
