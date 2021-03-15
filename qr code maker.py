
# Import QRCode from pyqrcode 
import pyqrcode 
import png 
from pyqrcode import QRCode 
  
  
# String which represents the QR code 
s = r"Enter Your File name for qr code conversion"
  
# Generate QR code 
url = pyqrcode.create(s) 
  
# Create and save the svg file naming "myqr.svg" 
url.svg("123.svg", scale = 8) 
  
# Create and save the png file naming "myqr.png" 
url.png('123.png', scale = 6)