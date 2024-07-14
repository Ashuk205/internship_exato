from flask import Flask, request, jsonify, make_response
 
app = Flask(__name__)
 
users = {}
 
@app.route('/register', methods = ['POST'])
def register():
    data = request.json
 
    username = data['username']
    password = data['password']
 
    if username in users:
        return jsonify({'message': 'user already exists!'})
    else:
        return jsonify({'message': 'successfully registered'})
     
 
if __name__ == '__main__':
    app.run(debug=True)
