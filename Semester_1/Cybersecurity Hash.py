import hashlib
text = "skateboarding is fun"

# SHA-256 HASH
hash_object = hashlib.sha256(text.encode())
hashed_text = hash_object.hexdigest()

print("Original:", text)
print("Sha-256:", hashed_text)