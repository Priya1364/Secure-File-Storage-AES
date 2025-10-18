
# 🛡️ Secure File Storage System using AES-256

### 🔐 Overview  
This project is a **local file encryption and decryption system** built using **Python** and **AES-256** encryption (via the `cryptography` library).  
It enables users to **securely encrypt, decrypt, and verify files** using a unique AES key with hash verification for integrity.  
The project is fully compatible with **Pydroid (Android)** and **Python 3 (Windows/Linux/Mac)**.

---

### ⚙️ Features  
✅ AES-256 Encryption & Decryption  
✅ Secure Key Generation (Fernet-based)  
✅ SHA-256 Hash Verification (Integrity Check)  
✅ Metadata Storage (filename, timestamp, hash)  
✅ Simple Command-Line Interface (CLI)  
✅ Works 100% offline  

---

### 🛠️ Technologies Used  
- **Python 3**  
- **cryptography (Fernet)**  
- **hashlib (SHA-256)**  
- **json (metadata handling)**  
- **Pydroid 3 (for Android)**  

---

### 🚀 How It Works  

#### 1️⃣ Key Generation  
- The AES key and salt are generated and stored in `key.txt`.  
- This key is reused for encryption and decryption.  

#### 2️⃣ File Encryption  
- Input any file name (e.g., `notes.txt`).  
- It will create an encrypted file `notes.txt.enc`.  
- Metadata (file name, hash, timestamp) is stored in `metadata.json`.  

#### 3️⃣ File Decryption  
- Input encrypted file (e.g., `notes.txt.enc`).  
- The program decrypts and verifies file integrity using SHA-256.  
- Output: `notes.txt_decrypted.txt`.  

---

### 🗂️ Folder Structure
Secure-File-Storage-AES/ │ ├── secure_file_storage.py       # Main Python Script ├── key.txt                      # AES key storage ├── metadata.json                # Metadata and file hash ├── notes.txt                    # Example input file ├── notes.txt.enc                # Encrypted file └── notes.txt_decrypted.txt      # Decrypted output file
Copy code

---

### 📲 How to Run (In Pydroid or Python)
1. Open **Pydroid 3** on Android or **any Python IDE** on PC.  
2. Create a new file named `secure_file_storage.py`.  
3. Paste the full script code.  
4. Run the file.  
5. Choose an option from the menu:
--- Secure File Storage ---
Encrypt a file
Decrypt a file
Exit

6. Follow the on-screen instructions to encrypt or decrypt files.  

---

### 💻 Example Output
✅ AES key loaded from key.txt
--- Secure File Storage ---
Encrypt a file
Decrypt a file
Exit Enter choice: 1 Enter file name to encrypt: notes.txt ✅ File encrypted: notes.txt.enc ✅ Metadata saved (for hash verification)
--- Secure File Storage ---
Encrypt a file
Decrypt a file
Exit Enter choice: 2 Enter encrypted file name (.enc): notes.txt.enc ✅ File decrypted: notes.txt_decrypted.txt ✅ Integrity check passed: file is safe!


---

### 👩‍💻 Author  
**Priyadharshini L**  
B.E. Cybersecurity | Paavai Engineering College  
GitHub: [@Priya1364](https://github.com/Priya1364)

---

### 🌱 Future Enhancements  
- GUI version using **PyQt5**  
- Password-protected metadata  
- Batch file encryption/decryption  
- Cloud backup for encrypted files  


### 📄 License  
This project is licensed under the **MIT License** — free to use and modify.
