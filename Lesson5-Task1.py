file = open('text.txt', 'w')
line = input()
while line.strip():
    file.write(line + "\n")
    line = input()
file.close()