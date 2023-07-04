with open('c:/Users/Moroz-ED/Documents/PythonProjects/text.txt', 'r') as f1:
    s = f1.read()
    print(s)
with open('c:/Users/Moroz-ED/Documents/PythonProjects/res.txt', 'w+') as f2:
    f2.write(s[::-1])
    f2.seek(0)
    print(f2.read())