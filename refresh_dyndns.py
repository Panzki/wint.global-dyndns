import urllib.request
from secrets import userId, apiKey, domain

refreshUrl = f'https://api.org-dns.com/dyndns/?user={userId}&key={apiKey}&domain={domain}'
print(f'Attempting to refresh dns record by fetching: {refreshUrl}')
response = str(urllib.request.urlopen(refreshUrl).read())
if 'not updated' in response:
    print('[SUCCESS] Dns record already up to date.')
elif 'success' in response and 'record updated' in response:
    print('[SUCCESS] Dns record was successfully updated.')
else:
    print(f'[FAIL] Dns record could not be updated, response is: {response}')