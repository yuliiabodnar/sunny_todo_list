from locations.models.location import Location


def get_color_for_location(weather):
    if check_if_cold_or_rain(weather):
        return 'task-cold'

    if check_if_warm_or_cloudy(weather):
        return 'task-warm'

    if check_if_hot_or_sunny(weather):
        return 'task-hot'

    return None


def check_if_cold_or_rain(weather):
    if weather.is_rain or weather.temperature < 10:
        return True

    return False


def check_if_warm_or_cloudy(weather):
    if weather.is_cloudy or (10 <= weather.temperature < 27):
        return True

    return False


def check_if_hot_or_sunny(weather):
    if weather.is_sunny or weather.temperature >= 27:
        return True

    return False


def get_locations_context(request, locations):
    locations_context = []
    for location in locations:
        location_weather = location.get_location_weather(request)

        location_data = {
            'location': location_weather.location,
            'temperature': location_weather.temperature,
            'is_rain': location_weather.is_rain,
            'is_cloudy': location_weather.is_cloudy,
            'is_sunny':location_weather.is_sunny,
            'background_class': get_color_for_location(location_weather)
        }

        locations_context.append(location_data)

    return locations_context
