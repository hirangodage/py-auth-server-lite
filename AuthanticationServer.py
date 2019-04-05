from flask import Flask,jsonify
from flask_restful import Api,Resource,reqparse
from flask_jwt_extended import JWTManager, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
import jwt  
import signal

parser=reqparse.RequestParser()
class token(Resource):
   
    def post(self):
        try:
            parser.add_argument('username',help='this filed cannot be blank',required=True)
            parser.add_argument('password',help='this filed cannot be blank',required=True)
            data=parser.parse_args()
            if data['username']==data['password']=='test':
                access_token = jwt.encode({'identity':'testuser','aud':['testapp','testapp2']}, 
                'test-123', algorithm='HS256')
                return {'token':access_token.decode()},200
            else:
                return {'message':'incorrect username password'},404
        except Exception as e:
            return {'message':e}


#main app
AuthApp = Flask(__name__)
api=Api(AuthApp)
api.add_resource(token,'/token')
JWTManager(AuthApp)







