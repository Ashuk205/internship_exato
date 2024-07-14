from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/ashu', methods=['POST'])
def add_user():
    data = request.get_json()
    first_name = data.get('first_name')
    last_name = data.get('last_name')
    mobile_no = data.get('mobile_no')
    email = data.get('email')

    response = {
        'status': 'success',
        'data': {
            'first_name': first_name,
            'last_name': last_name,
            'mobile_no': mobile_no,
            'email': email
        }
    }
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)
