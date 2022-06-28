import time
import openapi_client
from openapi_client.rest import ApiException
from pprint import pprint


configuration = openapi_client.Configuration(
    host = "https://api.blockchain.com/v3/exchange",
    api_key = {
        'X-API-Token': 'YOUR_API_KEY'
    }

configuration.api_key_prefix['X-API-Token'] = 'Bearer'
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.PaymentsApi(api_client)
    create_withdrawal_request = openapi_client.CreateWithdrawalRequest() # CreateWithdrawalRequest |

    try:
        # Request a withdrawal
        api_response = api_instance.create_withdrawal(create_withdrawal_request)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling PaymentsApi->create_withdrawal: %s\n" % e)


