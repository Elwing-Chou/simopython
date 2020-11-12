import subprocess


with open("out.txt", "w") as f1, open("err.txt", "w") as f2:
    cmd = ["/usr/local/bin/python3.6", "test.py"]
    result = subprocess.run(cmd, stdout=f1, stderr=f2)
    print(result)

