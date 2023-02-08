from flask import *
from bs4 import BeautifulSoup
import requests



app = Flask(__name__)
if __name__ == '__main__':
    app.run(threaded=True)


@app.route('/', methods=['GET'])

def home_page():
    page = requests.get('https://dsebd.org/dseX_share.php').text
    soup = BeautifulSoup(page, 'lxml')
    table = soup.find('div', class_='table-responsive')
    #table = table.text.replace('</a> </td> <td width="10%"> ' , ' ')
    return render_template('index.html', table=table)


    



