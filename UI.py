import subprocess

binary_path = '/Users/benjaminliu/Desktop/VS\ Code/calculator'

proc = subprocess.Popen(binary_path, shell=True)

proc.wait()

return_code = proc.returncode
output, error = proc.communicate()
print("Output: ", output)
print("Error: ", error)
print("Return code: ", return_code)
