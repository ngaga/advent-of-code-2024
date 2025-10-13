import requests
import os

url = "https://adventofcode.com/2024/day/1/input"
# Get session from environment variable
my_session = os.getenv('ADVENT_OF_CODE_SESSION')
if not my_session:
    print("Error: ADVENT_OF_CODE_SESSION environment variable not set. Please check your .env file.")
    exit(1)
cookies = {'session': my_session}

# Make request with session cookies
response = requests.get(url, cookies=cookies)

print(f"Status Code: {response.status_code}")
print(f"Response: {response}")

if response.status_code == 200:
    print("Connection successful!")
    print(f"Content length: {len(response.text)} characters")
    print(f"First 100 characters: {response.text[:100]}")
else:
    print(f"Error: {response.status_code}")
    print(f"Response content: {response.text}")