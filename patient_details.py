from turtle import clear

def patient_details(email,token,env_url):
  from str_to_dict import str_to_dict
  import requests
  from urllib.parse import quote
  from configparser import ConfigParser
    
  configuration = ConfigParser()
  configuration.read('config.ini')

  url = configuration.get('urls','patient_details_url')

  api_url = env_url + url + quote(email)  # quote is used here to encode symbols like +, etc
  
  tk = token
  headers = {
  "accept" : "application/json",
  "Authorization": str(tk)
  }
  response = requests.get(api_url,headers=headers,verify=True)
  data = str_to_dict(response)
  if str(response) == "<Response [200]>":
    print(data['firstName'],data['lastName']+" : ",end="")
    return(data['id'])
  else:
    return(response)