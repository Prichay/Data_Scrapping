#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#     This python script will give you the names of the MOVIE    |
#     along with the year in which they received awards, the     |
#     number of awards they won and nomination counts.           |
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#     Important term: 'tr' = TAG ROW.                            |
#                     'td' = TAG DATA.                           |
#                     'th' = TAG HEADINGS.                       |
#                     'tbody' = tables or contents are stored    |
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
import numpy as np # Import the library numpy as reference np.
# Numpy is a liberary used for scientific calc.
# WHY: to put the parsed value from lxml into columns and rows of our table.
import pandas as pd # Import library pandas as alias pd.
# this library is responsible for data manipulation and analysis. to read or write a data to an output file
from urllib.request import urlopen # from urllib library use the request sub-lib to import urlopen.
# we areusing this lib only to get the html page in a vriable.
from bs4 import BeautifulSoup # From beautiful soup bs4 import BeautifulSoup.
# this lib is used for the manipulation of html page from web.
import lxml.html as lh #
# This lib is used to convert the html page to a string format.
import requests
# this lib is used to request the web page from internet.
Url = 'https://en.wikipedia.org/wiki/List_of_Academy_Award-winning_films'# URL of our webpage.
Webpage = requests.get(Url)# variable 'Webpage' contain the whole html of our page
string = lh.fromstring(Webpage.content)# convert the html content of our webpage in a readable string format.
tr_data = string.xpath('//tr')# (find, findall, findText functions)archive only the 'tr' TAG content and its data of the parsed document.
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#||| THIS SECTION IS USED TO DETERMINE THE 'CLASS' OF OUR TABLE WHICH WE WILL BE USING TO OPERATE DIFFERENT OPERATIONS ON.                              |
#Table = Webpage.find_all('table')# here we use the find_all function of BS which finds and returns the result containing the TAG which we have given it|
#for table in Table:                                                                                                                                    |
#    print(table.prettify())# again we are using a function od BS to print the parsed html tree of web page in a nicelly formated output.               |
#||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
# AFTER USING ABOVE FUNCTION WE GOT OUR 'CLASS' OF TABEL I.E 'class="wikitable sortable plainrowheaders"'.
#NOW
#define column and row of a list
col=[]# column 
i=0# row
#For each row, store each first element (header) and an empty list
for a in tr_data[0]:# 0 means in the very first column as a heading
    i+=1
    field=a.text_content()# In this step lxml's().text_content helps to find the only text content in a given variable().
    col.append((field,[]))# append the returned text in a column row by row.
    #print ('%d:"%s"'%(i,name)) Uncomment it to see wether we have the column names correct or not
for b in range (1,len(tr_data)):# o is a header, so we will continue from 1
    z = tr_data[b]# consider rows one by one till the last row.
    i=0 # this is for the indexing
    for t in z.iterchildren():# consider all the child values in a this specific 'tr' TAG to get the value
        data=t.text_content()# put the searched value in 'data'
        if i > 0:
            try:
                data = int(data) # change all the value into intiger to save space.
            except:
                pass
        col[i][1].append(data) # write the data in the cloumns row by row
        i+=1 # next index number.
file = {title:column for (title,column) in col}
#|||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||||
#     OK for the next step, as our value for the first column .i.e for names of the movies                     |
#     is quite large and uneven string value. Thats why i have used the orientation and                        |
#     transpose from the panda dict to arrange our value vertical then horizontal.                             |
df = pd.DataFrame.from_dict(file, orient='index')
df1 = df.T
df1.to_csv('Data_Movies_NEW.csv')
