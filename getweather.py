from pyowm import *
import constants


owm = OWM(constants.WEATHER_TOKEN_NAME, language="ru")


def search_temperature(city):
    try:
        observation = owm.weather_at_place(city)
    except:
        return "Нет такого города"
    else:
        weather = observation.get_weather()
        temperature = weather.get_temperature('celsius')
        return str(temperature['temp']) + " Градус"
