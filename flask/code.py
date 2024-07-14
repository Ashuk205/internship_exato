import qrcode

# Data to be encoded in the QR code
data = "Hello"

# Create a simple QR code
img = qrcode.make(data)

# Save the generated QR code as an image file
img.save("Hello world")

print("QR code generated and saved as Hello.png")
