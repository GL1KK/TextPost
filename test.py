from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def verify_password():
    password = "okak10"
    hashed = pwd_context.hash(password) 
    print(hashed)
    print(pwd_context.verify("okak11", hashed))

verify_password()