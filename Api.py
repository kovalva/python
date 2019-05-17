"""Document containing REST-interface."""
from flask import Flask, request, jsonify, abort, make_response
from Library import Library

app = Flask(__name__)
MyLibrary = Library()


@app.route('/library', methods=['GET'])
def get_book():
    """Function that allows you to get
     a list of books from the library.
    """
    return jsonify({'library': MyLibrary.books})


@app.route('/library/<int:book_id>', methods=['GET'])
def get_book_id(book_id):
    """Function that allows you to get
     a books from the library by id.
    """
    if len(MyLibrary.books) <= book_id or book_id < 0:
        abort(404)
    book = MyLibrary.books[book_id]
    return jsonify({'book': book})


@app.route('/library/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    """Function that allows you to delete
     a book from the library by id.
    """
    if len(MyLibrary.books) <= book_id or book_id < 0:
        abort(404)
    book = [MyLibrary.books[book_id]]
    MyLibrary.DeleteBook(book)
    return jsonify({'result': True})


@app.route('/library', methods=['POST'])
def create_book():
    """Function that allows you to add
     a book to the library.
    """
    if not request.json:
        abort(400)

    for key in MyLibrary.book_attributes:
        if key not in request.json or request.json[key] == '':
            abort(400)

    try:
        if int(request.json['Pages']) <= 0 or \
                type(request.json['Take_status']) is not bool:
            abort(400)
    except ValueError:
        abort(400)

    MyLibrary.books.append(request.json)
    MyLibrary.JsonObj.update_json(MyLibrary.JsonObj.json_file_path,
                                  MyLibrary.books)
    return jsonify({'new_book': request.json}), 201


@app.route('/library/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    """Function that allows you to update
     a book from the library by id.
    """
    if len(MyLibrary.books) <= book_id or book_id < 0:
        abort(404)

    if not request.json:
        abort(400)

    for key in MyLibrary.book_attributes:
        if key not in request.json or request.json[key] == '':
            abort(400)

    try:
        if int(request.json['Pages']) <= 0 or \
                type(request.json['Take_status']) is not bool:
            abort(400)
    except ValueError:
        abort(400)

    for key in MyLibrary.book_attributes:
        MyLibrary.books[book_id][key] = request.json[key]

    return jsonify({'updated_book': MyLibrary.books[book_id]})


@app.errorhandler(404)
def not_found(error):
    """Function that describe 404 error.
    """
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
