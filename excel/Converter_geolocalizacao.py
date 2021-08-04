from pygeocoder import Geocoder

endereco='1222, Lins de Vasconcelos, São Paulo, SP'
recebe=Geocoder('AIzaSyB4Xtw6R8nndygFV7_f_Y-qrKCyBqxh30A').geocode(endereco)



endereco=input("Digite um endereco com número e cidade. ")
resultado = Geocoder.geocode(endereco)
if resultado.valid_address == True:
    print("Endereço completo.: ", resultado)
    print("Coordenadas.......: ", resultado.coordinates)
    print("Número............: ", resultado.street_number)
    print("CEP...............: ", resultado.postal_code)

print("Foi(ram) encontrado(s) ",resultado.count, " endereço(s).")
for r in resultado:
    print("Cidade......: ", r.state)
    print("País........: ", r.country)
    print("Logradouro..: ", r.route)
    print("###########################")

latitude=float(input("Digite a latitude...: "))
longitude=float(input("Digite a longitude.: "))

resultado = Geocoder.reverse_geocode(latitude, longitude)
if resultado.valid_address == True:
    print("Endereço completo.: ", resultado)
    print("Número............: ", resultado.street_number)
    print("CEP...............: ", resultado.postal_code)
