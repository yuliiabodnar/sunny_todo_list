function fetchTasksBackground(location = '') {
    fetch('/api/tasks/')
        .then(response => response.json())
        .then(data => {
            const taskContainer = document.getElementById('task-container');
            const tasks = taskContainer.getElementsByClassName('task');
            const tasksArray = Array.from(tasks);
            console.log(tasks)

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
            taskContainer.className = `task ${data[].background_class}`;
        })
        .catch(error => {
            console.error('Error fetching tasks:', error);
        });
}
