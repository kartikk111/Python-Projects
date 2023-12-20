import qrcode 

def gen_qrcode(text):

    qr = qrcode.QRCode(version = 1, error_correction = qrcode.constants.ERROR_CORRECT_L, box_size = 10, border = 4)

    qr.add_data(text)
    qr.make(fit = True)
    img = qr.make_image(fill_color = "black", back_color = "white")
    img.save("qrcodeimg.png")

website_name = input("Enter the website to generate QR Code for: ")


gen_qrcode(website_name)