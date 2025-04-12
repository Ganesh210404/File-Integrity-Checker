# File-Integrity-Checker
🔐 File Integrity Checker

A simple Python tool to monitor file integrity by calculating and comparing SHA-256 hash values. This tool helps detect unauthorized file modifications, additions, or deletions — a vital component in cybersecurity workflows.

📌 Features
Calculates SHA-256 hash values for files

Saves current hash states to a JSON file

Compares current file hashes with previously saved hashes

Detects new, modified, or unchanged files

Supports entire directory scanning

🧰 Tech Stack
Python 3.x

hashlib – for hashing

os – for file system navigation

json – for saving hash data

🚀 How to Use
1. Clone the Repository
bash

git clone https://github.com/ganesh210404/File-Integrity-Checker.git cd File-Integrity-Checker

2. Save Hashes (Initial Snapshot)

# Inside Python
from checker import save_hashes
save_hashes("path/to/your/folder")

3. Check for File Changes

from checker import check_integrity
check_integrity("path/to/your/folder")

Example Output:
pgsql

[OK]        path/to/file.txt
[MODIFIED]  path/to/modified_file.py
[NEW]       path/to/new_file.md

📂 File Structure
pgsql

file-integrity-checker/
│
├── checker.py         # Main script with save and check functions
├── hash_store.json    # Auto-generated hash database (optional)
└── README.md          # This file

📎 Use Cases

Monitoring web server file integrity

Detecting unauthorized file changes

Securing configuration or log files

Periodic integrity audits

📢 Notes

Only files are hashed (not directories).

Uses SHA-256 for strong integrity checking.

Can be extended with alerts, logging, or GUI support.

📜 License

MIT License – use it freely with credits!