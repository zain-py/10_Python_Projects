import urllib.request as urllib

def main(url):
    
    print('\nChecking Connectivity.')
    
    response = urllib.urlopen(url)
    
    print(f'Connected to "{url}" successfully.\n')
    print(f'The response code was: [{response.getcode()}]')

url = input('Enter the URL of the site: ')

main(url)    
