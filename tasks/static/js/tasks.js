/**
 * Fetches tasks data from the server and updates the background color of task elements based on their location.
 * @param {string} location - The location for which tasks background is to be fetched.
 */
function fetchTasksBackground(location = '') {
    // Fetch tasks data from the server
    fetch('/api/tasks/')
        .then(response => response.json())
        .then(data => {
            const taskListContainer = document.getElementById('task-list-container');
            // Get all task elements within the container
            const tasks = taskListContainer.getElementsByClassName('task');
            // Convert the HTMLCollection to an array
            const tasksArray = Array.from(tasks);

            // Iterate over each task data from the server response
            data.forEach(taskData => {
                // Filter tasks based on their location attribute
                const tasksInLocation = tasksArray.filter(taskElement => taskElement.getAttribute('location') === taskData.location);

                // Update the class name of each task element in the location
                tasksInLocation.forEach(taskElement => {
                    taskElement.className = `task ${taskData.background_class}`;
                });
            });
        })
        .catch(error => {
            console.error('Error fetching tasks:', error);
        });
}

/**
 * Updates the class name of the task container element.
 * @param {string} className - The class name to be set on the task container.
 */
function updateTaskContainerClassName(className = '') {
    const taskContainer = document.getElementById('task-container');
    taskContainer.className = `task ${className}`;
}

/**
 * Updates the text content of the temperature container element.
 * @param {string} textContent - The text content to be set on the temperature container.
 */
function updateTemperatureContainerText(textContent = '') {
    const temperatureContainer = document.getElementById('location-temperature');
    temperatureContainer.textContent =`${textContent}`;
}

/**
 * Fetches location data from the server and updates task container class name and temperature container text content.
 * @param {string} location - The location for which data is to be fetched.
 */
function fetchLocationBackground(location) {
    // If location is not provided, clear task container class name and temperature container text
    if (!location) {
        updateTaskContainerClassName('');
        updateTemperatureContainerText('');
        return;
    }

    / Fetch location data from the server
    fetch('/api/location/' + location + '/')
        .then(response => response.json())
        .then(data => {
            // Initialize default text content and class name
            var textContent = 'No temperature data available';
            var className = '';
            // If data is available, update text content and class nam
            if (data.length > 0) {
                className = `${data[0].background_class}`;
                textContent =`Temperature: ${data[0].temperature}°C`;
            }

            // Update task container class name and temperature container text content
            updateTaskContainerClassName(className);
            updateTemperatureContainerText(textContent);
        })
        .catch(error => {
            console.error('Error fetching location data:', error);
        });
}
