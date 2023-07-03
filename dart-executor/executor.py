import os
import subprocess
path = os.path.dirname(os.path.realpath(__file__))


def execute(file_name):

    base_name = os.path.basename(file_name)
    os.chdir(os.path.join(path, 'files'))
    compile_process = subprocess.Popen(['dart', 'compile', 'exe', f"./{file_name}.dart"], stdout=subprocess.PIPE,
                                       stderr=subprocess.PIPE)
    compile_process.wait()

    result = subprocess.run([f"./{base_name}.exe"], capture_output=True)
    output = result.stdout.decode('utf-8')
    error = result.stderr.decode('utf-8')
    os.remove(f"./{base_name}.exe")
    os.remove(f"./{file_name}.dart")
    return {'output': output, 'error': error}


if __name__ == "__main__":
    pass
