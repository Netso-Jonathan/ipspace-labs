import requests, yaml, getpass
from flask import render_template
from jinja2 import Template, Environment, FileSystemLoader

loader = FileSystemLoader('.')
env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

user = input("Enter GNS3 Username: ")
password = getpass.getpass(prompt="Enter GNS3 Password: ")

res = requests.get('http://10.0.8.10:3080/v2/projects', auth=(user, password))
a = res.json()
lab_list= []
print("For which of the following lab do you want to create an ansible inventory")
lab_list= []
for line in a:
    print(line['name'])
    lab_list.append(line['name'])

lab_choice = None
while lab_choice not in lab_list:
    lab_choice = input("Enter lab name: ")

for line in a:
    if lab_choice == line['name']:
        project_id = line['project_id']
        print("GNS3 Project id is : ", project_id)

api_call = "http://10.0.8.10:3080/v2/projects/" + project_id + "/nodes"
res = requests.get(api_call, auth=('jonathan', password))
b = res.json()

template_config = env.get_template('gns3_inv_v2.j2')

render_1 = template_config.render(config = b)

print(str(render_1))

inventory = open("./hosts", "w")
inventory.write(render_1)