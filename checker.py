import hashlib
import os
import json

# Choose hashing algorithm
def calculate_hash(filepath):
    sha256_hash = hashlib.sha256()
    try:
        with open(filepath, "rb") as f:
            # Read and update hash in chunks
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

# Save current hash values for files in a folder
def save_hashes(directory, output_file="hash_store.json"):
    hash_data = {}
    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            hash_data[full_path] = calculate_hash(full_path)
    with open(output_file, "w") as f:
        json.dump(hash_data, f, indent=4)
    print(f"[✓] Hashes saved to {output_file}")

# Compare current hash values to previously stored ones
def check_integrity(directory, hash_file="hash_store.json"):
    if not os.path.exists(hash_file):
        print("[!] No saved hash file found.")
        return
    with open(hash_file, "r") as f:
        old_hashes = json.load(f)

    for root, _, files in os.walk(directory):
        for file in files:
            full_path = os.path.join(root, file)
            new_hash = calculate_hash(full_path)
            old_hash = old_hashes.get(full_path)

            if old_hash is None:
                print(f"[NEW] {full_path}")
            elif new_hash != old_hash:
                print(f"[MODIFIED] {full_path}")
            else:
                print(f"[OK] {full_path}")

if __name__ == "__main__":
    save_hashes("C:/Users/GK/Documents")       # To initialize and save hashes
    check_integrity("C:/Users/GK/Documents")   # To check for changes later