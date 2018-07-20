f_in = open("/home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/TnT/new_corpus.txt", "r", encoding='utf-8')
f_out = open("/home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/TnT/clean_corpus.txt", 'w', encoding='utf-8')
inp = f_in.read()
dirty = inp.split('\n')
clean = []
for i in dirty:
    if i not in clean:
        clean.append(i)

for j in clean:
    f_out.write("%s\n" % j)
f_in.close()
f_out.close()

