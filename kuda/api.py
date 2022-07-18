def bank_list(self):
    """The Bank list covered here are for all Nigerian Financial Institutions supported by NIBSS
    https://kudabank.gitbook.io/kudabank/single-fund-transfer/bank-list

    Returns:
        dict
    """
    serviceType = "BANK_LIST"
    return self.sign_request("BANK_LIST")

def name_enquiry(self,
                account_number: int,
                bank_code: str,
                SenderTrackingReference: str = "") -> dict:
    """Validate and retrieve information on a NUBAN account number
    https://kudabank.gitbook.io/kudabank/single-fund-transfer/name-enquiry

    Args:
        account_number (int): Destination Account Number
        bank_code (int): Destination Bank Code. Defaults to Kuda bank code

    Returns:
        dict
    """
    serviceType = "NAME_ENQUIRY"

    if not SenderTrackingReference:
        SenderTrackingReference = ""
        isRequestFromVirtualAccount = "false"
    else:
        isRequestFromVirtualAccount = "true"

    data = {
        "beneficiaryAccountNumber": account_number,
        "beneficiaryBankCode": bank_code,
        "SenderTrackingReference": SenderTrackingReference,
        "isRequestFromVirtualAccount" : isRequestFromVirtualAccount
        }

    return self.sign_request(serviceType, data)

def create_virtual_account(self,
                        lastName: str,
                        firstName: str,
                        email: str,
                        phoneNumber: str,
                        trackingRef: int) -> dict:
            
    """Create a Virtual Account
    https://kudabank.gitbook.io/kudabank/virtual-account-creation#create-a-virtual-account

    Args:
        lastName (str): User's last name
        firstName (str): User's first name
        emailAddress (str): User's email address
        phoneNumber (str): User's phone number
        trackingRef (int): Unique identifier for the account

    Returns:
        dict
    """
    serviceType = "ADMIN_CREATE_VIRTUAL_ACCOUNT"

    data = {
        "email": email, 
        "phoneNumber": phoneNumber, 
        "firstName": firstName, 
        "trackingReference": trackingRef
        }
    
    return self.sign_request(serviceType, data)

def get_virtual_single_account(self,
                            trackingRef: int) -> dict:
    """Retrieve Virtual Account information
    https://kudabank.gitbook.io/kudabank/virtual-account-creation/retrieve-virtual-account

    Args:
        trackingRef (int): Unique Identifier for virtual Account

    Returns:
        dict
    """
    serviceType = "ADMIN_RETRIEVE_SINGLE_VIRTUAL_ACCOUNT"

    data = {
        "trackingReference": trackingRef
    }

    return self.sign_request(serviceType, data)


def single_fund_transfer(self,
                        trackingRef: int,
                        beneficiaryAccountNumber: int,
                        beneficiaryBankCode: int,
                        beneficiaryName: str,
                        amount: int,
                        SenderName: str,
                        narration: str,
                        accountID: int,
                        NameEnquirySessionID: str = None) -> dict:
    """Bank transfer from a Kuda Account to any bank account
    https://kudabank.gitbook.io/kudabank/single-fund-transfer/send-money-from-a-kuda-account

    Args:
        trackingRef (int): Request Reference ID
        beneficiaryAccountNumber (int): Destination bank account number
        beneficiaryBankCode (int): Destination bank code
        beneficiaryName (str): Name of the recipient
        amount (int): Amount to be transferred (in kobo)
        SenderName (str): Name of the person sending money
        narration (str): User defined reason for the transaction.
        accountID (int): Main Account number
        NameEnquirySessionID (str, optional): Session ID generated from the nameEnquiry request. Defaults to None.

    Returns:
        dict
    """
    
    serviceType = "SINGLE_FUND_TRANSFER"
    
    # TODO: Check Request Body
    if not NameEnquirySessionID:
        accountInfo = self.name_enquiry(beneficiaryAccountNumber, beneficiaryBankCode)
        NameEnquirySessionID = accountInfo["data"]["Data"]["SessionID"]
        accountName = accountInfo["data"]["Data"]["BeneficiaryName"]
    else:
        accountInfo = self.name_enquiry(beneficiaryAccountNumber, beneficiaryBankCode)
        NameEnquirySessionID = accountInfo["data"]["Data"]["SessionID"]
        accountName = accountInfo["data"]["Data"]["BeneficiaryName"]

    data = {
      "ClientAccountNumber": accountID, 
      "beneficiarybankCode": beneficiaryBankCode,
      "beneficiaryAccount": beneficiaryAccountNumber,
      "beneficiaryName": accountName,
      "amount": amount,
      "narration": narration,
      "nameEnquirySessionID": NameEnquirySessionID,
      "trackingReference": trackingRef,
      "senderName": SenderName,
    }

    return self.sign_request(serviceType, data)

