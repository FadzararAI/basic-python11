import urllib,requests,urllib.error,json
#word = "high"
with urllib.request.urlopen("https://api.dictionaryapi.dev/api/v2/entries/en/high") as url:
	definition = json.loads(url.read().decode())
print(definition[0]['meanings'][0]['definitions'][1]['definition'])