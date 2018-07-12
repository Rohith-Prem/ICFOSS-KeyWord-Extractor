from Features.feature_extraction import data

input = open("/home/rohith/ICFOSS-KeyWord-Extractor/Extracion/output.txt", 'r').read()
line = input.split('\n')
feat = [l.split() for l in line]
#print(feat)
#print(len(feat))
labels = [l[4] for l in feat]
#print(labels)
#print(len(labels))
words = data()
dictr = words.word_features
#print(dictr)
#print(len(dictr))
keywords = []

malwords = []
for val in dictr.values():
    malwords.append(val[0])

#print(malwords)
i = 0
for lab in labels:
    if lab == "B_K":
        value = malwords[i]
        keywords.append(value)
        i+=1
    else:
        i+=1
        continue

print(keywords) #final keyword output


#print(keywords)

