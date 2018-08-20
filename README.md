# ICFOSS-KeyWord-Extractor
### This project was implemented as a part of the summer internship programme at ICFOSS, Thiruvananthapuram, under the guidance of Dr. Rajeev R R.
#### This project is an Automatic Keyword Extractor for Malayalam News Articles. 

#### Program Modules
1)Web scrapping: scrap.py accepts an url using which it will extract the main paragraphs from the corresponding webpage and write it to scrapped_text.txt inside Tokenize folder. This code has to be modified according to the arrangement of text in the chosen webpage.

2)Pre-processing: the scrapped text contains junk characters and english characters which must be removed. tokenise.py removes all unwanted characters but retains non_breaking prefixes like 'Dr.' 'Mr' etc. The cleaned text is then tokenized into words and stored in tokenized_text.txt inside POSTagging folder.

3)POS Tagging: A TnT Tagger was trained with over 70,000 thousand words annotated with the BIS Tagset to form a POS Tagger. POStagger.py tags the tokenized text which is again cleaned and split using split_tagged.py. The final tagged words are written to tagged_split.txt inside Features folder.

4)Feature Extraction: The following features are extracted from each word:-

    i)POS tag(POS)
   ii)Term frequency(TF) (word freq/max word freq)
  iii)Depth(DEP) (position of first occurence/total number of words)
   iv)Length(LEN) (word length/max word length)
   v)Presence in Heading(H)
   
  feature_extraction.py extracts the following features from each word in tagged_split.txt and writes the feature vectors to               features.txt. This dataset can be used for training after manual labelling of keywords, or can be fed into the CRF model to be           labelled automatically.
  
5)CRF model: The current CRF model has been trained with over 5000 words from about 50 news articles. predict.py will labell the feature vectors using the trained CRF model. For instructions on using CRF++ refer [CRF++ Taku Kudo](https://taku910.github.io/crfpp/)

    
    MIT License

Copyright (c) 2018 ICFOSS

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

