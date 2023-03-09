def get_movement_id(excecise_name,env_url):
  try:
    import requests
    from str_to_dict import str_to_dict
    from configparser import ConfigParser
    
    configuration = ConfigParser()
    configuration.read('config.ini')

    url = configuration.get('urls','movement_url')

    movement_api_url = env_url + url + excecise_name #api url
    headers = {
    "accept" : "application/json"
    }
    response = requests.get(movement_api_url,headers=headers,verify=True)
    data = str_to_dict(response)
    return(data['movementsList'][0])
  except Exception as e:
    print("an error at fetching exercise(movement) details. The exception is :"+e)