import requests
import json

def compare_responses(url1: str, url2: str) -> str:
    try:
        response1 = requests.get(url1)
        response2 = requests.get(url2)

        if response1.status_code != response2.status_code:
            return f"{url1} {response1.status_code} not equals {url2} {response2.status_code}"
        
        json1 = response1.json()
        json2 = response2.json()
        
        if json1 != json2:
            return f"{url1} not equals {url2}"

        return f"{url1} equals {url2}"
    
    except Exception as e:
        return f"Error comparing {url1} and {url2}: {e}"

def main(file1: str, file2: str):
    with open(file1) as f1, open(file2) as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()
        num_lines = min(len(lines1), len(lines2))

        for i in range(num_lines):
            url1 = lines1[i].strip()
            url2 = lines2[i].strip()

            result = compare_responses(url1, url2)

            if "equals" in result:
                print(result)
            else:
                print(result)
                print()

file1 = "file1.txt"
file2 = "file2.txt"

with open(file1) as f1, open(file2) as f2:
    urls1 = f1.readlines()
    urls2 = f2.readlines()

    for url1, url2 in zip(urls1, urls2):
        url1 = url1.strip()
        url2 = url2.strip()
        compare_responses(url1, url2)
