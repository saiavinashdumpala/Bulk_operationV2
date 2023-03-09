def therapist(email,token,env_url):
  import requests
  from str_to_dict import str_to_dict
  from configparser import ConfigParser
    
  configuration = ConfigParser()
  configuration.read('config.ini')

  url = configuration.get('urls','therapist_url')

  therapist_api_url = env_url + url + str(email)
  tk = token
  headers = {
  "accept" : "application/json",
  "Authorization": str(tk)
  }
  response = requests.get(therapist_api_url,headers=headers,verify=True)
  data = str_to_dict(response)
  return (data[0])