def virtual_fund_transfer(self,
                    trackingRef: int,
                    beneficiaryAccount: int,
                    amount: int,
                    narration: str,
                    beneficiaryBankCode: int,
                    beneficiaryName: str,
                    senderName: str,
                    nameEnquiryId: str = None) -> dict:

    """Bank transfer from a KUDA Virtual Account to any bank account
    https://kudabank.gitbook.io/kudabank/single-fund-transfer/virtual-account-fund-transfer

    Args:
        trackingRef (int): Unique Identifier for virtual Account
        beneficiaryAccount (int): Destination bank account number
        beneficiaryBankCode (int): Destination bank code
        beneficiaryName (str): Name of the recipient
        amount (int): Amount to be transferred (in kobo)
        narration (str): User defined reason for the transaction.
        SenderName (str): Name of the person sending money
        nameEnquiryId (str, optional): Session ID generated from the nameEnquiry request. Defaults to None.

    Returns:
        dict
    """
    serviceType = "VIRTUAL_ACCOUNT_FUND_TRANSFER"

    # TODO: Check Request Body
    if not nameEnquiryId:
        accountInfo = self.name_enquiry(beneficiaryAccount, beneficiaryBankCode, trackingRef)
        nameEnquiryId = accountInfo["data"]["Data"]["SessionID"]
        accountName = accountInfo["data"]["Data"]["BeneficiaryName"]
    else:
        accountInfo = self.name_enquiry(beneficiaryAccount, beneficiaryBankCode, trackingRef)
        nameEnquiryId = accountInfo["data"]["Data"]["SessionID"]
        accountName = accountInfo["data"]["Data"]["BeneficiaryName"]

    data = {
        "trackingReference": trackingRef,
        "beneficiarybankCode": beneficiaryBankCode,
        "beneficiaryAccount": beneficiaryAccount,
        "beneficiaryName": accountName,
        "amount": amount,
        "narration": narration,
        "nameEnquiryId": nameEnquiryId,
        "senderName": senderName,
    }

    return self.sign_request(serviceType, data)

def txn_status_query(self,
                third_party: bool,
                txnRef: int) -> dict:

    """Retrieve information on a the status of a transaction
    https://kudabank.gitbook.io/kudabank/single-fund-transfer/transactions-query

    Args:
        txnRef (int): Unique identifier for the transfer
        third_party (bool, optional): Does it concern a third-party bank? Defaults to False

    Returns:
        dict
    """

    serviceType = "TRANSACTION_STATUS_QUERY"
    if third_party:
        isThirdPartyBankTransfer = "true"
    else:
        isThirdPartyBankTransfer = "true"

    data = {
        "isThirdPartyBankTransfer": isThirdPartyBankTransfer,
        "transactionRequestReference": txnRef
    }
    return self.sign_request(serviceType, data)

def get_main_account_balance(self) -> dict:

    """Check the balance on your KUDA main account
    https://kudabank.gitbook.io/kudabank/check-admin-account-balance

    Returns:
        dict
    """
    serviceType = "ADMIN_RETRIEVE_MAIN_ACCOUNT_BALANCE"
    return self.sign_request(serviceType)

def get_virtual_account_balance(self,
                            trackingRef: int) -> dict:

    """Retrieve Virtual Account Balance
    https://kudabank.gitbook.io/kudabank/check-virtual-account-balance

    Args:
        trackingRef (int)

    Returns:
        dict
    """
    serviceType = "RETRIEVE_VIRTUAL_ACCOUNT_BALANCE"

    data = {
        "trackingReference": trackingRef
        }

    return self.sign_request(serviceType, data)

def txn_logs(self,
            RequestReference: int,
            ResponseReference: int,
            startDate: str,
            endDate: str,
            txnDate = "",
            HasTransactionDateRangeFilter: bool = False,
            FetchSuccessfulRecords: bool = True,
            pageSize: int = 10,
            pageNumber: int = 1) -> dict:
    
    """Get Transaction Logs

    Args: 
        Refer to documentaion: https://kudabank.gitbook.io/kudabank/view-transaction-history/get-transaction-logs
    
    Returns:
        dict
    """

    serviceType = "RETRIEVE_TRANSACTION_LOGS"

    if HasTransactionDateRangeFilter:
        HasTransactionDateRangeFilter = "true"
    else:
        startDate = txnDate
        endDate = txnDate
        HasTransactionDateRangeFilter = "false"
    
    if FetchSuccessfulRecords:
        FetchSuccessfulRecords = "true"
    else:
        FetchSuccessfulRecords = "false"

    data = {
        "RequestReference": RequestReference,
        "ResponseReference": ResponseReference,
	    "TransactionDate": txnDate,
        "HasTransactionDateRangeFilter": HasTransactionDateRangeFilter,
        "StartDate": startDate,
        "EndDate": endDate,
        "PageSize": pageSize,
        "PageNumber": pageNumber,
        "FetchSuccessfulRecords": FetchSuccessfulRecords
    }
    return self.sign_request(serviceType, data)

