<<<<<<< HEAD
import requests
import base64
import json

# Configure your issuer, client, and user credentials
issuer = "https://cxone.niceincontact.com"
client_id = " your client id"  
client_secret = "your client secret"  
access_key = "generated from CXone user with API RBAC"  
access_key_secret = "generated from CXone user with API RBAC"  


# Specific parameters
skill_id = "VCC skill id" #create a new skill just for this use-case
script_path = "User\KSI\myscript" #not a real script yet
parameters = "value1|value2|value3" #supports up to 20 parameters

# Discover the appropriate auth token endpoint
auth_discovery_endpoint = f"{issuer}/.well-known/openid-configuration"
oidc_discovery = requests.get(auth_discovery_endpoint).json()
token_endpoint = oidc_discovery['token_endpoint']

# Encode client_id and client_secret for Basic Auth
auth_string = f"{client_id}:{client_secret}"
auth_encoded = base64.b64encode(auth_string.encode()).decode()

# OAuth2 request requires URL encoding of input parameters
key_public_encoded = requests.utils.quote(access_key)
key_private_encoded = requests.utils.quote(access_key_secret)
body = f"grant_type=password&username={key_public_encoded}&password={key_private_encoded}"

# Headers for the token request
auth_headers = {
    'Authorization': f'Basic {auth_encoded}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Generate REST API call to retrieve Token
auth_response = requests.post(token_endpoint, headers=auth_headers, data=body)
try:
    auth_response.raise_for_status()  # Raise an exception for HTTP errors
    auth_response_json = auth_response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
    print(f"Response content: {auth_response.text}")
    exit()
except json.JSONDecodeError:
    print("Failed to decode JSON response")
    print(f"Response content: {auth_response.text}")
    exit()

myAuthToken = auth_response_json.get('access_token')

if myAuthToken is None:
    print("Failed to retrieve access token")
    print(f"Response content: {auth_response_json}")
    exit()

# Construct the start script URL with query parameters
start_script_url = (
    f"https://api-b32.nice-incontact.com/incontactapi/services/v31.0/scripts/start"
    f"?skillId={skill_id}&scriptPath={requests.utils.quote(script_path)}&Parameters={requests.utils.quote(parameters)}"
)

# Headers for the script request
script_headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {myAuthToken}'
}

# Start the script
script_response = requests.post(start_script_url, headers=script_headers, data='')
try:
    script_response.raise_for_status()  # Raise an exception for HTTP errors
    print("Script Start Response Status Code:", script_response.status_code)
    try:
        print("Script Start Response Content:", script_response.json())
    except json.JSONDecodeError:
        print("Failed to decode JSON response for script start")
        print(f"Response content: {script_response.text}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred while starting the script: {e}")
    print(f"Response content: {script_response.text}")
except Exception as e:
=======
import requests
import base64
import json

# Configure your issuer, client, and user credentials
issuer = "https://cxone.niceincontact.com"
client_id = " your client id"  
client_secret = "your client secret"  
access_key = "generated from CXone user with API RBAC"  
access_key_secret = "generated from CXone user with API RBAC"  


# Specific parameters
skill_id = "VCC skill id" #create a new skill just for this use-case
script_path = "User\KSI\myscript" #not a real script yet
parameters = "value1|value2|value3" #supports up to 20 parameters

# Discover the appropriate auth token endpoint
auth_discovery_endpoint = f"{issuer}/.well-known/openid-configuration"
oidc_discovery = requests.get(auth_discovery_endpoint).json()
token_endpoint = oidc_discovery['token_endpoint']

# Encode client_id and client_secret for Basic Auth
auth_string = f"{client_id}:{client_secret}"
auth_encoded = base64.b64encode(auth_string.encode()).decode()

# OAuth2 request requires URL encoding of input parameters
key_public_encoded = requests.utils.quote(access_key)
key_private_encoded = requests.utils.quote(access_key_secret)
body = f"grant_type=password&username={key_public_encoded}&password={key_private_encoded}"

# Headers for the token request
auth_headers = {
    'Authorization': f'Basic {auth_encoded}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# Generate REST API call to retrieve Token
auth_response = requests.post(token_endpoint, headers=auth_headers, data=body)
try:
    auth_response.raise_for_status()  # Raise an exception for HTTP errors
    auth_response_json = auth_response.json()
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred: {e}")
    print(f"Response content: {auth_response.text}")
    exit()
except json.JSONDecodeError:
    print("Failed to decode JSON response")
    print(f"Response content: {auth_response.text}")
    exit()

myAuthToken = auth_response_json.get('access_token')

if myAuthToken is None:
    print("Failed to retrieve access token")
    print(f"Response content: {auth_response_json}")
    exit()

# Construct the start script URL with query parameters
start_script_url = (
    f"https://api-b32.nice-incontact.com/incontactapi/services/v31.0/scripts/start"
    f"?skillId={skill_id}&scriptPath={requests.utils.quote(script_path)}&Parameters={requests.utils.quote(parameters)}"
)

# Headers for the script request
script_headers = {
    'accept': 'application/json',
    'Authorization': f'Bearer {myAuthToken}'
}

# Start the script
script_response = requests.post(start_script_url, headers=script_headers, data='')
try:
    script_response.raise_for_status()  # Raise an exception for HTTP errors
    print("Script Start Response Status Code:", script_response.status_code)
    try:
        print("Script Start Response Content:", script_response.json())
    except json.JSONDecodeError:
        print("Failed to decode JSON response for script start")
        print(f"Response content: {script_response.text}")
except requests.exceptions.HTTPError as e:
    print(f"HTTP error occurred while starting the script: {e}")
    print(f"Response content: {script_response.text}")
except Exception as e:
>>>>>>> cb17b698911e173c32317f99d1c00bad67effa02
    print(f"An unexpected error occurred: {e}")