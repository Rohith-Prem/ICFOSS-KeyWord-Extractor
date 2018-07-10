# -*- coding: utf-8 -*-
import re
import csv


in_file = open("E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\Features\\tagged_split.txt", 'r', encoding='utf-8')
number_of_words = open("E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\Features\\wordcount.txt", 'r')
text = in_file.read()
# print(text)
words = text.split()
# print(words)
tokens = [tk.split('\\') for tk in words if '\\' in tk]
# print(tokens)
tag = ['NNN', 'NNNP', 'NNST', 'VVMVNF', 'VVAUX']  # nnn-1 nnnp-2 nnnst-3 verb-4
keywords = dict()



class FeatureExtractor:

    final_result = dict()
    def main(self):
        id = 1
        # filtering nouns and verbs and assigning priority
        for t in tokens:
            if t[1] in tag and len(t[0]) > 2:
                keywords.setdefault(id, []).append(t[0])
                if t[1] == "NNN":
                    keywords.setdefault(id, []).append("NNN")
                elif t[1] == "NNNP":
                    keywords.setdefault(id, []).append("NNNP")
                elif t[1] == "NNST":
                    keywords.setdefault(id, []).append("NNST")
                elif t[1] == "VVMVNF":
                    keywords.setdefault(id, []).append("VVMVNF")
                elif t[1] == "VVAUX":
                    keywords.setdefault(id, []).append("VVAUX")
                else:
                    break
                    # keywords.setdefault(id, []).append(5)
                id += 1

        # print(keywords)

        # counting frequency
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
        result = {}
        #deleting duplicates
        for key, value in keywords.items():
            if value not in result.values():
                result[key] = value
        #print(result)

    # changing frequency to relative term frequency
        wordcount = float(number_of_words.read())
        for key, value in result.items():
            tf = value[2] / wordcount
            result[key] = [value[0], value[1], tf]
        # print(result)

        # checking presence in heading and url
        headurl = open("E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\Features\\head_url.txt", 'r', encoding='utf-8').read()
        headurl_words = headurl.split()
        # print(headurl_words)
        for key, value in result.items():
            if value[0] in headurl_words:
                result.setdefault(key, []).append(1)
            else:
                result.setdefault(key, []).append(0)
        #print(result)

        #assigning depth
        for key,values in result.items():
            depth = float(key/wordcount)
            result.setdefault(key, []).append(depth)
        #print(result)

        self.final_result = result

        #writing to features text file
        f_out = open("features.txt", 'w', encoding='utf-8')
        for value in result.values():
            wd = str(value[0])
            pos = str(value[1])
            tf = str(value[2])
            hu = str(value[3])
            dp = str(value[4])
            line = wd + " " + pos + " " + tf + " " + hu + " " + dp
            f_out.write(line+"\n")

#if __name__ == '__main__':
#    a = FeatureExtractor()
#    a.main()

class data:
    var = FeatureExtractor()
    var.main()
    word_features = var.final_result





#with open('features.csv', 'a') as csvfile:
    #fieldnames = ['POS', 'TF', 'Head/URL', 'Depth']
    #writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    #writer = csv.writer(csvfile)
    #writer.writeheader()
#    for value in result.values():
        #malword = value[0].encode('utf-8')
#        writer.writerow({'POS': value[1], 'TF': value[2], 'Head/URL': value[3], 'Depth': value[4]})
