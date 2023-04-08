# Import required libraries
import os
from PIL import Image
from blitzmeets.client import MeetClient

# Create a MeetClient object
client = MeetClient()

# Create a QR code and get its bytes
qr_code_bytes = client.create_qr_code()

# Save the QR code bytes to a file
filename = "meeting_qr_code.png"
with open(filename, "wb") as f:
    f.write(qr_code_bytes)

# Load the saved QR code image and display it
qr_code_image = Image.open(filename)
qr_code_image.show()
