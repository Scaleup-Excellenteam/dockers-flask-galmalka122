import os
import subprocess
path = os.path.dirname(os.path.realpath(__file__))


def execute(file_name):

    base_name = os.path.basename(file_name)
    os.chdir(os.path.join(path, 'files'))
    compile_process = subprocess.Popen(['javac', f"./{file_name}.java"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    compile_process.wait()

    java_file = ''.join(base_name.split('_', 1)[1:])

    result = subprocess.run(['java', f"{java_file}"], capture_output=True)
    output = result.stdout.decode('utf-8')
    error = result.stderr.decode('utf-8')
    os.remove(f"./{java_file}.class")
    os.remove(f"./{base_name}.java")
    return {'output': output, 'error': error}


if __name__ == "__main__":
    pass
