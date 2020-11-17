import requests
import json

upgrades = {}


from v_029 import Upgrade as u_029
from v_03 import Upgrade as u_03

upgrades.update(u_029().upgrades)
upgrades.update(u_03().upgrades)

resultado = str(json.dumps(upgrades, indent=4))

with open('upgrades.json', 'w', encoding='utf-8') as file:
    file.write(resultado)

print(resultado)
