from flask import Flask
from flask_restful import Api
from user import UserRegister
from flask_jwt import JWT

from item import Item, ItemList
from security import authenticate, identity

app = Flask(__name__)
app.secret_key = 'Furqan'
api = Api(app)

jwt = JWT(app, authenticate, identity)

api.add_resource(Item, '/item/<string:name>')
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, '/register')

if __name__ == '__main__':
    app.run(port=5000, debug = True)


# next me or list me yeh farq hota hai k next sirf ak element list me sy return krta hai jo usy sb sy phly milta hai, jbky list sary elements ko return kr deti hai.
# 400 stands for bad request.
# when we import the file, it runs all the things except methods in it, so if we want to ignore this thing
# we can use if __name__ == '__main__' thing and run everything into it so that it wont run on every import. 
# when we run the file that files becomes the main file so if we run app.py file then this file becomes main file, so everything
# in it is executed. if we run user.py file then that file becomes the main file.
