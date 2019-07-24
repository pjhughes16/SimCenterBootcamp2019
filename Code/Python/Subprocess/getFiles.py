import subprocess

p = subprocess.Popen(['ls', '-l'], stdout=subprocess.PIPE)

res = p.communicate()[0]

s = res.decode(encoding='utf-8', errors='strict')
slist = s.strip().split('\n')

cnt = 0

for item in slist:
    print("{}: {}".format(cnt, item))
    cnt += 1

