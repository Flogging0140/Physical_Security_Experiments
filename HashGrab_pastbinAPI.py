import requests

# Set the API endpoint URL
url = "https://pastebin.com/api/api_post.php"

# Set the required parameters for the API call
api_dev_key = "hP986F51fO0JUEVZg64XzLR6otvP8CTu"
api_option = "paste"
api_paste_code = "some rando text"

# Send the POST request to the API endpoint with the UTF-8 encoded data
response = requests.post(url, data={
    "api_dev_key": api_dev_key,
    "api_option": api_option,
    "api_paste_code": api_paste_code.encode("utf-8")
})

# Check the response status code to see if the request was successful
if response.ok:
    # Print the URL of the pastebin post
    print(response.text)
else:
    print("Error: Request failed with status code", response.status_code)
