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
			path= '/home/sid/icfoss/final_scrap/'
			
			for t in links:
					    txt+=t.text
			
			filename=path+"sai"+".utf8"	
			f=codecs.open(str(filename),'a','utf-8')
			f.write(""+txt+"")
	else:
		print("error")
		
def main():
		print("enter the link\n")
		ll=raw_input()
		getdata(ll)
		

if __name__=="__main__":
	main()
