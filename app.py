from flask import Flask, request, jsonify, make_response
from dbhelpers import run_statement
from helpers import check_endpoint_info 
from flask_cors import CORS 

app = Flask(__name__)
CORS(app)

#Users SignUp Function

@app.post('/api/user')
def post_user():
    valid_check = check_endpoint_info(request.json, ['first_name', 'last_name', 'email', 'password', 'phone_number'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL user_signUp(?, ?, ?, ?, ?)", [request.json.get("first_name"), request.json.get("last_name"), request.json.get("email"), request.json.get("password"), request.json.get("phone_number")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify(results[0]), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)




#Users login function

@app.post('/api/userLogin')
def post_user_login():
    valid_check = check_endpoint_info(request.json, ['email', 'password'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL user_login(?, ?)", [ request.json.get("email"), request.json.get("password")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify(results[0]), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)



#User Contact function

@app.post('/api/contact')
def post_contact():
    valid_check = check_endpoint_info(request.json, ['first_name', 'email', 'general_inquiry', 'message'])
    if(valid_check != None):
        return make_response(jsonify(valid_check), 400)
    results = run_statement("CALL post_contact(?, ?, ?, ?)", [ request.json.get("first_name"), request.json.get("email"), request.json.get("general_inquiry"), request.json.get("message")])
    print(results)
    if(type(results) == list):
        return make_response(jsonify(results[0]), 200)
    else: 
        return make_response(jsonify("Sorry, something went wrong"), 500)







app.run(debug=True)
