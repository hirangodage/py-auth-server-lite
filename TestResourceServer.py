from flask import Flask,jsonify
from flask_restful import Api,Resource,reqparse
from flask_jwt_extended import JWTManager, jwt_required, jwt_refresh_token_required, get_jwt_identity, get_raw_jwt
import jwt  
import signal

parser=reqparse.RequestParser()
#to test above token endpoint
class testcall(Resource):
    #no authantication required
    def post(self):
        parser.remove_argument('username')
        parser.remove_argument('password')
        return {'data':'ping'},200

    #valid token required    
    @jwt_required
    def get(self):
        return {"message":"authanticated"},200

#main app
TestApp = Flask(__name__)
api=Api(TestApp)
api.add_resource(testcall,'/ping')
JWTManager(TestApp)

#configurations
TestApp.config['JWT_SECRET_KEY']='test-123'
TestApp.config['JWT_DECODE_AUDIENCE']='testapp'