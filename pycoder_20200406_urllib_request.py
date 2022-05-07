from urllib.error import HTTPError, URLError
from urllib.request import urlopen, Request
from pprint import pprint
import certifi
import ssl

url = "https://www.example.com"
with urlopen(url) as response:
    body = response.read()
    pass

print(f"1) Let's open {url} and read it's body's first 15 characters:\n{body[:15]}")
print(f"Looks like it is a binary html file.")
print(f"Let's pretty print the response using the dir function  (it's big):")
# input("Press Enter to continue...")
pprint(dir(response))
print(f"I guess those are methods and properties?")

print(f"\nWe can look at all the headers in the response:")
pprint(response.headers.items())
print("\nand quickly request a particular header like 'connection':")
pprint(response.getheader("Connection"))

character_set = response.headers.get_content_charset()
decoded_body = body.decode(character_set)
print(f"\nLet's look at first 50 characters of the body decoded as {character_set}:")
pprint(decoded_body[:50])

with open("save_example_ok_to_delete.html", mode="wb") as html_file:
     html_file.write(body)

import json
url = "https://jsonplaceholder.typicode.com/todos/1"
with urlopen(url) as response:
    body = response.read()

    todo_item = json.loads(body)
    print(f"\n2) Here we open a url which has a json file {url} which we can also"
    f"read and load in python as a json file:\n{todo_item}")

print("\nNow we're going to look at error handling.")

def make_request(url, headers=None):
    request = Request(url, headers=headers or {})
    try:
#        with urlopen(url, timeout=10) as response:  Simpler version, request can contain info
#                                                    necessary to get a good response.
        with urlopen(request, timeout=10) as response: # request version of urlopen
            print(response.status)
            return response.read(), response
    except HTTPError as error:
        print("HTTPError:", error.status, error.reason)
    except URLError as error:
        print("URLError", error.reason)
    except TimeoutError:
        print("Request timed out")

#url = "https://httpstat.us/403"
url = "https://www.httpbin.org/user-agent"
header = {"User-Agent": "Real Python"}

body, request = make_request(url, header)
print(body, request)

url = "https://superfish.badssl.com/"
print(f"Ok let's access a bad certificate url: {url}")
make_request(url, header)

certifi_context = ssl.create_default_context(cafile=certifi.where())
header.append("context": certifi_context)
make_request(url, header)