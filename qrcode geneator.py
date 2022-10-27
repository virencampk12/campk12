import pyqrcode
import png
from pyqrcode import QRCode
qr = "www.google.co.in"
url = pyqrcode.create(qr)
url.svg("googleqr.svg", scale = 8)
url.png("googleqr.png", scale = 6)