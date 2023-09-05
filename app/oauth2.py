from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, status, HTTPException
from fastapi.security import OAuth2PasswordBearer
from .schemas import tokenData

oauth2_scheme = OAuth2PasswordBearer(tokenUrl='login')

SECRET_KEY = "testsecretkey"
ALGORITHM = "HS256"
EXPIRATION_TIME_MIN = 30

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=EXPIRATION_TIME_MIN)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str, cred_excep):
    try:    
        payload = jwt.decode(token, SECRET_KEY,algorithms=[ALGORITHM])
        email: str = payload.get("user_email")

        if email is None:
            raise cred_excep
        
        token_data = tokenData(email=email) 
    except JWTError:
        raise cred_excep
    
    return token_data
    

def get_current_user(token: str = Depends(oauth2_scheme)):
    cred_excep = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="could not validate credentials",
                               headers={"WWW-Authenticate":"Bearer"})
    return verify_access_token(token,cred_excep)


