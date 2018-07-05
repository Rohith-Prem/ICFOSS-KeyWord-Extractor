import requests
import codecs

from bs4 import BeautifulSoup


def getdata(i):
	url=str(i)
	resp=requests.get(url)
	if resp.status_code==200:
		soup=BeautifulSoup(resp.text,'html.parser')
		links =soup.findAll("p")
		if len(links) != 1:
			txt=soup.findAll("h1")[0].text
			txt+="\n"
			path= 'E:\Work\ICFOSS\ICFOSS-KeyWord-Extractor\Tokenise'
			
			for t in links:
					    txt+=t.text
			
			filename=path+"\scrapped_text"+".utf8"
			f=codecs.open(str(filename),'a','utf-8')
			f.write(""+txt+"")
	else:
		print("error")
		
def main():
		#print("enter the link\n")
		#ll=input()
		url = "http://www.deshabhimani.com/news/kerala/swaminathan-commission-report/735250"
		getdata(url)
		

if __name__=="__main__":
	main()
