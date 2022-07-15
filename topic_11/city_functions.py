def get_formatted_city_country(city, country, population = ''):
    """Строит отформатированную инфу вида 'Город, Страна - популяция'."""
    city = city.title()
    country = country.title()
    if population:
        formatted_city_country = city + ', ' + country + ' population - '
        formatted_city_country += population + '.'
    else:
        formatted_city_country = city + ', ' + country + '.'
    return formatted_city_country 