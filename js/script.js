
async function fetchUsers() {
    try {
      const response = await fetch('https://jsonplaceholder.typicode.com/users');
      const users = await response.json();
      displayUsers(users);
    } catch (error) {
      console.error('Erro ao buscar usuários:', error);
    }
  }
  
  
  function displayUsers(users) {
    const usersContainer = document.getElementById('users-container');
    usersContainer.innerHTML = ''; 
  
    users.forEach(user => {
      const userDiv = document.createElement('div');
      userDiv.className = 'user';      userDiv.innerHTML = <strong>${user.name}</strong> (Username: ${user.username});
      userDiv.onclick = () => fetchUserTodos(user.id); // Ao clicar, buscar as tarefas do usuário
      usersContainer.appendChild(userDiv);
    });
  }

  async function fetchUserTodos(userId) {
    try {
      const response = await fetch(https://jsonplaceholder.typicode.com/users/${userId}/todos);
      const todos = await response.json();
      displayTodos(todos);
    } catch (error) {
      console.error('Erro ao buscar to-dos:', error);
    }
  }
  
  function displayTodos(todos) {
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
  
  window.onload = fetchUsers;