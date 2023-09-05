from fastapi import APIRouter
from ..schemas import signUp
from ..database import cursor, conn
from ..utils import hash_pwd
import uuid

router = APIRouter(
    prefix="/signup",
    tags=['signup']
)


@router.post("")
def sign_up(sign_up: signUp):
    
    uuid_id = str(uuid.uuid1())

    #password hashed
    hashed_pwd = hash_pwd(sign_up.password)
    sign_up.password = hashed_pwd

    cursor.execute("""insert into user_details (id, first_name, last_name, 
                   email, password) values (%s, %s, %s, %s, %s)""", (uuid_id,sign_up.first_name,sign_up.last_name,sign_up.email,sign_up.password)) 
    conn.commit()

    return {"message" : "user data saved in database"}