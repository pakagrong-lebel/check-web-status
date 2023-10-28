# Python script to check the status of a website
import requests
def check_website_status(url):
    response = requests.get(url)
    if response.status_code == 200:
        # Your code here to handle a successful response
    else:
        # Your code here to handle an unsuccessful response





    