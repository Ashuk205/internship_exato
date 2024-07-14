from datetime import date, datetime
from flask import Flask, request, jsonify, abort
from models import init_db, db, Book
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@127.0.0.1:3306/books_db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
init_db(app)
 
@app.route('/books', methods=['POST']) 
def create_book():
    data = request.get_json()
    title = data.get('title')
    author = data.get('author')
    issue_date_str = data.get('issue_date')
    return_date_str = data.get('return_date')
    # Validate and convert date strings to datetime.date objects
    try:
        issue_date = datetime.strptime(issue_date_str, '%Y-%m-%d').date() if issue_date_str else None
        return_date = datetime.strptime(return_date_str, '%Y-%m-%d').date() if return_date_str else None
    except ValueError:
        abort(400, description="Invalid date format. Expected YYYY-MM-DD.")

    if not title or not author:
        abort(400, description="Title & Author are required fields.")

    new_book = Book(title=title, author=author, issue_date=issue_date, return_date=return_date)
    db.session.add(new_book)
    db.session.commit()

    return jsonify(new_book.to_dict()), 201
 
@app.route('/books', methods=['GET'])
def read_books():
    books = Book.query.all()
    return jsonify([book.to_dict() for book in books]), 200
 
@app.route('/books/<int:book_id>', methods=['GET'])
def read_book(book_id):
    book = Book.query.get_or_404(book_id)
    return jsonify(book.to_dict()), 200
 
@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = Book.query.get_or_404(book_id)
    data = request.get_json()
    book.title = data.get('title', book.title)
    book.author = data.get('author', book.author)
    book.issue_date = data.get('date', book.issue_date)
    book.return_date = data.get('rdate',book.return_date)
    db.session.commit()
    return jsonify(book.to_dict()), 200
 
@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    book = Book.query.get_or_404(book_id)
    db.session.delete(book)
    db.session.commit()
    return '', 204
 
if __name__ == '__main__':
    app.run(debug=True)