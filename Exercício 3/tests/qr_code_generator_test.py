from projects import qr_code_generator as qr_gen
from PIL import Image
from pyzbar.pyzbar import decode

test_string: str = "asuidbaisbasubdcicuasbcxawbduiabwd"

def test_create_qr_code() -> None:
    qr_gen.create_qr_code(test_string)

    generated_img: Image = Image.open("./artifacts/url_qrcode.png")
    
    data = decode(generated_img)

    decoded_string = data[0].data.decode("utf-8")

    assert decoded_string == test_string