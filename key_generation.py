# step2_key_generation.py
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from base64 import urlsafe_b64encode
import os

# Step 2: Generate AES-256 Key from password
password = input("Enter your password: ").encode()
salt = os.urandom(16)  # Random salt (save this safely for decryption)

kdf = PBKDF2HMAC(
    algorithm=hashes.SHA256(),
    length=32,
    salt=salt,
    iterations=100000,
)

key = urlsafe_b64encode(kdf.derive(password))

print("\n✅ AES-256 key generated successfully!")
print("Key:", key.decode())
print("Salt (save this):", salt.hex())