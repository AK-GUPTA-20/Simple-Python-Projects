import qrcode
from PIL import Image
import qrcode.constants          #  PIL is uswed to format 


qr = qrcode.QRCode(version = 1 ,
                   error_correction = qrcode.constants.ERROR_CORRECT_H,
                   box_size =50 , border = 20)

qr.add_data("https://www.linkedin.com/in/akshat-gupta-243460280?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")
qr.make(fit=True)
img = qr.make_image(fill_color = "blue" , back_color = 'yellow')
img.save("akshat_linkedinProfile.png")