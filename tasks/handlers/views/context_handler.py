from locations.models.location import Location


def get_color_for_location(weather):
    """
    Get the color code for the location based on weather conditions.

    Args:
        weather: A weather object.

    Returns:
        str or None: The color code for the location based on weather conditions.
                     Returns None if weather conditions don't match any criteria.
    """
    if check_if_cold_or_rain(weather):
        return 'task-cold'

    if check_if_warm_or_cloudy(weather):
        return 'task-warm'

    if check_if_hot_or_sunny(weather):
        return 'task-hot'

    return None


def check_if_cold_or_rain(weather):
    """
    Check if the weather indicates cold or rainy conditions.

    Args:
        weather: A weather object.

    Returns:
        bool: True if the weather indicates cold or rainy conditions, False otherwise.
    """
    if weather.is_rain or weather.temperature < 10:
        return True

    return False


def check_if_warm_or_cloudy(weather):
    """
    Check if the weather indicates warm or cloudy conditions.

    Args:
        weather: A weather object.

    Returns:
        bool: True if the weather indicates warm or cloudy conditions, False otherwise.
    """
    if weather.is_cloudy or (10 <= weather.temperature < 27):
        return True

    return False


def check_if_hot_or_sunny(weather):
    """
    Check if the weather indicates hot or sunny conditions.

    Args:
        weather: A weather object.

    Returns:
        bool: True if the weather indicates hot or sunny conditions, False otherwise.
    """
    if weather.is_sunny or weather.temperature >= 27:
        return True

    return False


def get_locations_context(request, locations):
    """
    Get the context data for multiple locations.

    Args:
        request (HttpRequest): The HTTP request object.
        locations (iterable):  An iterable of Location objects.

    Returns:
        list: A list of context dictionaries for the locations.
    """
    locations_context = []
    for location in locations:
        location_weather_factory = location.get_location_weather_factory(request)
        location_weather = location_weather_factory.create()

        context_data = get_context_by_weather(location_weather)

        locations_context.append(context_data)

    return locations_context


def update_tasks_if_completed(tasks):
    """
    Update completed tasks with additional context data.

    Args:
        tasks (iterable): An iterable of task objects.

    Returns:
        list: A list of updated task objects with additional context data.
    """
    updated_tasks = []
    for task in tasks:
        updated_task = task

        if task.completed:
            # Get context data for the completed task
            task_context = get_task_context(task)

            # Update task with additional context data
            updated_task.background_class = task_context['background_class']
            updated_task.temperature = task_context['temperature']

        updated_tasks.append(updated_task)

    return updated_tasks


def get_task_context(task):
    """
    Get the context for a single task.

    Args:
        task: A task object.

    Returns:
        dict: A context dictionary for the task.
    """
    location_weather_factory = task.location.get_location_weather_factory()
    location_weather = location_weather_factory.create(
        task.location.name,
        float(task.temperature),
        task.is_rain,
        task.is_cloudy,
        task.is_sunny
    )
    return get_context_by_weather(location_weather)


def get_context_by_weather(location_weather):
    """
    Get the context for a location based on weather.

    Args:
        location_weather: A weather object.

    Returns:
        dict: A context dictionary for the location weather.
    """
    return {
            'location': location_weather.location,
            'temperature': location_weather.temperature,
            'is_rain': location_weather.is_rain,
            'is_cloudy': location_weather.is_cloudy,
            'is_sunny':location_weather.is_sunny,
            'background_class': get_color_for_location(location_weather)
        }
