# secure_file_storage.py
from cryptography.fernet import Fernet
import hashlib
import json
from datetime import datetime
import os

# ---------- Step 1: Generate or enter AES key ----------
# For first use, generate new key. Save this key safely.
if not os.path.exists("key.txt"):
    key = Fernet.generate_key()
    with open("key.txt", "wb") as f:
        f.write(key)
    print("✅ New AES key generated and saved in key.txt")
else:
    with open("key.txt", "rb") as f:
        key = f.read()
    print("✅ AES key loaded from key.txt")

fernet = Fernet(key)

# ---------- Functions ----------

def file_hash(file_path):
    """Return SHA-256 hash of a file"""
    hasher = hashlib.sha256()
    with open(file_path, "rb") as f:
        hasher.update(f.read())
    return hasher.hexdigest()

def encrypt_file(file_path):
    """Encrypt file and save .enc + metadata"""
    with open(file_path, "rb") as f:
        data = f.read()
    encrypted_data = fernet.encrypt(data)
    enc_path = file_path + ".enc"
    with open(enc_path, "wb") as f:
        f.write(encrypted_data)
    print(f"✅ File encrypted: {enc_path}")

    # Save metadata
    metadata = {
        "file_name": file_path,
        "time": str(datetime.now()),
        "hash": file_hash(file_path)
    }
    with open("metadata.json", "w") as f:
        json.dump(metadata, f)
    print("✅ Metadata saved (for hash verification)")

def decrypt_file(enc_path):
    """Decrypt file and verify hash"""
    with open(enc_path, "rb") as f:
        encrypted_data = f.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    output_file = enc_path.replace(".enc", "_decrypted.txt")
    with open(output_file, "wb") as f:
        f.write(decrypted_data)
    print(f"✅ File decrypted: {output_file}")

    # Verify hash
    with open("metadata.json", "r") as f:
        metadata = json.load(f)
    decrypted_hash = file_hash(output_file)
    if decrypted_hash == metadata["hash"]:
        print("✅ Integrity check passed: file is safe!")
    else:
        print("⚠️ Integrity check failed: file may be tampered!")

# ---------- Main Menu ----------

while True:
    print("\n--- Secure File Storage ---")
    print("1. Encrypt a file")
    print("2. Decrypt a file")
    print("3. Exit")
    choice = input("Enter choice: ")

    if choice == "1":
        file_path = input("Enter file name to encrypt: ")
        if os.path.exists(file_path):
            encrypt_file(file_path)
        else:
            print("❌ File does not exist.")
    elif choice == "2":
        enc_path = input("Enter encrypted file name (.enc): ")
        if os.path.exists(enc_path):
            decrypt_file(enc_path)
        else:
            print("❌ Encrypted file does not exist.")
    elif choice == "3":
        print("Exiting...")
        break
    else:
        print("❌ Invalid choice")