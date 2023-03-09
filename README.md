# Bulk_operations
 
## CSV File
The CSV file contains the information of exercise names along with the patient email id.

## Config File
Any other configurations which needs to be changed will be here. There are no changes needed to be done in remaining files.
### Auth
In auth section we need to replace the token which is used for login purpose.
### environment_list
List the envirnoments here
### environment
change the value of env to any one of the above listed environments in the environment_list
### urls
Here all the urls for the different api's are listed 
### default
It has all the default values for the program to run.
The default therapist email is also in this section which can be changed.
### file
The path to the csv file mentioned above should be placed here.
### exercise_types
Here the types of exercises and their default values are to be noted.
### care_episode
Here the condition for creating the care episode is to be noted.
### patient_register
Here the purpose for the patient registration is to be noted.

# Installing Requirements
Use this command for initial setup for installing all the requiremnts "pip install -r  requirements.txt"

# Running the program
Open the command prompt in the file directory.
Use the command "python main.py" to run the program.
