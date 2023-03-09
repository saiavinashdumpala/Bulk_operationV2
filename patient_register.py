from operator import mod
from re import purge

def patient_register(clinicId,patient_email,therapist_email,therapist_id,token,env_url):
  import requests
  import uuid
  from datetime import datetime
  from datetime import timedelta
  from datetime import datetime
  from configparser import ConfigParser
  import names

  f_name = names.get_first_name()
  l_name = names.get_last_name()
  # print(f_name,l_name)

  configuration = ConfigParser()
  configuration.read('config.ini')

  url = configuration.get('urls','patient_register_url')
  purpose = configuration.get('patient_register','purpose')
  # dob = (datetime.now() - timedelta(days=20*365)).isoformat()
  today = datetime.now().isoformat()[:-3]+'Z'

  # "2022-08-03T14:10:29.470Z"
  # "2022-08-03T19:36:21.329943"
  model = {
    "clinicId": clinicId,
    "dateOfBirth": "",
    "email": patient_email,
    "emrId": str(uuid.uuid4()),
    "firstName": f_name,
    "gender": "",
    "lastName": l_name,
    "pta": {
      "id": therapist_id,
      "startDate": today
    },
    "purpose": purpose,
    "rtm": 'true',
    "therapistEmail": therapist_email
  }

  api_url = env_url + url  
  tk = token
  headers = {
  "accept" : "application/json",
  "Authorization": str(tk)
  }
  response = requests.post(api_url,headers=headers,json = model,verify=True)