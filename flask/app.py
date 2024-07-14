# if __name__ == "__main__":
#     app.run(debug=True)
 
from flask import Flask, jsonify, request
 
# creating a Flask app
app = Flask(__name__)
 
# on the terminal type: curl http://127.0.0.1:5000/
# returns hello world when we use GET.
# returns the data that we send when we use POST.
@app.route('/hello', methods = ['GET', 'POST'])
def home():
    if(request.method == 'GET'):
 
        data = "hello world"
        return jsonify({'data': data})
    else:
        data = "Hello Ritesh"
        return jsonify({'data': data})
 