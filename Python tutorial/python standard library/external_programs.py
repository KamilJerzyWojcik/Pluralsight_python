import subprocess

# completed = subprocess.run(["ls", "-l"],
#                            capture_output=True,
#                            text=True)

try:
    completed = subprocess.run(["python3", "other.py"],
                               capture_output=True,
                               text=True,
                               check=True)

    print("")
    print("----prop---")
    print("args: ", completed.args)
    print("return code: ", completed.returncode)
    print("stderr: ", completed.stderr)
    print("stdout: ", completed.stdout)

except subprocess.CalledProcessError as ex:
    print(ex)

