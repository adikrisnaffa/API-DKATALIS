import requests

with open('file1.txt') as f1, open('file2.txt') as f2:
    for url1, url2 in zip(f1, f2):
        url1 = url1.strip()
        url2 = url2.strip()
        try:
            response1 = requests.get(url1)
            response2 = requests.get(url2)
            if response1.json() == response2.json():
                print(url1, "equals", url2)
            else:
                print(url1, "not equals", url2)
        except requests.exceptions.RequestException as e:
            print("Error:", e)