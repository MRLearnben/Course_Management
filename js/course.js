document.addEventListener('DOMContentLoaded', function () {
    // Function to fetch and display course data
    function fetchCourses() {
        fetch('/courses')
            .then(response => response.json())
            .then(data => {
                const courseList = document.getElementById('course-list');
                courseList.innerHTML = ''; // Clear previous course list
                data.forEach(course => {
                    const listItem = document.createElement('li');
                    listItem.innerHTML = `<strong>${course.title}</strong>: ${course.description}`;
                    courseList.appendChild(listItem);
                });
            })
            .catch(error => console.error('Error fetching courses:', error));
    }

    // Fetch and display course data when the page loads
    fetchCourses();

    // Other event listeners and functions for creating, updating, and deleting courses
});
