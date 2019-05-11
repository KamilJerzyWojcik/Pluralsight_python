import sys

print(len(sys.argv))

if len(sys.argv) == 1:
    print("USAGE: python3 command_argument.py <password>")
else:
    password = sys.argv[1]
    print("Password: ", password)