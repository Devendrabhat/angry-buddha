import requests

'''
    Returns a tuple (iscloudy, cloudcover, humidity, temperature)
'''
def weatherInfo(lat, lon) :

    response = requests.get(f'https://samples.openweathermap.org/data/2.5/weather?lat={lat}&lon={lon}&appid=b6907d289e10d714a6e88b30761fae22')
    cloudCover = response.json()['clouds']['all']
    humidity = response.json()['main']['humidity']
    temperature = response.json()['main']['temp']

    if cloudCover > 70 and humidity > 70 :
        return (1, cloudCover , humidity, temperature)
    else :
        return (0, cloudCover , humidity, temperature- 273.15) 

if __name__ == '__main__' :
    ic, cc, humid, tem = weatherInfo(52.516, 12.389)
    print(tem)