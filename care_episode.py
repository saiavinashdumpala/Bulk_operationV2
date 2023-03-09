def care_episode(clinicId,therapist_id,patient_id,token,env_url):
  import requests
  from datetime import datetime
  from configparser import ConfigParser

  configuration = ConfigParser()
  configuration.read('config.ini')

  condition = configuration.get('care_episode','condition')
  url = configuration.get('urls','care_episode_url')

  today = datetime.now().isoformat()[:-3]+'Z'
  model = {
  "clinicId": clinicId,
  "condition": condition,
  "startDate": today,
  "therapistId": therapist_id
  }

  api_url = env_url + url + patient_id + "/careepisode"
  tk = token
  headers = {
  "accept" : "application/json",
  "Authorization": str(tk)
  }
  response = requests.post(api_url,headers=headers,json = model,verify=True)