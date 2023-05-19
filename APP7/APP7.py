import requests
from bs4 import BeautifulSoup
import pandas

info = []                                                                                                       

var = requests.get("https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS")
con = var.content
soup = BeautifulSoup(con, "html.parser")
page_no = soup.find_all("a", {"class":"Page"})                                                                      #extracting no. of pages

base_url = "https://pythonizing.github.io/data/real-estate/rock-springs-wy/LCWYROCKSPRINGS/t=0&s="

for i in range(0,int(page_no[-1].text)*10,10):                                                                       #upper limit is the last page no.    
    url = base_url+str(i)+".html"                                                                                    #we see a pattern in the url when we toggle to next page: an increment of 10(t=0&s=0, t=0&s=10....)at the end of the url         
    var = requests.get(url)                                                                                             
    con = var.content
    soup = BeautifulSoup(con, "html.parser")

    div_prop = soup.find_all("div", {"class":"propertyRow"})
    
    #so now we loop through all the pages 

    for i in div_prop:
        d = {}
        d["Price"]=i.find("h4", {"class":"propPrice"}).text.replace(" ","").replace("\n", "")               #extracting price
        d["Address line1"]=i.find_all("span",{"class":"propAddressCollapse"})[0].text                       #extracting address line 1
        d["Address line2"]=i.find_all("span",{"class":"propAddressCollapse"})[1].text                       #extracting address line 2
        try:                                                                                    #we use try since some entries have no bed attribute on webpage. So text method cannot be used with None. 
            d["Beds"]=i.find("span",{"class":"infoBed"}).find("b").text                      
        except:
            d["Beds"]=None
        try:                                                                                    #we use try since some entries have no area attribute on webpage. So text method cannot be used with None. 
            d["Area"]=i.find("span",{"class":"infoSqFt"}).find("b").text                      
        except:
            d["Area"]=None
        try:                                                                                    #we use try since some entries have no fullbath attribute on webpage. So text method cannot be used with None. 
            d["Full Bath"]=i.find("span",{"class":"infoValueFullBath"}).find("b").text                      
        except:
            d["Full Bath"]=None
        try:                                                                                   
            d["Half Bath"]=i.find("span",{"class":"infoValueHalfBath"}).find("b").text                     
        except:
            d["Half Bath"]=None

        for col_grp in i.find_all("div",{"class":"columnGroup"}):                                                                               #there are many div with class columngroup so we iterate
            for c, n in zip(col_grp.find_all("span", {"class":"featureGroup"}), col_grp.find_all("span", {"class":"featureName"})):             #we iterate through all the features under columngroup div
                if "Lot Size" in c.text:
                    d["Lot Size"]=n.text
                else:
                    pass

        info.append(d)

data = pandas.DataFrame(info)
data.to_csv("Property Details.csv")
