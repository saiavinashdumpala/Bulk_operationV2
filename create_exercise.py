from therapist import therapist

def create_exercise(email,token,therapist_details,movement_details,patient_id,env_url):
  import requests
  from datetime import datetime
  from datetime import timedelta
  from configparser import ConfigParser

  configuration = ConfigParser()
  configuration.read('config.ini')

  url = configuration.get('urls','create_exercise_url')

  movement_set = configuration.get('movement','set')
  movement_rest = configuration.get('movement','rest')
  movement_repetition = configuration.get('movement','repetition')

  position_hold = configuration.get('position','hold')
  position_rest = configuration.get('position','rest')
  position_repetition = configuration.get('position','repetition')
# to get default date and time(here default date implies current date and the following date)
  today = datetime.now().isoformat()[:-3]+'Z'
  tomorrow = (datetime.now() + timedelta(days=1)).isoformat()[:-3]+'Z'  
# default vaules
  hold = configuration.get('default','hold')
  repetition = configuration.get('default','repetition')
  rest = configuration.get('default','rest')
  set = configuration.get('default','set')
  frequency = configuration.get('default','frequency')
  per = configuration.get('default','per')
  status = configuration.get('default','status')
# if exercise type is movement
  if movement_details['type'] == "MOVEMENT":
    set = movement_set
    rest = movement_rest
    repetition = movement_repetition
# if exercise type is position
  elif movement_details['type'] == "POSITION":
    hold = position_hold
    rest = position_rest
    repetition = position_repetition

    
    # print(movement_details)

  model = {
      "clinicId": therapist_details['therapistClinics'][0]['clinicId'],
      "exercises": [
        {
          "createdBy":therapist_details['firstName'] + " "+ therapist_details['lastName'],
          "dates": [
            today,
            tomorrow
          ],
          "description":movement_details['description'],
          "frequency": frequency,
          "hold": hold,
          "movementId": movement_details['id'],
          "order": 0,
          "per": per,
          "repetition": repetition,
          "rest": rest,
          "set": set,
          "startDate": today,
          "status": status,
          "statusPeriod": [
            {
              "active": "true",
              "endDate": today,
              "modifiedBy": therapist_details['firstName'] + " "+ therapist_details['lastName'],
              "startDate": today
            }
          ]
        }
      ],
      "patientId": patient_id
    }
  api_url = env_url + url + email
  tk = token
  headers = {
  "accept" : "application/json",
  "Authorization": str(tk)
  }
  response = requests.post(api_url,headers=headers,json = model,verify=True)

  if str(response) == "<Response [400]>":
    print(movement_details['name'],"is already assigned to the patient\n")
  # print(response.content)
  elif str(response) == "<Response [200]>" or str(response) == "<Response [500]>":
    print(movement_details['name'],"is assigned to the patient\n")