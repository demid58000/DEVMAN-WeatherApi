import requests

url_sanfr = 'https://wttr.in/san%20francisco?nTqM&lang=ru'

url_london = 'https://wttr.in/london?nTqM&lang=ru'

url_sheremetievo = 'https://wttr.in/svo?nTqM&lang=ru'

url_cherepovetz = 'https://wttr.in/Череповец?nTqM&lang=ru'

response_cherepovetz = requests.get(url_cherepovetz)
response_cherepovetz.raise_for_status()

response_sheremetievo = requests.get(url_sheremetievo)
response_sheremetievo.raise_for_status()

response_london = requests.get(url_london)
response_london.raise_for_status()

response = requests.get(url_sanfr)
response.raise_for_status()

print(response_cherepovetz.text)
print(response_sheremetievo.text)
print(response.text)
print(response_london.text)