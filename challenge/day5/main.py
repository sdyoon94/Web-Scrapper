import os
import requests
from bs4 import BeautifulSoup

def get_data() -> list:
  url = "https://www.iban.com/currency-codes"
  result = requests.get(url)
  soup = BeautifulSoup(result.text, "html.parser")
  tbody = soup.find("tbody")
  datas = tbody.find_all("tr")
  country_currency_code = []
  for data in datas:
    tds = data.find_all("td")
    country = []
    for td in tds:
      country.append(td.text)
    if country[2] == "":
      continue
    country_currency_code.append(country)
  return country_currency_code

def get_currency_code(data: list) -> None:
  while True:
    try:
      number = int(input("#: "))
      print(f"You chose {data[number][0].capitalize()}")
      print(f"The currency code is {data[number][2]}")
      break

    except ValueError:
      print("That wasn't a number.")
    except IndexError:
      print("Choose a number from the list.")

os.system("clear")
print("Hello! Please choose select a country by number:")
data = get_data()
for i, k in enumerate(data):
  print(f"# {i} {k[0].capitalize()}")
get_currency_code(data)