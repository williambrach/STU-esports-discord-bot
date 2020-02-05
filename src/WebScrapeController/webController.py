import requests


def isStubaPerson(msg):
    url = "https://is.stuba.sk/uissuggest.pl"
    name = str(msg.content)
    print(name)
    payload = "_suggestKey=" + name + "&upresneni_default=aktivni_a_preruseni%2C%2Czamestnanci%2Cexterniste%2Cabsolventi&_suggestMaxItems=25&subjekt=21010&subjekt=21020&subjekt=21030&subjekt=21040&subjekt=21050&subjekt=21060&subjekt=21070&subjekt=21900&subjekt=21940&subjekt=21950&subjekt=21960&subjekt=21970&subjekt=21980&upresneni=aktivni_a_preruseni&upresneni=absolventi&upresneni=zamestnanci&upresneni=externiste&vzorek=&_suggestHandler=lide&lang=undefined"
    headers = {
        'Content-Type': "application/x-www-form-urlencoded",
        'cache-control': "no-cache",
        'Postman-Token': "d1c4d891-9cb2-4df9-9d98-e6a420598886"
    }
    response = requests.request("POST", url, data=payload, headers=headers)
    ## TODO pridat filter na gramtiku
    for person in response.json()['data'][0]:
        if name in person:
            return True

    return False
