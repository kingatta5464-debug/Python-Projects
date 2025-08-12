import qrcode

data = "https://www.facebook.com/atta.ul.mustafa.729512"
qr = qrcode.make(data)
qr.save("message.png")
