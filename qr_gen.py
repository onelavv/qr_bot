import qrcode

def gen(src):
    image = qrcode.make(src)
    image.save("qr.png")
    return "qr.png"
