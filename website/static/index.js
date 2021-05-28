function deleteNote(noteId){
    fetch(' /delete-note', {
    method: 'POST',
    body: JSON.stringify({ noteId: noteId})
    }).then((_res) => {
        window.location.href = "/";
    });
}

function deleteTask(taskId){
    fetch(' /task/delete-task', {
    method: 'POST',
    body: JSON.stringify({ taskId: taskId})
    }).then((_res) => {
        window.location.href = "/task";
    });
}