import requests
# import configparser
res = requests.get('http://10.0.8.10:3080/v2/projects/a08ea215-6343-4bd9-b81d-ffe7963dc7f1/nodes', auth=('jonathan', '1J0uriftpn!!'))
a = res.json()

# inventory = configparser.ConfigParser(allow_no_value = True)

for node in a:
 if 'hda_disk_image' in node['properties']:
  image = node['properties']['hda_disk_image']
 else: 
  image = "no Image"
 console = node['name'] + ', ' + node['console_host'] + ', ' + str(node['console']) + ', ' + image 
 print(console)
 print(console)
