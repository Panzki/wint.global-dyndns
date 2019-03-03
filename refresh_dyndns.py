import urllib.request, argparse

def parseArguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--userId", type=str, required=True, help="Your wint.global user id.")
    parser.add_argument("-k", "--apiKey", type=str, required=True, help="Your wint.global api password.")
    parser.add_argument("-d", "--domain", type=str, required=True, help="Your wint.global domain that will be updated.")
    arguments = parser.parse_args()

    return (arguments.userId, arguments.apiKey, arguments.domain)

if __name__ == "__main__":
    userId, apiKey, domain = parseArguments()
    refreshUrl = f'https://api.org-dns.com/dyndns/?user={userId}&key={apiKey}&domain={domain}'
    print(f'Attempting to refresh dns record by fetching: {refreshUrl}')
    
    response = str(urllib.request.urlopen(refreshUrl).read())
    if 'not updated' in response:
        print('[SUCCESS] Dns record already up to date.')
    elif 'success' in response and 'record updated' in response:
        print('[SUCCESS] Dns record was successfully updated.')
    else:
        print(f'[FAIL] Dns record could not be updated, response is: {response}')