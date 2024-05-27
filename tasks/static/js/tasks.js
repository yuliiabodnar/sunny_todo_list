function fetchTasksBackground(location = '') {
    fetch('/api/tasks/')
        .then(response => response.json())
        .then(data => {
            const taskContainer = document.getElementById('task-container');
            const tasks = taskContainer.getElementsByClassName('task');
            const tasksArray = Array.from(tasks);

            data.forEach(taskData => {
                const tasksInLocation = tasksArray.filter(taskElement => taskElement.getAttribute('location') === taskData.location);

                tasksInLocation.forEach(taskElement => {
                    taskElement.className = `task ${taskData.background_class}`;
                });
            });
        })
        .catch(error => {
            console.error('Error fetching tasks:', error);
        });
}

function fetchLocationBackground(location) {
    fetch('/api/location/' + location + '/')
        .then(response => response.json())
        .then(data => {
            const taskContainer = document.getElementById('task-container');
            const temperatureContainer = document.getElementById('location-temperature');

            if (data.length > 0) {
                taskContainer.className = `task ${data[0].background_class}`;
                temperatureContainer.textContent =`Temperature: ${data[0].temperature}°C`;;
            } else {
                temperatureContainer.textContent = 'No temperature data available';
            }
        })
        .catch(error => {
            console.error('Error fetching tasks:', error);
        });
}
