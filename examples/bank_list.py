from kuda import Kuda
from kuda.error import ClientError

email = ""
apiKey = ""

Kuda = Kuda(email, apiKey, 
                sandbox=False,
                show_request=False,
                show_header=False)

banks = Kuda.bank_list()['data']['Data']['banks']
banks = json.dumps(banks, indent=4)

print(banks)