from flask import Flask, request, jsonify, make_response

from executor import execute

app = Flask(__name__)


@app.route('/', methods=['POST'])
def dart_executor():
    try:
        file_name = request.args.get('file_name')
        result = execute(file_name)

        return make_response(jsonify(result), 200)

    except Exception as e:
        return make_response(jsonify({'error': str(e)}), 500)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
