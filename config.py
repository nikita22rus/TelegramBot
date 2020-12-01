TOKEN = '1426946005:AAH4BJZA73EcUBi5jTiVrsm5ltn2WsI9i8E'

URL = 'https://api.telegram.org/bot{token}/{method}'

UPDATE_METH = 'getUpdates'
SEND_METH = 'sendMessage'

MY_ID =

UPDATE_ID_FILE_PATH = 'update_id'

with open(UPDATE_ID_FILE_PATH) as file:
    data = file.readline()
    if data:
        data = int(data)
    UPDATE_ID = data


WEATHER_TOKEN = '4630b4814440849e47f04c0b66a30668'

WEATHER_URL = 'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={token}'

