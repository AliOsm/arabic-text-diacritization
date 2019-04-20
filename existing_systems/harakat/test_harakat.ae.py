import json
import requests
import pickle as pkl

# Constants
CONSTANTS_PATH = '../../helpers/constants'
DATASET_PATH = '../../dataset'

with open(CONSTANTS_PATH + '/DIACRITICS_LIST.pickle', 'rb') as file:
  DIACRITICS_LIST = pkl.load(file)

BATCH_LIMIT = 50
USERID = # User ID
KEY = # API Key

def remove_diacritics(content):
  return content.translate(str.maketrans('', '', ''.join(DIACRITICS_LIST)))

lines = open(DATASET_PATH + '/test.txt').readlines()

result = list()
for idx, line in enumerate(lines):
  line = remove_diacritics(line).strip().split()
  new_line = list()
  i = 0
  while i < len(line):
    batch = ' '.join(line[i:i + BATCH_LIMIT])
    
    url = 'http://api.multillect.com/translate/json/1.0/%s?method=translate/api/vocalize&text=%s&sig=%s' % (USERID, batch, KEY)
    response = requests.get(url)
    
    if response == '' or response == None:
      continue
    
    json_data = json.loads(response.text)
    
    if json_data['error'] != None or json_data['result'] == None:
      continue
    
    new_line.append(json_data['result']['text'])
    i += BATCH_LIMIT
  result.append(' '.join(new_line))
  
  print(idx + 1, end='\r')

with open('output.txt', 'w') as file:
  file.write('\n'.join(result))
