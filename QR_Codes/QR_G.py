import qrcode
import os

#link path:
data = "https://www.example.com"  

#your saved path:
save_path = r"D:\College\Codes\VS\Side_Projects\PY\QR_Codes"


if not os.path.exists(save_path):
    os.makedirs(save_path)

#QR code name to be saved by:
file_name = "my_qr_code.png"
full_path = os.path.join(save_path, file_name)


qr = qrcode.QRCode(
    version=1,  
    error_correction=qrcode.constants.ERROR_CORRECT_L,  
    box_size=10,  
    border=4,  
)

qr.add_data(data)
qr.make(fit=True)

img = qr.make_image(fill_color="#6aff9b", back_color="black")
img.save(full_path)
print(f"QR code has been generated and saved at '{full_path}'.")
