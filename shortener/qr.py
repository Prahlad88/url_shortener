import qrcode
from io import BytesIO
import base64

def generate_qr_code(url):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )

    qr.add_data(url)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Convert the image to bytes
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    image_data = buffered.getvalue()

    # Encode the image data to base64
    img_base64 = base64.b64encode(image_data).decode('utf-8')

    return img_base64