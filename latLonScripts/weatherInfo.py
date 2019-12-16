import requests
import json

'''
    Returns a tuple (iscloudy, cloudcover, humidity, temperature)
'''
def weatherInfo(lat, lon) :
    with open('key.json') as f :
        appid = json.load(f)['appid']
    
    response = requests.get(f'https://samples.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid={appid}')
    cloudCover = response.json()['clouds']['all']
    humidity = response.json()['main']['humidity']
    temperature = response.json()['main']['temp']
    f.close()
    if cloudCover > 70 and humidity > 70 :
        return (1, cloudCover , humidity, temperature)
    else :
        return (0, cloudCover , humidity, temperature- 273.15) 

if __name__ == '__main__' :
    ic, cc, humid, tem = weatherInfo(52.516, 12.389)
    print(tem)