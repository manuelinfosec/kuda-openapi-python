# Kuda Python


This is a lightweight library that works as a connector to [Kuda OpenAPI](https://kudabank.gitbook.io/kudabank/).

- Customizable base URL.
- Response metadata can be displayed.
- Included examples.

  
## Upcoming
- Savings endpoints,
- Example cases,
- HTTP proxy.


## Installation

Coming to PyPi<br />
While the repo is not yet on pip, simply clone this library and add to your project folder.


## Documentation

Coming Soon
  

## Getting started

> - Login to your [Kuda dashboard](https://developer.kuda.com) and generate your apiKey.
> - Load your email and apiKey to the Kuda client (JSON or dotenv is recommended).
> - JWT tokens are automatically generated.


Usage examples:

```python
from kuda import Kuda

# email and apiKey are generated from your Kuda developer dashboard
Kuda = Kuda(email='<email>', apiKey='<liveApiKey>', show_request=True, sandbox=False, base_url="")

# Get bank list
print(Kuda.bank_list())

# Retrieve main account balance
print(Kuda.get_main_account_balance())

# Perform name enquiry
print(Kuda.name_enquiry(2005161838, "090267"))

# Create virtual account
params = {
    'lastName': 'Manuel',
    'firstName': 'Infosec',
    'email': 'manuelinfosec@gmail.cm',
    'phoneNumber': "+2349131103073",
    'trackingRef': Kuda.get_ref(10) # you can generate your trackingReference some other way you choose.
}
  
print(Kuda.create_virtual_account(**params))
```
  

### Kuda OpenAPI Test

[Kuda Test](https://kuda-openapi-uat.kudabank.com/v2) is available too.

To use Kuda OpenAPI on Test, switch to test on your dashboard and copy apiKey (Live apiKey still remains valid):

```python
from kuda import Kuda

# email and apiKey are generated from your Kuda developer dashboard
Kuda = Kuda(email='<email>', apiKey='<testApiKey>', show_request=True, sandbox=False, base_url="")

  

# Get bank list
print(Kuda.bank_list())

# Retrieve main account balance
print(Kuda.get_main_account_balance())

# Perform name enquiry
print(Kuda.name_enquiry(2005161838, "999129"))


# Create virtual account

params = {
    'lastName': 'Manuel',
    'firstName': 'Infosec',
    'email': 'manuelinfosec@gmail.cm',
    'phoneNumber': "+2349131103073",
    'trackingRef': Kuda.get_ref(10) # you can generate your trackingReference some other way you choose.
}

  
print(Kuda.create_virtual_account(**params))
```


### Base URL

If not provided, `base_url` defaults to `https://kuda-openapi.kuda.com/v2` if `sandbox=False`, or `https://kuda-openapi-uat.kudabank.com/v2` if `sandbox=True`.<br/>

Changes to the Kuda OpenAPI URL will reflect in future updates. In the case of late update, it is recommended to pass in the `base_url` parameter.


### Request and Response Metadata

This library provies requests and header data for debugging purposes.

You can display them by initializing the client with `show_request=True` or `show_header=True` respectively:

```python
from kuda import Kuda

# email and apiKey are generated from your Kuda developer dashboard
Kuda = Kuda(email='<email>', apiKey='<liveApiKey>', show_request=True, show_header=True, sandbox=False, base_url="")

# Get bank list
print(Kuda.bank_list())
```

returns:

```python
{'headers': {'User-Agent': 'python-requests/2.27.1', 'Accept-Encoding': 'gzip, deflate', 'Accept': '*/*', 'Connection': 'keep-alive', 'Authorization': 'Bearer <JWT_TOKEN>', 'Content-Length': '77', 'Content-Type': 'application/json'}, 'body': {'data': '<REDACTED>', 'password': ''}}
```

You can also display full response metadata to help in debugging:

```python
Kuda = Kuda(email='<email>', apiKey='<liveApiKey>', show_request=True, sandbox=False, base_url="")

# Get bank list
print(Kuda.bank_list())
```

returns:

```python
{
    "data": "{'serviceType': 'BANK_LIST', 'requestRef': '9903712', 'data': {}}"
}
# <API RESPONSE>
```
> Refer to documentation for respective data types for each fields in the payload
 
If `ClientError` is received, it'll display full header meta information.


### Error

There are 2 types of errors returned from the library:

- `kuda.error.ClientError`

    - This is thrown when server returns `4XX`, it's an issue from client side.

    - It has 3 properties:

        - `status_code` - HTTP status code, e.g. `-404`

        - `error_message` - Server's error message, e.g. `Something went wrong`

        - `header` - Full response header.

- `binance.error.ServerError`

    - This is thrown when server returns `5XX`, it's an issue from server side.


## Contributing 

Contributions are welcome.<br/>

If you've found a bug within this project, please open an issue to discuss what you would like to change.<br/>

If you have any questions, feature requests, or notice any errors with the OpenAPI, please reach out to [Kuda](mailto:openapi@kuda.com), creating a //Skype link and someone will respond.

## Authors
[Manuel](https://twitter.com/manuelinfosec)

## Acknowledgments
[Kuda Bank Team](https://kudabank.com/)
