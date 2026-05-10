import qrcode
from barcode.codex import Code128
from barcode.writer import ImageWriter
from PIL import Image
# from pyzbar.pyzbar import decode
from datetime import datetime

# Function to take student info
def take_student_info():
  student_id = input("Enter Student ID: ")
  name = input("Enter Your Name: ")
  return student_id, name

student_id, name = take_student_info()
print(f"Student ID: {student_id}, Name: {name}")

# Function to generate QR code
def generate_qr_code(student_id, name):
  data = f"Student ID: {student_id}, Name: {name}"
  qr = qrcode.QRCode(version=1, box_size=10, border=5)
  qr.add_data(data)
  qr.make(fit=True)
  qr_img = qr.make_image(fill='black', back_color='white')
  qr_img.save(f"{student_id}_qr.png")
  print(f"Successfully generated QR code and saved as {student_id}_qr.png")

# Function to generate barcode
def generate_barcode(student_id, name):
  data = f"Student ID: {student_id}, Name: {name}"
  barcode = Code128(data, writer=ImageWriter())
  barcode.save(f"{student_id}_barcode")
  print(f"Successfully generated barcode and saved as {student_id}_barcode.png")



if __name__ == "__main__":
  student_id, name = take_student_info()
  generate_qr_code(student_id, name)
  generate_barcode(student_id, name)