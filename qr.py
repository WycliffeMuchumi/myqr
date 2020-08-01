import pyqrcode
import png
from pyqrcode import QRCode

# String that represents the QR code
myString = "https://www.wycliffemuchumi.co.ke/"

# Generate QR code
url = pyqrcode.create(myString)

# Create and save the svg file naming "myqr.svg"
url.svg("myqr.svg", scale =8)

# create and save the png file naming "myqr.png"
url.png('myqr.png', scale=6)    