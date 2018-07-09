from Features.feature_extraction import data

input = open("output.txt", 'r').read()
line = input.split('\n')
feat = [l.split() for l in line]
#print(feat)
labels = [l[4] for l in feat]
#print(labels)
words = data()
dictr = words.word_features
#print(dictr)
keywords = []
i = 1
for l in labels:
    if l == "B_K":
        value = dictr[i]
        keywords.append(value[0])
        i+=1
    else:
        i+=1

print(keywords)


#print(keywords)

