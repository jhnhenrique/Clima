import requests
import json

cidade = input("Escreva o nome da cidade:")

requisicao = requests.get('http://api.openweathermap.org/data/2.5/weather?q='+cidade+'&appid=02a651cfdbaecec33f105564f3e4c930')

tempo = json.loads(requisicao.text)

print('Condição do Tempo:', tempo['weather'][0]['main'])
print('Temperatura:', float(tempo['main']['temp']) - 273.15)