from Features.feature_extraction import data

f = open("/home/rohith/ICFOSS-KeyWord-Extractor/Extraction/output.txt", 'r').read()
line = f.split('\n')
feat = [l.split() for l in line]
end = len(feat)-1
feat.__delitem__(end)
#print(feat)
#print(len(feat))
labels = []
labels = [l[4] for l in feat[:-1] 
#print(labels)
#print(len(labels))
words = data()
dictr = words.word_features
#print(dictr)
print(len(dictr))
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

