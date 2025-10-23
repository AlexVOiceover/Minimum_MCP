import requests

def main():
    sentence = input("Enter a sentence to count 'r' letters: ")

    response = requests.post("http://localhost:8000/count_r",
                           json={"sentence": sentence})

    if response.status_code == 200:
        result = response.json()
        print(f"Result: {result['result']}")
    else:
        print(f"Error: {response.status_code}")

if __name__ == "__main__":
    main()