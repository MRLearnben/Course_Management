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

    // Function to handle form submissions for creating new courses
    const createCourseForm = document.getElementById('create-course-form');
    createCourseForm.addEventListener('submit', function (e) {
        e.preventDefault();
        const formData = new FormData(this);
        fetch('/course', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                title: formData.get('title'),
                description: formData.get('description'),
            }),
        })
            .then(response => response.json())
            .then(data => {
                console.log('Course created:', data);
                fetchCourses(); // Refresh course list after creation
                createCourseForm.reset(); // Clear the form
            })
            .catch(error => console.error('Error creating course:', error));
    });

    // Add similar event listeners and functions for updating and deleting courses
});
