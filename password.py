import os
import hashlib
password = ""


def salted_password(password,salt):
    password = str(password)
    salt = salt.encode()
    hashed = hashlib.sha256(password.encode()+salt).hexdigest()
    return hashed

#THIS WAS GRADED 2.0/2.0
