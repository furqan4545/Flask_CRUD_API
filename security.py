from werkzeug.security import safe_str_cmp
from user import User

def authenticate(username, password):
    user = User.find_by_username(username)
    if user and safe_str_cmp(user.password, password):
        return user
    
def identity(payload):
    user_id = payload['identity']
    uuu = 0
    for i in user_id:
        uuu = i
    print(uuu)
    return User.find_by_id(uuu)
    

# .get is another way of accessing dictionary. 
# safe_str_cmp is the method to compare two strings. 
# authenticate method username and password khud bakhud utha rha hai from postman 
# or payload bhi wo generated token ko ly rha hai khud bakhud 
    
    
    