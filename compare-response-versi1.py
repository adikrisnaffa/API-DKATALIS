import requests
import json

def compare_responses(url1, url2):
    response1 = requests.get(url1)
    response2 = requests.get(url2)

    if response1.status_code != response2.status_code:
        return f"{url1} not equals {url2}"
    
    json1 = json.loads(response1.content)
    json2 = json.loads(response2.content)
    
    if json1 != json2:
        return f"{url1} not equals {url2}"
    
    return f"{url1} equals {url2}"

file1 = 'file1.txt'
file2 = 'file2.txt'

with open(file1) as f1, open(file2) as f2:
    for url1, url2 in zip(f1, f2):
        url1 = url1.strip()
        url2 = url2.strip()
        
        try:
            result = compare_responses(url1, url2)
            print(result)
        except Exception as e:
            print(f"Error comparing {url1} and {url2}: {e}")