def main_txn_logs(self,
                pageSize: int = 10, pageNumber: int = 1) -> dict:
    """Retrieve a list of all transactions for the currently authenticated user.
    https://kudabank.gitbook.io/kudabank/view-transaction-history/kuda-account-transaction-history

    Args:
        pageSize (int)
        pageNumber (int)
    """
    serviceType = "ADMIN_MAIN_ACCOUNT_TRANSACTIONS"

    data = {
        "pageSize" : pageSize,
        "pageNumber" : pageNumber
    }

    return self.sign_request(serviceType, data)

def filter_main_txn_logs(self,
                startDate: str,
                endDate: str,
                pageSize: int = 10,
                pageNumber: int = 1) -> dict:
    """Retrieve a filtered list of all transactions for the currently authenticated user.
    https://kudabank.gitbook.io/kudabank/view-transaction-history/filtered-kuda-account-transaction-history

    Args:
        startDate (str): Ex: 2020-10-27T09:58:23.4740446Z
        endDate (str): Ex: 2020-12-27T09:58:23.4740446Z
        pageSize (int, optional)
        pageNumber (int, optional)

    Returns:
        dict
    """
    serviceType = "ADMIN_MAIN_ACCOUNT_FILTERED_TRANSACTIONS"

    data = {
        "pageSize": pageSize,
        "pageNumber": pageNumber,
        "startDate": startDate,
        "endDate": endDate
    }
    return self.sign_request(serviceType, data)

def virtual_txn_logs(self,
                    trackingRef: int,
                    pageSize: int = 10,
                    pageNumber: int = 1) -> dict:
    """Retrieve a list of all transactions for a specified virtual account
    https://kudabank.gitbook.io/kudabank/view-transaction-history/virtual-accounttransactionhistory

    Args:
        trackingRef (int): Unique Identifier for virtual Account
        pageSize (int, optional)
        pageNumber (int, optional)

    Returns:
        dict
    """
    serviceType = "ADMIN_VIRTUAL_ACCOUNT_TRANSACTIONS"

    data = {
        "trackingReference": trackingRef, 
        "pageSize" : pageSize,
        "pageNumber" : pageNumber,
    }

    return self.sign_request(serviceType, data)

def filter_virtual_txn_logs(self,
                            trackingRef: int,
                            startDate: str,
                            endDate: str,
                            pageSize: int = 10,
                            pageNumber: int = 1) -> dict:
    """Retrieve a filtered list of all transactions for a specified virtual account
    https://kudabank.gitbook.io/kudabank/view-transaction-history/virtual-account-transaction-history

    Args:
        trackingRef (int): Unique Identifier for virtual Account
        startDate (str): Ex: 2020-10-27T09:58:23.4740446Z
        endDate (str): Ex: 2020-12-27T09:58:23.4740446Z
        pageSize (int, optional)
        pageNumber (int, optional)

    Returns:
        dict
    """
    serviceType = "ADMIN_MAIN_ACCOUNT_FILTERED_TRANSACTIONS"
    
    data = {
        "trackingReference": trackingRef,
        "pageSize": pageSize,
        "pageNumber": pageNumber,
        "startDate": startDate,
        "endDate": endDate
    }
    return self.sign_request(serviceType, data)

def fund_virtual_account(self,
                        trackingRef: int,
                        amount: int,
                        narration: str) -> dict:

    """Deposit to a virtual account
    https://kudabank.gitbook.io/kudabank/add-remove-money-from-a-virtual-account

    Args:
        trackingRef (int): Unique Identifier for virtual Account
        amount (int): Amount to fund (in kobo)
        narration (str, optional): Transaction Description. Defaults to "".

    Returns:
        dict:
    """
    serviceType = "FUND_VIRTUAL_ACCOUNT"

    data = {
        "trackingReference": trackingRef,
        "amount": amount,
        "narration": narration
    }
    return self.sign_request(serviceType, data)

def withdraw_virtual_account(self,
                            trackingRef: int,
                            amount: int,
                            narration: str = "") -> dict:
    """Withdrawing funds from a virtual account means to transfer funds from a virtual account to an associated KUDA account or to any other Nigerian Bank account.
    https://kudabank.gitbook.io/kudabank/add-remove-money-from-a-virtual-account#withdraw-from-virtual-account

    Args:
        trackingRef (int): Unique Identifier for virtual Account
        amount (int): Amount to be withdrawn (in kobo)
        narration (str, optional): Transaction description. Defaults to "".

    Returns:
        dict
    """
    serviceType = "WITHDRAW_VIRTUAL_ACCOUNT"

    data = {
        "trackingReference": trackingRef,
        "amount": amount,
        "narration": narration
    }

    return self.sign_request(serviceType, data)