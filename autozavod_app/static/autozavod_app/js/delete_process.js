let processIdToDelete = null;

// Функция для получения CSRF-токена из куки
function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

const csrftoken = getCookie('csrftoken'); // Получаем CSRF-токен

// Функция для открытия модального окна
function confirmDelete(processId) {
    processIdToDelete = processId;
    console.log(`Подтверждение удаления процесса с ID: ${processIdToDelete}`); // Логирование
    document.getElementById('deleteModal').style.display = 'block';
}

// Обработчик для кнопки "Да, удалить"
document.getElementById('confirmDeleteBtn').addEventListener('click', async function () {
    if (processIdToDelete) {
        try {
            console.log(`Отправка запроса на удаление процесса с ID: ${processIdToDelete}`); // Логирование
            const response = await fetch(`/delete_process/${processIdToDelete}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken, // Используем полученный CSRF-токен
                    'Content-Type': 'application/json'
                }
            });

            console.log(`Ответ сервера: ${response.status}`); // Логирование

            if (response.ok) {
                const data = await response.json();
                if (data.status === 'success') {
                    console.log('Процесс успешно удален'); // Логирование
                    location.reload(); // Обновляем страницу
                } else {
                    alert('Ошибка при удалении процесса: ' + data.message);
                }
            } else {
                alert('Ошибка при удалении процесса. Статус: ' + response.status);
            }
        } catch (error) {
            console.error('Ошибка:', error);
            alert('Произошла ошибка при удалении.');
        } finally {
            document.getElementById('deleteModal').style.display = 'none'; // Закрываем модальное окно
        }
    }
});

// Обработчик для кнопки "Отмена"
document.getElementById('cancelDeleteBtn').addEventListener('click', function () {
    console.log('Удаление отменено'); // Логирование
    document.getElementById('deleteModal').style.display = 'none';
});

// Закрытие модального окна при клике вне его
window.onclick = function (event) {
    const modal = document.getElementById('deleteModal');
    if (event.target === modal) {
        modal.style.display = 'none';
    }
};

// Обработчик для изменения статуса процесса
document.querySelectorAll('.status-checkbox').forEach(checkbox => {
    checkbox.addEventListener('change', async function () {
        const processId = this.dataset.processId;
        const newStatus = this.checked;

        try {
            const response = await fetch(`/update_process_status/${processId}/`, {
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrftoken, // Используем полученный CSRF-токен
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify({ status_procces: newStatus })
                
            });

            if (response.ok) {
                const data = await response.json();
                if (data.status === 'success') {
                    // Обновляем текст статуса
                    location.reload(); // Обновляем страницу
                    const statusText = this.nextElementSibling;
                    if (newStatus) {
                        statusText.textContent = 'Выполнен';
                        statusText.className = 'process-true';
                    } else {
                        statusText.textContent = 'Требует действий';
                        statusText.className = 'process-false';
                    }
                } else {
                    alert('Ошибка при обновлении статуса: ' + data.message);
                    // Восстанавливаем предыдущее состояние чекбокса
                    this.checked = !newStatus;
                }
            } else {
                alert('Ошибка при обновлении статуса. Статус: ' + response.status);
                // Восстанавливаем предыдущее состояние чекбокса
                this.checked = !newStatus;
            }
        } catch (error) {
            console.error('Ошибка:', error);
            alert('Произошла ошибка при обновлении статуса.');
            // Восстанавливаем предыдущее состояние чекбокса
            this.checked = !newStatus;
        }
    });
});