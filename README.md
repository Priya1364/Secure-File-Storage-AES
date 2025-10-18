# Secure-File-Storage-AES
AES-256 File Encryption/Decryption System with Hash Verification in Python (Pydroid)
🛡️ Secure File Storage System using AES-256
📘 Overview
This project is a local file encryption and decryption system built using Python and the AES-256 algorithm (via the cryptography library).
It allows users to securely store, encrypt, decrypt, and verify the integrity of files using a unique AES key and hash verification.
Built and tested on Pydroid (Android) for easy mobile encryption.
⚙️ Features
✅ AES-256 Encryption & Decryption
✅ Secure Key Generation (Fernet-based)
✅ SHA-256 Hash Verification to prevent tampering
✅ Metadata storage for filename, timestamp, and hash
✅ CLI Interface (simple and lightweight)
✅ Works fully offline on Android (Pydroid 3)
🧠 Technologies Used
Python 3
Cryptography (Fernet)
Hashlib (SHA-256)
JSON for metadata storage
🚀 How It Works
Generate AES Key
A key and salt are generated using a password.
Key is saved securely in key.txt.
Encrypt File
Enter the filename (e.g., notes.txt).
The system encrypts it into notes.txt.enc.
Metadata (hash, timestamp, original filename) is stored securely.
Decrypt File
Enter the encrypted file name (e.g., notes.txt.enc).
The system decrypts it and verifies integrity.
Decrypted file saved as notes.txt_decrypted.txt.
🗂️ Folder Structure


SecureFileStorage/
│
├── secure_file_storage.py
├── key.txt
├── metadata.json
├── notes.txt
├── notes.txt.enc
└── notes.txt_decrypted.txt
🪄 How to Run (in Pydroid or Python)
Open Pydroid 3 on your Android.
Create a new file named secure_file_storage.py.
Paste the full code inside it.
Run the program.
Follow on-screen steps to encrypt or decrypt files.
🧩 Example Output


✅ AES key loaded from key.txt

--- Secure File Storage ---
1. Encrypt a file
2. Decrypt a file
3. Exit
Enter choice: 1
Enter file name to encrypt: notes.txt
✅ File encrypted: notes.txt.enc
✅ Metadata saved (for hash verification)

--- Secure File Storage ---
1. Encrypt a file
2. Decrypt a file
3. Exit
Enter choice: 2
Enter encrypted file name (.enc): notes.txt.enc
✅ File decrypted: notes.txt_decrypted.txt
✅ Integrity check passed: file is safe!
👩‍💻 Author
Priyadharshini L
B.E. Cybersecurity | Paavai Engineering College
GitHub: @Priya1364
🏆 Future Enhancements
Add GUI using PyQt5
Password-protected metadata
Multiple file encryption support
Secure cloud backup integration
