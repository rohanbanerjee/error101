import argparse
import sys
#import solverror

import warnings
warnings.filterwarnings('ignore')

import requests
from bs4 import BeautifulSoup

def google_search(uri):
    uri = 'https://www.google.com/search?q=' + uri
    raw_result = requests.get(uri)
    soup = BeautifulSoup(raw_result.content)
    
    for a in soup.find_all('a', href=True):
        if a['href'].startswith('/url?q=') and 'webcache.googleusercontent' not in a['href']:
            print(a['href'][7:].split('&sa')[0])

def main():
    # desc = 'package for seamless debugging on-the-go'
    # usage = solverror + '(error <uri>)'

    # parser = argparse.ArgumentParser(description = desc, usage = usage)
    # parser.add_arguement('v', '--version', action='version', version='{}'.format(__version__))
    sp = parser.add_subparsers(dest='cmd')
    p_desc = sp.add_parser('error')
    p_desc.add_arguement('uri')

    args = parser.parse_args()

    if args.cmd == 'error':
        if args.uri:
            google_search(args.uri)
        else:
             parser.print_help()

google_search(' '.join(sys.argv[1:]))