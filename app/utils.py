from werkzeug.security import generate_password_hash, check_password_hash

def hash_password(password):
    """Hashes a password using Werkzeug's security module."""
    return generate_password_hash(password)

def check_password(password, hashed_password):
    """Checks a password against a hashed password."""
    return check_password_hash(hashed_password, password)