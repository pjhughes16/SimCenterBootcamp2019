import subprocess

p = subprocess.Popen(['./greet'], stdin=subprocess.PIPE)

firstname = 'Peter'
lastname  = 'Mackenzie-Helnwein'

answers      = (firstname, lastname)
answerString = "\n".join(answers)
answerBytes  = answerString.encode(encoding='utf-8', errors='strict')

# send answers to STDIN
p.communicate(answerBytes)

