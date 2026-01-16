import subprocess

result = subprocess.run(
    "echo Hello World",
    capture_output=True,
    text=True,
    shell=True  #because it allow shell scripting
)

print(result.stdout)

subprocess.run(("python", "TC_Multiple_Abstract.py"))
subprocess.run(("python", "TC_Classes.py"))
