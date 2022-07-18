def get_spend_savings_txns(self,
                        trackingRef: int,
                        pageNumber: int,
                        pageSize: int) -> dict:
    serviceType = "RETRIEVE_SPEND_AND_SAVE_TRANSACTIONS"
    return
                        
def create_plain_savings(self,
                        savingsTrackingRef: int,
                        name: str,
                        virtualAccTrackingRef: int) -> dict:
    serviceType = "CREATE_PLAIN_SAVINGS"
    return

def get_plain_savings(self,
                    trackingRef: int) -> dict:
    serviceType = "GET_PLAIN_SAVINGS"
    return

def get_all_customer_plain_savings(self,
                                accountNumber: int) -> dict:
    return

def get_all_plain_savings(self) -> dict:
    return

def update_plain_savings_account(self,
                                trackingRef: int,
                                status: int) -> dict:
    return

def plain_savings_txn(self,
                    trackingRef: int,
                    amount: int,
                    transactionType: str,
                    narration: str = "") -> dict:
    serviceType = "PLAIN_SAVINGS_TRANSACTIONS"
    return

def plain_savings_txn_logs(self,
                        trackingRef: int,
                        pageSize: int,
                        pageNumber: int) -> dict:
    serviceType = "RETRIEVE_PLAIN_SAVINGS_TRANSACTIONS"
    return

def create_open_flexible_savings(self,
                        savingsTrackingRef: str,
                        name: str,
                        virtualAccTrackingRef: str,
                        amount: int,
                        duration: int,
                        frequency: int,
                        startNow: str,
                        startDate: str = True,
                        isInterestEarning: bool = True) -> dict:
    serviceType = "CREATE_OPEN_FLEXIBLE_SAVE"
    return

def create_closed_flexible_save(self,
                        savingsTrackingRef: str,
                        name: str,
                        virtualAccTrackingRef: str,
                        amount: int,
                        duration: int,
                        frequency: int,
                        startDate: str,
                        startNow: bool = True,
                        isInterestEarning: bool = True) -> dict:
    serviceType = "CREATE_CLOSED_FLEXIBLE_SAVE"
    return

def get_open_flexible_save(self,
                        trackingRef: int) -> dict:
    serviceType = "GET_OPEN_FLEXIBLE_SAVE"
    return

def get_closed_flexible_savings(self,
                        trackingRef: int) -> dict:
    serviceType = "GET_CLOSED_FLEXIBLE_SAVE"
    return

def get_all_customer_open_flexible_savings(self,
                                    primaryAccountNumber: int) -> dict:
    serviceType = "GET_ALL_CUSTOMER_OPEN_FLEXIBLE_SAVE"
    return

def get_all_customer_closed_flexible_savings(self,
                                    primaryAccountNumber: int) -> dict:
    serviceType = "GET_ALL_CUSTOMER_CLOSED_FLEXIBLE_SAVE"
    return

def get_all_open_flexible_savings(self) -> dict:
    serviceType = "GET_ALL_OPEN_FLEXIBLE_SAVE"
    return

def get_all_closed_flexible_savings(self) -> dict:
    serviceType = "GET_ALL_CLOSED_FLEXIBLE_SAVE"
    return

def withdraw_open_flexible_savings(self) -> dict:
    serviceType = "COMPLETE_OPEN_FLEXIBLE_SAVE_WITHDRAWAL"
    return

def withdraw_closed_flexible_savings(self) -> dict:
    serviceType = "COMPLETE_CLOSED_FLEXIBLE_SAVE_WITHDRAWAL"
    return

def open_flexible_savings_txn_logs(self,
                                trackingRef: int,
                                pageSize: int,
                                pageNumber: int) -> dict:
    serviceType = "RETRIEVE_OPEN_FLEXIBLE_SAVINGS_TRANSACTIONS"
    return

def closed_flexible_savings_txn_logs(self,
                                trackingRef: int,
                                pageSize: int,
                                pageNumber: int) -> dict:
    serviceType = "RETRIEVE_CLOSED_FLEXIBLE_SAVINGS_TRANSACTIONS"
    return

def create_fixed_savings(self,
                        savingsTrackingRef: int,
                        name: str,
                        virtualAccTrackingRef: int,
                        amount: int,
                        duration: int,
                        startDate: str,
                        startNow: bool = True,
                        isInterestEarning: bool = True) -> dict:
    serviceType = "CREATE_FIXED_SAVINGS"
    return

def get_fixed_savings(self,
                    trackingRef: int) -> dict:
    serviceType = "GET_FIXED_SAVINGS"
    return

def get_all_customer_fixed_savings(self,
                                primaryAccountNumber: int) -> dict:
    serviceType = "GET_ALL_CUSTOMER_FIXED_SAVINGS "
    return

def get_all_fixed_savings(self) -> dict:
    serviceType = "GET_ALL_FIXED_SAVINGS"
    return

def terminate_fixed_deposit(self,
                            trackingRef: int,
                            amount: int) -> dict:
    """Terminate a fixed deposit

    https://kudabank.gitbook.io/kudabank/savings/fixed-deposit/terminate-a-fixed-deposit

    Args:
        trackingRef (int)
        amount (int)

    Returns:
        dict
    """
    serviceType = "COMPLETE_FIXED_SAVINGS_WITHDRAWAL"

    data = {
        "trackingReference" : trackingRef,
        "amount" : amount
    }
    
    return self.sign_request(serviceType, data)

def fixed_savings_txn_logs(self,
                        trackingRef: int,
                        pageSize: int = 10,
                        pageNumber: int = 1) -> dict:
    """View all transactions on a fixed savings account

    https://kudabank.gitbook.io/kudabank/savings/fixed-deposit/view-all-transactions-on-a-fixed-savings-account

    Args:
        trackingRef (int)
        pageSize (int, optional): Defaults to 10
        pageNumber (int, optional): Defualts to 1

    Returns:
        dict
    """
    serviceType = "RETRIEVE_FIXED_SAVINGS_TRANSACTIONS"
    
    data = {
        "trackingReference" : trackingRef,
        "pageSize": pageSize,
        "pageNumber" : pageNumber
    }
    return self.sign_request(serviceType, data)