import json

usuarios={}
usuarios={
    "Chaves":["Chaves Silva","17/06/2017","Recep_01"],
    "Quico":["Enrico Flores","03/06/2017","Raiox_02"]
    }
with open("bd1.json","w")  as arq_json:
      json.dump(usuarios,arq_json)