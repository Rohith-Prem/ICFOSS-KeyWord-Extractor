import re

in_file = open("tagged_split.txt", 'r', encoding='utf-8')
text = in_file.read()
#print(text)
words = text.split()
#print(words)
tokens = [tk.split('\\') for tk in words if tk != '.']
#print(tokens)
tag = ['NNN', 'NNNP', 'NNST', 'VVMVNF', 'VVAUX'] #nnn-1 nnnp-2 nnnst-3 verb-4
keywords = dict()
id = 0
for t in tokens:
    if t[1] in tag and len(t[0])>2:
        keywords.setdefault(id, []).append(t[0])
        if t[1] == "NNN":
            keywords.setdefault(id, []).append(1)
        elif t[1] == "NNNP":
            keywords.setdefault(id, []).append(2)
        elif t[1] == "NNST":
            keywords.setdefault(id, []).append(3)
        elif t[1] == "VVMNF" or t[1] == "VVAUX":
            keywords.setdefault(id, []).append(4)
        else:
            keywords.setdefault(id, []).append(5)
        id += 1


for i in keywords.keys():
    count = 0
    values = keywords[i]
    check = values[0]
    re.compile(check, re.UNICODE)
    for j in keywords.values():
        if check == j[0]:
            count += 1
    keywords.setdefault(i, []).append(count)

for j in keywords.keys():
    values = keywords[j]
    word = values[]

print(keywords)
