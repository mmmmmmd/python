file = open("test.txt")
content = file.read()
file.close()

print content

file = open("test.txt")
while True:
    lines = file.readlines(100)
    if not lines:
        break
    for line in lines :
        print line.strip()
