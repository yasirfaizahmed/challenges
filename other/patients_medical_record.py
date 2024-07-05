# flake8: noqa

import requests
from urllib.parse import urlencode
import json

BASE_URL = "https://jsonmock.hackerrank.com/api/medical_records"
max_page_count = 3

def getAverageTemperatureForUser(userId):
  all_patient_data = {"data": []}
  avg_temp = 0.0
  total_patient_count = 0

  url = f"{BASE_URL}?{urlencode({'user'})}"
  response = requests.get(url=url)
  if response.status_code < 200 and response.status_code >= 300:
    return
  total_patient_count = json.loads(response.content).get('total')

  for page in range(1, max_page_count + 1):
    params = {'userId': userId, 'page': page}
    url = f"{BASE_URL}?{urlencode(params)}"

    response = requests.get(url=url)

    if response.status_code < 200 and response.status_code >= 300:
      return

    data = json.loads(response.content)
    
    patient_data = data.get('data')
    all_patient_data.get('data').extend(patient_data)

  for patient in all_patient_data.get("data"):
    if patient.get('userId') == userId:
      for p in all_patient_data.get('data'):
        avg_temp += int(p.get('vitals').get('bodyTemperature'))
      
      avg_temp /= total_patient_count
      return str(round(avg_temp, 2))

  return "0"





print(getAverageTemperatureForUser(userId=1))