import requests
from bs4 import BeautifulSoup
import yagmail

# Pull recent headlines from mountain project forums and then email those headlines
# with links to the forums to a user
URL = "https://www.mountainproject.com/"
page = requests.get(URL)

file = open("mpResults.txt", "w")

soup = BeautifulSoup(page.content, 'html.parser')

cont = soup.find(id='recent-forums')


headlines = cont.find_all('div', class_='forum-row')




for headline in headlines:
    # print(headline)
    topic = headline.find('a', class_='topic')
    link = headline.find('a')['href']
    # location_elem = job_elem.find('div', class_='location')
    #if None in (title_elem, company_elem, location_elem):
    #  continue
    file.write(topic.text.strip() + "\n")
    file.write(link.strip() + "\n")
    # print(location_elem.text.strip())
    file.write("\n")

file.close()

receiver = "receiver@gmail.com"
body = ""
filename = "mpResults.txt"

yag = yagmail.SMTP(user="user@gmail.com", password="userpassword")
yag.send(
    to=receiver,
    subject="Mountain Project Headlines",
    contents=body,
    attachments=filename
)
