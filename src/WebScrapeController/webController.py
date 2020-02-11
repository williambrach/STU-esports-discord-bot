import requests
import unidecode
import itertools

def isStubaPerson(input):
    url = "https://is.stuba.sk/uissuggest.pl"
    name = ' '.join(input[0:])
    payload = "_suggestKey=" + name + "&upresneni_default=aktivni_a_preruseni%2C%2Czamestnanci%2Cexterniste%2Cabsolventi&_suggestMaxItems=25&subjekt=21010&subjekt=21020&subjekt=21030&subjekt=21040&subjekt=21050&subjekt=21060&subjekt=21070&subjekt=21900&subjekt=21940&subjekt=21950&subjekt=21960&subjekt=21970&subjekt=21980&upresneni=aktivni_a_preruseni&upresneni=absolventi&upresneni=zamestnanci&upresneni=externiste&vzorek=&_suggestHandler=lide&lang=undefined"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "d1c4d891-9cb2-4df9-9d98-e6a420598886"
    }
    listInput = []
    for x in input:
        listInput.append(x)
    listOfPermutations = []
    for x in list(itertools.permutations(listInput, len(listInput))):
        listOfPermutations.append(" ".join(x).lower())

    response = requests.request("POST", url, data=payload, headers=headers)
    for person in response.json()['data']:
        unaccented_string = unidecode.unidecode(person[0])
        if unaccented_string.lower() in listOfPermutations:
            return True

    return False
