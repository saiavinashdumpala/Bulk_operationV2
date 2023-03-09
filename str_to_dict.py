def str_to_dict(response):
  import json

  response.json()
  data =  (response.content.decode("utf-8") ) #converting the response from bytes to string
  return(json.loads(data)) #converting string to dictionary