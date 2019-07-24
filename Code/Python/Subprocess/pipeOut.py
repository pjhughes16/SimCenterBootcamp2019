import subprocess

# start a $ `cat -` and connect a pipe to STDIN
p = subprocess.Popen(['cat','-'],stdin=subprocess.PIPE)

# send a byte stream to PIPE
# ... create the string
s = "Hello, World!\nHello, Peter!\n"

# ... convert to byte stream ===> encoding
b = s.encode(encoding='utf-8', errors='strict')

# send to PIPE
p.communicate(b);

