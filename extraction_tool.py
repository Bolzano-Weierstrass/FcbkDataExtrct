#---imports---
import pandas as pd
from bs4 import BeautifulSoup

def export_conv(yourName, conv_num, path):
    
#---params---
    conv_num = str(conv_num)
    url = path + conv_num + ".html"
    page = open(url, encoding="utf8")
    soup = BeautifulSoup(page.read(), 'lxml')

#---functions---

    def title(string):
        return ( 25*'-' + string + 25*'-')

    def getStringParticipants(soup):
        stringClassThread = str(soup.find_all("div", class_="thread"))
        intermediate = stringClassThread.split('</h3>')
        return(intermediate[1]\
               .split('<div class="message">')[0])
    
    def getAllContent(soup):
        all_content = (soup.find_all("p"))
        list_to_pop, k = [], 0
        for i in range(len(all_content)-1):
            if (str(all_content[i]) == "<p></p>") and (str(all_content[i].find_next())[:3] =="<p>"):
                list_to_pop.append(i)
        for j in list_to_pop:
            all_content.pop(j-k)
            k +=1
        all_content = list(map(str, all_content))
        all_content = [x[3:-4] for x in all_content]
        return(all_content)
    
        
#All the metadata
    style_metadata = (soup\
                      .find_all("style"))[0]
    convName_metadata = soup.h3.get_text()
    ppl_metadata = getStringParticipants(soup) + "and " + yourName

#creation of the text of Metadata_%.txt
    final_metadata = title('Conversation Name') + '\n' + convName_metadata +\
        '\n' + title('People Names') + '\n' + ppl_metadata +\
        '\n' + title('Style Tag') + '\n' + str(style_metadata)
        
#All the messages
    allMessages = (soup\
                   .find_all("div", class_="message"))

#All the users
    allUsers = [x.find_all("span", class_="user")[0].get_text() for x in allMessages]

#All the dates
    allDates = [x.find_all("span", class_="meta")[0].get_text() for x in allMessages]

#All the content
    all_content = getAllContent(soup)

#creation of the Pandas DataFrame of Data_%.csv
    df = pd.DataFrame(allUsers, columns =['message_sender'])
    df['message_date'] = allDates
    df['message_content'] = all_content

#---outputs---

    text_file_name =  "Metadata_"+ conv_num +".txt"
    text_file = open(text_file_name, "w")
    text_file.write(final_metadata)
    text_file.close()
    
    csv_name =  "Data_"+ conv_num + ".csv"
    df.to_csv(csv_name, index=False)






























