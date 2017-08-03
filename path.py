import http.client

conn = http.client.HTTPSConnection("64.100.10.234")

payload = "{ \n\t\"sourceIP\": \"10.1.15.117\", \n\t\"destIP\": \"10.1.12.20\" \n\t}"

headers = {
    'x-auth-token': "ST-5-G5fuLwYqaqQZywdRjAyH-cas",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "ecf8d73e-f005-e51b-0176-9577540d0922"
    }

conn.request("POST", "/api/v1/flow-analysis", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
