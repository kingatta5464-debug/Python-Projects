import qrcode
from PIL import Image

qr = qrcode.QRCode(
    version=1, error_correction=qrcode.ERROR_CORRECT_H, box_size=10, border=4
)

qr.add_data("https://www.facebook.com/atta.ul.mustafa.729512")
qr.make(fit=True)

img = qr.make_image(fill_color="blue", back_color="white").convert("RGB")
# img.save("advance_FB_URL.png")

logo = Image.open("profile.jpg")
logo_size = 120
logo = logo.resize((logo_size, (logo_size + 60)))


pos = (img.size[0] - logo_size) // 2, (img.size[1] - (logo_size + 60)) // 2

img.paste(logo, pos)

img.save("QR_with_Profile.png")
