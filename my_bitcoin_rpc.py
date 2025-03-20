import requests
import json
from base64 import b64encode

rpc_user = "charity"
rpc_password = "1@Wanjiku"
rpc_host = "127.0.0.1"
rpc_port = "38332"  # Ensure this is the correct port for Signet

rpc_url = f"http://{rpc_host}:{rpc_port}/"
auth = b64encode(f"{rpc_user}:{rpc_password}".encode()).decode()
headers = {"Authorization": f"Basic {auth}", "Content-Type": "application/json"}

# Test by getting blockchain info
payload = {"jsonrpc": "2.0", "id": "1", "method": "getblockchaininfo", "params": []}
response = requests.post(rpc_url, data=json.dumps(payload), headers=headers)

if response.status_code == 200:
    print("Bitcoin Node Connected Successfully!")
    print(response.json())
else:
    print("RPC Connection Failed!")
    print(response.text)
