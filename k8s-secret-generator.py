import base64
import json
import yaml

# Prompt the user for information
registry_url = input('Enter the registry URL: ')
namespace = input('Enter the namespace where the secret should be created: ')
username = input('Enter your username: ')
password = input('Enter your password: ')

# Generate a base64-encoded auth string for the Docker credentials
auth_string = base64.b64encode(f'{username}:{password}'.encode())

# Create a Docker credentials object
creds = {
  "auths":{
    registry_url:{
      "username":username,
      "password":password,
      "auth":auth_string.decode()
    }
  }
}

# Encode the Docker credentials as a base64 string
encoded_creds = base64.b64encode(json.dumps(creds).encode()).decode()

# Create a Kubernetes secret object
secret = {
  "apiVersion": "v1",
  "kind": "Secret",
  "metadata": {
    "name": "registry-credentials",
    "namespace": namespace
  },
  "type": "kubernetes.io/dockerconfigjson",
  "data": {
    ".dockerconfigjson": encoded_creds
  }
}

# Write the secret to a file
with open('secret.yaml', 'w') as f:
  f.write(yaml.dump(secret))
print("kubectl apply -f secret.yaml")