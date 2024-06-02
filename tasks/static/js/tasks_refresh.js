// Fetch tasks on page load
document.addEventListener('DOMContentLoaded', function() {
    buildTasksMap();
    fetchTasksBackground();
});

// Fetch tasks every 10 minutes
setInterval(fetchTasksBackground, 600000);