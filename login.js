document.getElementById('loginForm').addEventListener('submit', function(e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
    
    if (login(username, password)) {
        window.location.href = 'login.html';
    } else {
        document.getElementById('errorMessage').textContent = 'ชื่อผู้ใช้หรือรหัสผ่านไม่ถูกต้อง';
    }
});

function login(username, password) {
    const validUsers = ['niceppn', 'cream', 'bonus' ,'nat'];
    const validPassword = '123456';

    if (validUsers.includes(username) && password === validPassword) {
        localStorage.setItem('isLoggedIn', 'true');
        localStorage.setItem('username', username);
        return true;
    }
    return false;
}