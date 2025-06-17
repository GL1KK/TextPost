from jose import jwt
from passlib.context import CryptContext

class Security:
    def __init__(self):
        self.__pwd_context = CryptContext(schemes=["argon2"])
    def verify_password(self,hashed_pwd, password):
        return self.__pwd_context.verify(secret=password, hash=hashed_pwd, scheme="argon2")
    def hash_password(self, password):
        return self.__pwd_context.hash(password)