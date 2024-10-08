import os
import qrcode
from flask import Flask, render_template, send_file, jsonify, request
import io
import uuid
from access_keys import keys

app = Flask(__name__)

# Simulated storage for valid codes
valid_codes = list(keys)

def get_mac_address():
    # Get the MAC address of the device
    mac = ':'.join(['{:02x}'.format((uuid.getnode() >> elements) & 0xff) for elements in range(0, 2 * 6, 2)][::-1])
    return mac

# Route to render the home page
@app.route('/')
def home():
    return render_template('index.html')

# Route to generate and serve QR code image
@app.route('/qr_code')
def generate_qr_code():
    # Get the MAC address to encode in the QR code
    data = get_mac_address()

    # Generate the QR code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(data)
    qr.make(fit=True)

    # Create a buffer to hold the image
    img_io = io.BytesIO()
    img = qr.make_image(fill='black', back_color='white')
    img.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png')

# Route to handle code verification
@app.route('/verify_code', methods=['POST'])
def verify_code():
    try:
        data = request.json
        if not data or 'code' not in data:
            return jsonify({'status': 'error', 'message': 'No code provided'}), 400
        
        entered_code = data['code']

        if entered_code in valid_codes:
            return jsonify({'status': 'authenticated'})
        else:
            return jsonify({'status': 'failed'}), 403
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
