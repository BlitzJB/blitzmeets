from flask import Flask, send_file, render_template
from io import BytesIO

from blitzmeets.client import MeetClient

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/qr_code')
def generate_qr_code():
    # Create a MeetClient object
    client = MeetClient()

    # Create a QR code and get its bytes
    qr_code_bytes = client.create_qr_code()

    # Create a BytesIO object and write the bytes to it
    img_buffer = BytesIO()
    img_buffer.write(qr_code_bytes)

    # Set the BytesIO object's cursor to the beginning
    img_buffer.seek(0)

    # Send the QR code image as a response
    return send_file(img_buffer, mimetype='image/png')


if __name__ == '__main__':
    app.run()