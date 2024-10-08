import qrcode
from flask import Flask, render_template, send_file
import io

app = Flask(__name__)

# Route to render the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to generate and serve QR code image
@app.route('/qr_code')
def generate_qr_code():
    # Data to encode in QR code (e.g., URL)
    data = "https://yourwebsite.com"

    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    # Create an in-memory bytes buffer to hold the image
    img_io = io.BytesIO()
    img = qr.make_image(fill='black', back_color='white')
    img.save(img_io, 'PNG')
    img_io.seek(0)

    # Send the image to the client as a file response
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)