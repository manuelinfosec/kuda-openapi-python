from kuda import Kuda
from kuda.error import ClientError

email = ""
apiKey = ""

Kuda = Kuda(email, apiKey, 
                sandbox=False,
                show_request=False,
                show_header=False)

beneficiaryAccountNumber = ""
beneficiaryBankCode = ""
    
name_enquiry = Kuda.name_enquiry(beneficiaryAccountNumber, 
                    beneficiaryBankCode)


    
name = name_enquiry['data']['Data']['BeneficiaryName']
