import requests, yaml, getpass
from flask import render_template
from jinja2 import Template, Environment, FileSystemLoader

loader = FileSystemLoader('.')
env = Environment(loader=loader, trim_blocks=True, lstrip_blocks=True)

password = getpass.getpass(prompt="Password:")
res = requests.get('http://10.0.8.10:3080/v2/projects/a08ea215-6343-4bd9-b81d-ffe7963dc7f1/nodes', auth=('jonathan', password))
a = res.json()

template_config = env.get_template('gns3_inv_v2.j2')

render_1 = template_config.render(config = a)

print(str(render_1))

inventory = open("./hosts", "w")
inventory.write(render_1)