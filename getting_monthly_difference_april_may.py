import json
with open(
        "naturalgas.json", "r", encoding="utf-8") as natural_gas_file: 
        natural_gas_production = json.load(natural_gas_file)
        