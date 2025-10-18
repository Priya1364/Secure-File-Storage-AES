# encrypt_file.py
from cryptography.fernet import Fernet

# 🔑 Use your AES key here
key = b"O9arv9M5uKe4oqtOGU-5a9wSbXoyssbpPYuQ6a2l89c="
fernet = Fernet(key)

# 📄 Ask for file to encrypt
file_path = input("Enter file name (example: notes.txt): ")

# ✅ Read and encrypt file
with open(file_path, "rb") as f:
    data = f.read()

encrypted_data = fernet.encrypt(data)

# 💾 Save encrypted file with .enc extension
enc_path = file_path + ".enc"
with open(enc_path, "wb") as f:
    f.write(encrypted_data)

print("\n✅ File encrypted successfully!")
print("Encrypted file saved as:", enc_path)