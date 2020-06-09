import socket
from simple_zpl2 import ZPLDocument, Code128_Barcode

# Each label is built with a ZPLDocument object
zdoc = ZPLDocument()
zdoc.add_comment(" TEX 7332262815348")
zdoc.add_field_origin(20, 20)
code128_data = '7332262815348'
bc = Code128_Barcode(code128_data, 'N', 30, 'Y')
zdoc.add_barcode(bc)

print(zdoc.zpl_text)


#Connection
mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = "10.80.209.106"
port = 9100
try:
	mysocket.connect((host, port))  # connecting to host
	#mysocket.send(b"zdoc.zpl_text")  # using bytes
	mysocket.send(zdoc.zpl_bytes)  # using bytes
	mysocket.close()  # closing connection
except:
	print("Error with the connection")
