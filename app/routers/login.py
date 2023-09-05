from fastapi import APIRouter, Depends, HTTPException, status
from .. import oauth2
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from ..database import cursor, conn
from ..utils import hash_pwd, verify_pwd

router = APIRouter(
    prefix="/login",
    tags=['login']
)


@router.post("")
def login(user_cred: OAuth2PasswordRequestForm = Depends()): 

    cursor.execute("""select password from user_details where email = %s""",[user_cred.username]) 
    user_pwd = cursor.fetchone()

    if not user_pwd:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user details not found")
    
   
    if not verify_pwd(user_cred.password,user_pwd['password']):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail="user details does not match")
    

    access_token = oauth2.create_access_token(data = {"user_email": user_cred.username})

    return {"access_token":access_token, "token_type": "bearer"}