function acquaintEmployee(employeeId, orderId) {
    fetch(`/acquaint_order/${employeeId}/${orderId}/`, {
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

function unacquaintEmployee(employeeId, orderId) {
    fetch(`/unacquaint_order/${employeeId}/${orderId}/`, {
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

function acquaintAll(orderId) {
    fetch(`/acquaint_all_order/${orderId}/`, {
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

function unacquaintAll(orderId) {
    fetch(`/unacquaint_all_order/${orderId}/`, {
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