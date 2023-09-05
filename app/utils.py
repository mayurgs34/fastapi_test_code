from passlib.context import CryptContext 

pwd_context = CryptContext(schemes=["bcrypt"])

def hash_pwd(password: str):
    return pwd_context.hash(password)

def verify_pwd(plain_pwd, hashed_pwd):
    return pwd_context.verify(plain_pwd,hashed_pwd)