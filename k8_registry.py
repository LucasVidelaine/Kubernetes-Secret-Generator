import base64

registry = input("Registry URL : ")
namespace = input("Namespace : ")
username = input("Username : ")
password = input("Password : ")
email = input("Email : ")
print("-----------------------------------")
userpass = username+":"+password
basic_auth = base64.b64encode(userpass.encode("utf-8")).decode("utf-8")
print(basic_auth)
print("-----------------------------------")
dockerconfigjson = """
{
    "auths": {
        \""""+registry+"""\":{
            "username":\""""+username+"""\",
            "password":\""""+password+"""\",
            "email":\""""+email+"""\",
            "auth":\""""+basic_auth+"""\"
        }
    }
}
"""
print(dockerconfigjson)
print("-----------------------------------")
output = base64.b64encode(dockerconfigjson.encode("utf-8")).decode("utf-8")
print("""
apiVersion: v1
kind: Secret
metadata:
  name: registry-credentials
  namespace: """+ namespace +"""
type: kubernetes.io/dockerconfigjson
data:
  .dockerconfigjson: """ + output)
print("-----------------------------------")
print("kubectl apply -f registry-credentials.yaml")
