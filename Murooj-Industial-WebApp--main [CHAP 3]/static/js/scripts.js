// Define a list of user credentials (for demonstration purposes)
const users = [
    { username: 'user1', password: 'password1' },
    { username: 'user2', password: 'password2' },
    { username: 'user3', password: 'password3' }
];

// Function to handle user login
function loginUser() {
    // Get the username and password entered by the user
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    // Check if the entered username and password match any user in the list
    const user = users.find(user => user.username === username && user.password === password);

    // If a matching user is found, simulate successful login
    if (user) {
        alert('Login successful! Welcome, ' + username);
        // Redirect to the dashboard or perform other actions
    } else {
        // If no matching user is found, display an error message
        alert('Invalid username or password. Please try again.');
    }
}
