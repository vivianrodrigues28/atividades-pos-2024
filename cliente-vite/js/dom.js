import { fetchUsers, fetchUserTodos } from './api.js';

export function displayUsers(users) {
  const usersContainer = document.getElementById('users-container');
  usersContainer.innerHTML = ''; 

  users.forEach(user => {
    const userDiv = document.createElement('div');
    userDiv.className = 'user';
    userDiv.innerHTML = `<strong>${user.name}</strong> (Username: ${user.username})`;
    userDiv.onclick = () => loadUserTodos(user.id); 
    usersContainer.appendChild(userDiv);
  });
}

export function displayTodos(todos) {
  const todosContainer = document.getElementById('todos-container');
  todosContainer.innerHTML = ''; 

  todos.forEach(todo => {
    const todoDiv = document.createElement('div');
    todoDiv.className = 'todo';
    todoDiv.innerHTML = `
      <p><strong>Tarefa:</strong> ${todo.title}</p>
      <p><strong>Completada:</strong> ${todo.completed ? 'Sim' : 'Não'}</p>
    `;
    todosContainer.appendChild(todoDiv);
  });
}

async function loadUserTodos(userId) {
  try {
    const todos = await fetchUserTodos(userId);
    displayTodos(todos);
  } catch (error) {
    console.error('Erro ao carregar to-dos:', error);
  }
}
