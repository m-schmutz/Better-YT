#!./env/bin/python3

from subprocess import run, check_output

result = run(['which', 'asdf'], capture_output=True, text=True)
result = check_output(['which', 'asdf'])



# print("STDOUT:", result.stdout)
# print("STDERR:", result.stderr)
# print("Return code:", result.returncode)
