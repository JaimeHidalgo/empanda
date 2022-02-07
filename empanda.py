from etherscan.contracts import Contract
import json

with open('private.json','r') as key_file:
    key = json.loads(key_file.read())['etherscanKey']


address = '0x348FC118bcC65a92dC033A951aF153d14D945312'

api  = Contract(address=address, api_key= key)
sourcecode = api.get_sourcecode()
print(sourcecode[0]['SourceCode'])
