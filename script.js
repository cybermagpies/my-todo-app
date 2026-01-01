const input = document.getElementById('task-input');
const addBtn = document.getElementById('add-btn');
const taskList = document.getElementById('task-list');

addBtn.addEventListener('click', () => {
    if (input.value !== "") {
        addTask(input.value);
        input.value = "";
    }
});

function addTask(text) {
    const li = document.createElement('li');
    li.classList.add('task-item');
    li.innerHTML = `
        <span>${text}</span>
        <i class="fas fa-trash" onclick="this.parentElement.remove()" style="color: #ff6b6b; cursor: pointer;"></i>
    `;
    taskList.appendChild(li);
}

// Display current date
document.getElementById('date-display').innerText = new Date().toDateString();
