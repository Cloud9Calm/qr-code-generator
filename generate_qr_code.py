import qrcode

# Define your vCard information
vcard_data = """BEGIN:VCARD
VERSION:3.0
N:Cronie;Erin;;;
FN:Erin Cronie
ORG:Cloud9 Calm Co.
TITLE:Owner
TEL;TYPE=work,voice:3249823284
EMAIL:erin@cloud9calm.com
URL:https://cloud9calm.com
END:VCARD
"""

# Create QR code object
qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Add data to the QR code
qr.add_data(vcard_data)
qr.make(fit=True)

# Create the QR code image
img = qr.make_image(fill='black', back_color='white')

# Save the QR code image in the images folder
img.save("images/business_card_qr.png")

# Display the QR code image (optional)
img.show()