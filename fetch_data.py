import os
import django
import requests
import json

#%%

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'poe_project.settings')
django.setup()

import requests
from poe_app.models import Currency

url = 'https://poe.ninja/api/data/currencyoverview?league=Sanctum&type=Currency'

response = requests.get(url)

if response.status_code == 200:
    character_data = response.json()["lines"]
    for character in character_data:
        character_obj = Currency.objects.create(
            name=character['currencyTypeName'],
            chaosEquivalent = character['chaosEquivalent']
        )
        print(f"Created character {character_obj.name}")
else:
    print(f"Failed to retrieve character data. Status code: {response.status_code}")

