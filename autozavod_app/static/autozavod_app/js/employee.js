function acquaintEmployee(employeeId, docId) {
    fetch(`/acquaint/${employeeId}/${docId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
            'Content-Type': 'application/json'
        }
    }).then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();
            }
        });
}

function unacquaintEmployee(employeeId, docId) {
    fetch(`/unacquaint/${employeeId}/${docId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
            'Content-Type': 'application/json'
        }
    }).then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();
            }
        });
}

function acquaintAll(docId) {
    fetch(`/acquaint_all/${docId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
            'Content-Type': 'application/json'
        }
    }).then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();
            }
        });
}

function unacquaintAll(docId) {
    fetch(`/unacquaint_all/${docId}/`, {
        method: 'POST',
        headers: {
            'X-CSRFToken': '{{ csrf_token }}',
            'Content-Type': 'application/json'
        }
    }).then(response => response.json())
        .then(data => {
            if (data.success) {
                location.reload();
            }
        });
}


