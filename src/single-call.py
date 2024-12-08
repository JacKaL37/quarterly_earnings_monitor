import requests 

ticker="AAPL"
quarter="Q1"
year=2024

response = requests.get(
        f"https://discountingcashflows.com/api/transcript/{ticker}/{quarter}/{year}/",
        auth=("user", "some kinda secret key guy eyyyy (go get your api key)"),
    )


print(response)
print(response.text)