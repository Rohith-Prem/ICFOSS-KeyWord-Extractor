import re

in_file = open("tagged_split.txt", 'r', encoding='utf-8')
number_of_words = open("wordcount.txt", 'r')
text = in_file.read()
#print(text)
words = text.split()
#print(words)
tokens = [tk.split('\\') for tk in words if '\\' in tk]
#print(tokens)
tag = ['NNN', 'NNNP', 'NNST', 'VVMVNF', 'VVAUX'] #nnn-1 nnnp-2 nnnst-3 verb-4
keywords = dict()
id = 0
#filtering nouns and verbs and assigning priority
for t in tokens:
    if t[1] in tag and len(t[0])>2:
        keywords.setdefault(id, []).append(t[0])
        if t[1] == "NNN":
            keywords.setdefault(id, []).append(1)
        elif t[1] == "NNNP":
            keywords.setdefault(id, []).append(2)
        elif t[1] == "NNST":
            keywords.setdefault(id, []).append(3)
        elif t[1] == "VVMVNF" or t[1] == "VVAUX":
            keywords.setdefault(id, []).append(4)
        else:
            break
            #keywords.setdefault(id, []).append(5)
        id += 1


#counting frequency
for i in keywords.keys():
    count = 0
    values = keywords[i]
    check = values[0]
    re.compile(check, re.UNICODE)
    for j in keywords.values():
        if check == j[0]:
            count += 1
    keywords.setdefault(i, []).append(count)

#print(keywords)

#deleting duplicates
result = {}
for key, value in keywords.items():
    if value not in result.values():
        result[key] = value

#print(result)

#changing frequency to relative term frequency
wordcount = float(number_of_words.read())
for key, value in result.items():
    tf = value[2]/wordcount
    result[key] = [value[0], value[1], tf]

print(result)

#assigning depth
