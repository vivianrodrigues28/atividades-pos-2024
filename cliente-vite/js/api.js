export async function fetchUsers() {
    try {
      const response = await fetch('https://jsonplaceholder.typicode.com/users');
      return await response.json();
    } catch (error) {
      console.error('Erro ao buscar usuários:', error);
      throw error;
    }
  }
  

  export async function fetchUserTodos(userId) {
    try {
      const response = await fetch(`https://jsonplaceholder.typicode.com/users/${userId}/todos`);
      return await response.json();
    } catch (error) {
      console.error('Erro ao buscar to-dos:', error);
      throw error;
    }
  }
  