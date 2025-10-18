# decrypt_file.py
from cryptography.fernet import Fernet

# 🔑 Same AES key used for encryption
key = b"O9arv9M5uKe4oqtOGU-5a9wSbXoyssbpPYuQ6a2l89c="
fernet = Fernet(key)

# 📂 Ask for encrypted file name
enc_file = input("Enter encrypted file name (example: notes.txt.enc): ")

# 🔓 Read and decrypt
with open(enc_file, "rb") as f:
    encrypted_data = f.read()

decrypted_data = fernet.decrypt(encrypted_data)

# 💾 Save as new file
output_file = enc_file.replace(".enc", "_decrypted.txt")
with open(output_file, "wb") as f:
    f.write(decrypted_data)

print("\n✅ File decrypted successfully!")
print("Decrypted file saved as:", output_file)