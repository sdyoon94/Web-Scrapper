import requests
import os

def clear():
  os.system("clear")

def replay():
  while True:
    try:
      do = input("Do you want to start over? y/n ")
      if do != "y" and do != "n":
        raise
      else:
        return do
    except:
      print("That's not a valid answer.")

def run(url=[]):
  for i in url:
    i=i.strip()
    if "." not in i:
      print(f"{i} is not a valid URL.")
      continue
    elif "http://" not in i:
      i= "http://" + i
    is_up(i)

def is_up(url=""):
  try:
    rsp=requests.get(url)
    if rsp.status_code == requests.codes.ok:
      print(f"{url} is up!")
    else:
      raise
  except:
    print(f"{url} is down!")

while True:
  print("Welcome to IsItDown.py!")
  print("Please write a URL or URLs you want to check. (separated by comma)")
  urls=input()
  url=urls.split(",")
  run(url)
  if replay() == "y":
    clear()
    continue
  else:
    break;
print("k, bye!")