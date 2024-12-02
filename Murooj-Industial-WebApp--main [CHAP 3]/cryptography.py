# cryptography.py

import hashlib

def hash_password(password):
    # Hash the password using SHA-256 algorithm
    hashed_password = hashlib.sha256(password.encode()).hexdigest()
    return hashed_password

 
