import random

month = int(input('Please enter a number of the month: '))

def get_random_temp():
    season = get_season()
    if season == 'winter':
        celsius = random.uniform(-10, 16)
        return celsius
    elif season == 'summer':
        celsius = random.uniform(23 , 40)
        return celsius
    elif season == 'autumn':
        celsius = random.uniform(18 , 23)
        return celsius
    elif season == 'spring':
        celsius = random.uniform(20 , 26)
        return celsius
    


def main():
    the_temperature = round(get_random_temp(), 1)
    print(f'The temperature right now is {the_temperature} degrees Celsius')
    if the_temperature < 0:
        print(f'\nBrrr, that\'s freezing! Wear some extra layers today')
    elif the_temperature >= 0 and the_temperature < 16:
        print(f'Quite chilly! Don\'t forget your coat')
    elif the_temperature >= 16 and the_temperature < 23:
        print(f'Normal temperature! Wear whatever you please')
    elif the_temperature >= 24 and the_temperature < 32:
        print(f'Quite Hot! Don\'t wear too heavy clothes')
    elif the_temperature >= 32 and the_temperature < 40:
        print(f'Super Hot today! Wear light clothes')

def get_season():
    if month >= 3 and month <= 5:
        season = 'spring'
        return season
    elif month >= 6 and month <= 8:
        season = 'summer'
        return season
    elif month >= 9 and month <= 11:
        season = 'autumn'
        return season
    elif month == 12 or month > 0 and month <= 2:
        season = 'winter'
        return season

get_season()
get_random_temp()
main()