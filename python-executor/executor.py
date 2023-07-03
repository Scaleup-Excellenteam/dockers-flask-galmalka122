import os
import subprocess
path = os.path.dirname(os.path.realpath(__file__))


def execute(file_name):
    os.chdir(os.path.join(path, 'files'))
    result = subprocess.run(['python', f"./{file_name}.py"], capture_output=True)
    output = result.stdout.decode('utf-8')
    error = result.stderr.decode('utf-8')
    os.remove(f"./{file_name}.py")

    return {'output': output, 'error': error}
