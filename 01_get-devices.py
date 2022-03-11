import requests
import json
import urllib3
from device_login import dnac

header = {
    'content-type': "application/json",
    'x-auth-token' : ""
}
requests.packages.urllib3.disable_warnings()

def getToken(host, username, password):    
    url = f"https://{host}/api/system/v1/auth/token"
    response = requests.post(url, auth = (username, password), headers=header, verify=False)
    return response.json()["Token"]

def networkDevices(host, token):    
    url = f"https://{host}/dna/intent/api/v1/network-device"
    header["x-auth-token"] = token
    response = requests.get(url, headers=header, verify=False)
    return response.json()

if __name__ == '__main__':
    token = getToken(dnac["host"],dnac["username"], dnac["password"])
    device_data = networkDevices(dnac["host"], token)
    print("\nBelow are the device deatils : ")
    print("--------------------------------------------------\n")
    for devices in device_data["response"]:
        print(f"  Hostname : {devices['hostname']}")
        print(f"  Family : {devices['family']}")
        print(f"  Series : {devices['series']}")
        print(f"  Serial Number : {devices['serialNumber']}")
        print(f"  Management IP: {devices['managementIpAddress']}")
        print(f"  Platform Type: {devices['platformId']}")
        print(f"  Software Version: {devices['softwareVersion']}")
        print("--------------------------------------------------")
    