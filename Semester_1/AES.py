import base64

text = "Skateboarding is fun"

# Encode
encoded = base64.b64encode(text.encode())

# Decode
decoded = base64.b64decode(encoded).decode()

print("Encoded:", encoded)
print("Decoded:", decoded)