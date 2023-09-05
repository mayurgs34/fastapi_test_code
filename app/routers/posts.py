from fastapi import APIRouter, Depends, HTTPException, status
from ..database import cursor, conn
from ..oauth2 import get_current_user

router = APIRouter(
    prefix="/posts",
    tags=['posts']
)


@router.get("")
def get_user(tokendata: str = Depends(get_current_user)):
    cursor.execute("""select * from user_details where email = %s""",[tokendata.email]) 
    user_data = cursor.fetchall()
    return {"data":user_data}