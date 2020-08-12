$(document).ready(function () {
    $('.js-example-basic-multiple').select2();
    $('.js-example-basic-single').select2();

    // Get csrftoken
    function getCookie(name) {
        let cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            const cookies = document.cookie.split(';');
            for (let i = 0; i < cookies.length; i++) {
                const cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === name + '=') {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    const csrftoken = getCookie('csrftoken');

    // Specify an empty card to add task
    const card = document.createElement('li');
    card.classList.add('list-group-item');
    card.innerHTML = `<div class="card shadow-sm p-3"><input class="js-editing form-control border-0" type="text"></div>`;

    // When the add-new-task button (plus symbol with class="js-add-task") is clicked, create an empty card to add a new task.
    document.querySelectorAll('.js-add-task').forEach((button) => {
        button.onclick = () => {
            const status = button.dataset.status;
            const project_id = button.dataset.projectid;
            const cardContainer = button.nextElementSibling.firstElementChild;
            if (cardContainer.contains(card)) {
                document.querySelector('.js-editing').value = '';
                card.remove();
            } else {
                cardContainer.prepend(card);
            }

            // Post the new added task to server when user press enter after done typing task title
            document.querySelector('.js-editing').addEventListener('keyup', function (event) {
                if (event.keyCode === 13) {
                    if (this.value.length === 0) {
                        card.remove();
                    } else {
                        const title = this.value;
                        postNewTask(status, project_id, title);
                        card.remove();
                    }
                }
            });
        };
    });

    // Update task status
    document.querySelectorAll('.js-status-update').forEach((button) => {
        button.onclick = () => {
            const status = button.dataset.status;
            const taskId = button.dataset.taskid;
            updateTaskStatus(taskId, status);
        };
    });

    // Delete task
    document.querySelectorAll('.js-task-delete').forEach((button) => {
        button.onclick = () => {
            const taskId = button.dataset.taskid;
            deleteTask(taskId);
        };
    });

    // Post comment
    const addCommentTextbox = document.querySelector('#js-add-comment');
    if (addCommentTextbox) {
        document.querySelector('#js-add-comment').addEventListener('keyup', function (event) {
            event.preventDefault();
            if (event.keyCode === 13 && this.value.length !== 0) {
                const content = this.value;
                const taskId = this.dataset.taskid;
                postNewComment(taskId, content);
                this.value = '';
            }
        });
    }

    function postNewTask(status, project_id, title) {
        const request = new XMLHttpRequest();
        request.open('POST', 'ajax/create-task/');
        request.setRequestHeader('X-CSRFToken', csrftoken);
        request.onload = () => {
            window.location.reload();
        };
        const data = new FormData();
        data.append('status', status);
        data.append('title', title);
        data.append('project_id', project_id);
        request.send(data);
    }

    function updateTaskStatus(taskId, newStatus) {
        const request = new XMLHttpRequest();
        request.open('POST', 'ajax/update-task-status/');
        request.setRequestHeader('X-CSRFToken', csrftoken);
        request.onload = () => {
            window.location.reload();
        };
        const data = new FormData();
        data.append('status', newStatus);
        data.append('task_id', taskId);
        request.send(data);
    }

    function deleteTask(taskId) {
        const request = new XMLHttpRequest();
        request.open('POST', 'ajax/delete-task/');
        request.setRequestHeader('X-CSRFToken', csrftoken);
        request.onload = () => {
            window.location.reload();
        };
        const data = new FormData();
        data.append('task_id', taskId);
        request.send(data);
    }

    function postNewComment(taskId, content) {
        const request = new XMLHttpRequest();
        request.open('POST', 'ajax/create-comment/');
        request.setRequestHeader('X-CSRFToken', csrftoken);
        request.onload = (data) => {
            window.location.reload();
        };
        const data = new FormData();
        data.append('task_id', taskId);
        data.append('content', content);
        request.send(data);
    }
});
