import os
import subprocess
import uuid
from datetime import datetime

import requests
from flask import Flask, request, jsonify, make_response, redirect, url_for

app = Flask(__name__)

os.makedirs('python', exist_ok=True)
os.makedirs('java', exist_ok=True)
os.makedirs('dart', exist_ok=True)

routes = {
    '.py': 'python-executor',
    '.java': 'java-executor',
    '.dart': 'dart-executor'
}


@app.post('/')
def upload_file():
    file = request.files['file']

    file_name, file_extension = os.path.splitext(file.filename)

    print(file_name, file_extension)

    if file_extension in ['.java', '.py', '.dart']:
        # Generate timestamp
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

        # Generate UUID
        file_uuid = str(uuid.uuid4().hex)

        # Create new file name
        new_file_name = os.path.join(f"{file_uuid}_{file_name}{file_extension}")

        # identify if the file contains code in java, python, or dart
        if file_extension == '.java':
            file.save(os.path.join('files', 'java', new_file_name))

        elif file_extension == '.py':
            file.save(os.path.join('files', 'python', new_file_name))

        elif file_extension == '.dart':
            file.save(os.path.join('files', 'dart', new_file_name))

        return make_response({'file_id': file_uuid, 'message': 'File uploaded successfully'}, 200)

    return jsonify({'message': 'Invalid file type'}, 400)


@app.get('/')
def get_status():
    file_id = request.args.get('file_id')

    code_file = None
    folders = os.listdir('files')

    # find the file by its uid and
    for folder in folders:
        for file in os.listdir(f'files/{folder}'):
            if file.startswith(file_id):
                code_file = file
                break
    if code_file is None:
        return make_response(jsonify({'message': 'File not found'}), 404)

    # get the file extension
    file_name = os.path.basename(code_file)
    file_name, file_extension = os.path.splitext(file_name)
    route = routes[file_extension]

    response = requests.post(f"http://{route}:5000/?file_name={file_name}")
    result = response.json()

    # Redirect to another route passing the file path as a query parameter
    return make_response(result, 200)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host="0.0.0.0", port=port)
