from movement import get_movement_id
from therapist import therapist
from create_exercise import create_exercise
from patient_details import patient_details
from patient_register import patient_register
from care_episode import care_episode
from configparser import ConfigParser
from urllib.parse import quote
import csv

configuration = ConfigParser()
configuration.read('config.ini')

therapist_email = configuration.get('default','therapist_email')
token =  configuration.get('auth','token')
env =  configuration.get('environment','env')
env_url = configuration.get('environment_list', env)

try:
# getting ClinicNpiId from therapist details
  therapist_details  = therapist(quote(therapist_email),token,env_url)

  # getting the list of movement Ids for the exercises in a csv file
  file  =  configuration.get('file','filename') 
  fields = []
  rows = []
  patient_email = []
  with open(file, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
      if row != []:
        rows.append(row)
        try:
          ## get patient details
          patient_info = patient_details(str(row[1]),token,env_url) # row[1] -> patient email
          if str(patient_info) == "<Response [400]>": # check if patient is not registered
            try:
              patient_register(therapist_details['therapistClinics'][0]['clinicId'],str(row[1]),therapist_email,therapist_details['id'],token,env_url) # row[1] -> patient email 
              patient_id = patient_details(str(row[1]),token,env_url)

              try:
                # to create a care episode for patient registered
                care_episode(therapist_details['therapistClinics'][0]['clinicId'],therapist_details['id'],patient_id,token,env_url)

                try:
                  # to create an exercise for a patient
                  create_exercise(therapist_email,token,therapist_details,get_movement_id(row[0],env_url),patient_id,env_url) # row[0] -> Exercise name 
                except Exception as e:
                  print("an error at creating an exercise after registering the patient. The exception is :" + e)
                

              except Exception as e:
                print("an error at creating a care episode. The exception is :" + e)
                

            except Exception as e:
              print("an error at registering a patient. The exception is :" + e)
          
          else:  
            patient_id = patient_info
            try:
              # to create an exercise for a patient
              create_exercise(therapist_email,token,therapist_details,get_movement_id(row[0],env_url),patient_id,env_url) # row[0] -> Exercise name
            except Exception as e:
              print("an error at creating an exercise. The exception is :" + e)
          

        except Exception as e:
          print("an error at requesting patient details. The exception is :",e )
          print("Try checking out the csv file for correct format")


except Exception as e:
  print("an error at requesting thearapist details. The exception is :",e )
  print("Try replacing the token in config file")
