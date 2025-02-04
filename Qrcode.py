import qrcode

def generate_qr_code(data, filename="qr_code.png"):
    
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    
    qr.add_data(data)
    qr.make(fit=True)

    
    img = qr.make_image(fill="black", back_color="white")

    
    img.save(filename)
    print(f"QR code saved as {filename}")


data = input("Enter text or URL to generate QR Code: ")
generate_qr_code(data)
