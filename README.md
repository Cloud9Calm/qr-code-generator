# QR Code Contact Information Generator

This project generates a QR code containing your contact information in the vCard format. The QR code can be scanned using a smartphone camera to quickly save your details, making it perfect for adding to business cards, email signatures, or other promotional materials.

## Features

- Generates a QR code containing your contact information in vCard format.
- Saves the QR code as an image file (`PNG`) which can be used on business cards or other materials.
- Automatically opens the QR code image for quick viewing and verification.

## Requirements

- Python 3.x
- `qrcode` library
- `Pillow` (PIL) library

## Installation

1. Clone this repository or download the files to your local machine.

   ```bash
   git clone <repository_url>
   cd qr-code-contact-generator


2. Copy the following code into generate_qr_code.py:
    ``bash
    import qrcode

    # vCard information for Erin Cronie
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

3. Run the script
    ```bash
    python3 generate_qr_code.py

4. The script will generate a QR code image (`business_card_qr.png`) in the `images` folder and display it automatically.

## Viewing and Verifying the QR Code

- The generated QR code can be viewed using any image viewer.
- To verify the content, scan the QR code using your smartphone’s camera or a QR scanner app. You should see an option to save the contact information directly to your phone.

## Customization

- **Colors**: Modify the `fill` and `back_color` parameters in `qr.make_image()` to change the QR code’s colors.
- **Size**: Adjust the `box_size` and `border` values in the `qrcode.QRCode()` function to change the QR code’s dimensions.
- **Error Correction**: You can change the error correction level (`qrcode.constants.ERROR_CORRECT_H`) for different levels of resilience to errors or partial damage.

## Troubleshooting

- If the QR code is not scanning correctly, double-check the vCard format for any errors or missing fields.
- Ensure the `qrcode` and `Pillow` libraries are correctly installed and up-to-date.

## Contributing

Feel free to contribute by suggesting improvements, reporting issues, or submitting pull requests.

## License

This project is open-source and available for personal and commercial use.