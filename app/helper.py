import subprocess

# comandos shell
def cowsay(e="lol"):
	return subprocess.Popen(['cowsay', '-f', 'daemon', e], stdout=subprocess.PIPE).communicate()

def ls(path):
	return subprocess.Popen(['cowsay', '-f', 'daemon', e], stdout=subprocess.PIPE).communicate()