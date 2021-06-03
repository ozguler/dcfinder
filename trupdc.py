import pandas as pd
import socket
import requests

df = pd.read_csv("suptr2.csv")
ip_list = []
dc_name = []
i=1
ripe_base = "https://rest.db.ripe.net/search.json?query-string="


def hostname_resolver(hostname):
    try:
        socket.gethostbyname(web_url)
        return socket.gethostbyname(web_url)
    except socket.error:
        return 0

def ripe_querier(ip_add):
    query_string = ripe_base + str(ip_add)

    response = requests.get(query_string)
    if response.json().get("objects"):
#    if (response.json()['objects']['object'][0]['attributes']['attribute'][1]['value']):
        dc_name = response.json()['objects']['object'][0]['attributes']['attribute'][1]['value']
        return dc_name
    else:
        return 0

for web_url in df['Links']:
#    df['ip_address'] = hostname_resolver(web_url)
#    ip_list.append(hostname_resolver(web_url))
#    print(i, web_url, hostname_resolver(web_url))
    ip_add = hostname_resolver(web_url)
#    print(i, web_url, ip_add, ripe_querier(ip_add))
    dc_name.append(ripe_querier(ip_add))
    i=i+1

df['DC'] = dc_name
df.to_csv("output.csv")
