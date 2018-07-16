from irtokz.indic_tokenize import tokenize_ind
import re


#test_file = open("test.txt", "w", encoding="utf-8")

def splitTagged():
    in_file = open("/home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/tagged_text.txt", "r", encoding="utf-8")
    out_file = open("/home/rohith/ICFOSS-KeyWord-Extractor/Features/tagged_split.txt", "w", encoding="utf-8")
    lines = in_file.readlines()
    del lines[0:12]
    del lines[-2:]
    in_file.close()
    in_file = open("/home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/tagged_text.txt", "w", encoding="utf-8")
    in_file.writelines(lines)
    in_file.close()
    in_file = open("/home/rohith/ICFOSS-KeyWord-Extractor/POSTagging/tagged_text.txt", "r", encoding="utf-8")
    inp = in_file.read()
    in_file.close()
    language = "mal"
    tok = tokenize_ind(lang="'"+language+"'", split_sen=True)
    text = tok.tokenize(inp)
    print(text)
    out_file.write("%s" % text)
    out_file.close()









