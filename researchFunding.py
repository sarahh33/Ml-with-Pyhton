#Here is my first time data getting:

#get the data from the server
#Here the data is from Computer Science Department, Aalto
import requests
import lxml.html as lh
import pandas as pd

url='https://akareport.aka.fi/ibi_apps/WFServlet?ekaLataus=0&IBIF_ex=x_RahPaatYht_report2&UILANG=en&SANAHAKU=&ETUNIMI=&SUKUNIMI=&SUKUPUOLI=FOC_NONE&HAKU=FOC_NONE&ORGANIS=Aalto+University&TUTKDI=1170&TMK=FOC_NONE&PAATVUOSI_A=2001&PAATVUOSI_L=2020&LAJITTELU=PAATOS&TULOSTE=HTML'
page = requests.get(url)
doc = lh.fromstring(page.content)
tr_elements = doc.xpath('//tr')

#clean and select my data

allInfo= []
professor= []
funding = []

for elements in tr_elements[14:]:#except head
    if len(elements) == 7:
        allInfo.append(elements)
        col=[]
        i=0
        for t in elements:
            i+=1
            name=t.text_content()
            #print ('%d:"%s"'%(i,name))
            col.append((name,[]))
            if i == 1:
                professor.append(col[0][0].lstrip())
            elif i ==7 :
                funding.append(col[6][0].lstrip())
                
for i in range(len(funding)):
    print("Author: %s \nFunding: %s \n"%(professor[i] ,funding[i]))  
