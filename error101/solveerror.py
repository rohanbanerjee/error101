import requests
from bs4 import BeautifulSoup

def google_search(uri):
    uri = 'https://www.google.com/search?q=' + uri
    raw_result = requests.get(uri)
    soup = BeautifulSoup(raw_result.content)
    
    for a in soup.find_all('a', href=True):
        if a['href'].startswith('/url?q=') and 'webcache.googleusercontent' not in a['href']:
            print(a['href'][7:].split('&sa')[0])


#query = 'tensorflow install error'
#google_search('https://www.google.com/search?q=' + query)