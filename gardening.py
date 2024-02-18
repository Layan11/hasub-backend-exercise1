
class Plant:
    def __init__(self, name, sun_or_rain, water_need, likes_wind, snow_amount):
        self.name = name
        self.sun_or_rain = sun_or_rain
        self.water_need = water_need
        self.likes_wind = likes_wind
        self.snow_amount = snow_amount


if __name__ == '__main__':
    p1 = Plant('p1', 'sun', 'low', 'yes', 'low')
    p2 = Plant('p2', 'sun', 'low', 'no', 'low')
    p3 = Plant('p3', 'rain', 'high', 'yes', 'high')
    plants = [p1, p2, p3]
    sunny = precipitation_number = wind = snow = ''
    while sunny not in ['sun', 'rain']:
        sunny = input(print('please describe the weather today, sun/rain ?'))
    while precipitation_number not in ['high', 'low']:
        precipitation_number = input(print('is the precipitation number high or low?'))
    while wind not in ['yes', 'no']:
        wind = input(print('is there wind ? yes/no'))
    while snow not in ['high', 'low']:
        snow = input(print('whats the amount of snow high / low ?'))
    print('plants that like ' + str(sunny) + ' conditions, and like ' + str(precipitation_number) +
          ' precipitation number, and ' + 'that like windy conditions' if wind == 'yes' else
          'that dont like windy conditions are: ')
    for plant in plants:
        if plant.sun_or_rain == sunny and plant.water_need == precipitation_number and plant.likes_wind == wind:
            print(plant.name)

    print('plants dead due to the snow: ')
    for plant in plants:
        if plant.snow_amount == snow:
            print(plant.name)
