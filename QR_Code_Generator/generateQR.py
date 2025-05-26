import qrcode as qr

img = qr.make("https://www.linkedin.com/in/akshat-gupta-243460280?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app")
img.save("Akshat_linkedin.png")
