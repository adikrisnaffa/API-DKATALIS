import requests
import json

def compare_json_response(url1, url2):

    response1 = requests.get(url1)
    response2 = requests.get(url2)

    if response1.status_code == response2.status_code:
        json_response1 = json.loads(response1.text)
        json_response2 = json.loads(response2.text)

        if json_response1 == json_response2:
            print(url1, "equals", url2)
        else:
            print(url1, "not equals", url2)
    else:
        print(url1, "status code", response1.status_code, "not equals", url2, "status code", response2.status_code)

def compare_api_responses(file1, file2):

    with open(file1) as f1, open(file2) as f2:
        for line1, line2 in zip(f1, f2):
            url1 = line1.strip()
            url2 = line2.strip()
            compare_json_response(url1, url2)

if __name__ == "__main__":
    file1 = "file1.txt"
    file2 = "file2.txt"
    compare_api_responses(file1, file2)