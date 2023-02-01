from bs4 import BeautifulSoup
import requests

html_text = requests.get('https://dsebd.org/dseX_share.php').text
soup= BeautifulSoup(html_text, 'lxml')
table = soup.find('div', class_='table-responsive')
table = table.text.replace('</a> </td> <td width="10%"> ' , ' ')
print(table)


##write to file
with open('data.txt', 'w') as f:
    f.write(table)



