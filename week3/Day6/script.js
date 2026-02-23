// Alert on button click
function showAlert() {
    alert('Hello! This is a basic JavaScript alert. Button was clicked!');
}
// Change text on click
function changeText() {
    const element = document.getElementById('changeText');
    if (element.innerText === 'Click me to change text!') {
        element.innerText = 'Text has been changed!';
        element.style.color = '#0b79d0';
    } else {
        element.innerText = 'Click me to change text!';
        element.style.color = '#333';
    }
}
// Form validation
function validateForm(event) {
    event.preventDefault();
    const name = document.getElementById('fullName').value.trim();
    const email = document.getElementById('email').value.trim();
    const password = document.getElementById('password').value.trim();
    const nameError = document.getElementById('nameError');
    const emailError = document.getElementById('emailError');
    const passwordError = document.getElementById('passwordError');
    const formMessage = document.getElementById('formMessage');
    
    // Reset error messages
    nameError.innerText = '';
    emailError.innerText = '';
    passwordError.innerText = '';
    formMessage.innerText = '';
    let isValid = true;
    
    // Name validation
    if (!name) {
        nameError.innerText = 'Name is required';
        isValid = false;
    } else if (name.length < 3) {
        nameError.innerText = 'Name must be at least 3 characters';
        isValid = false;
    }
    // Email validation
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    if (!email) {
        emailError.innerText = 'Email is required';
        isValid = false;
    } else if (!emailPattern.test(email)) {
        emailError.innerText = 'Please enter a valid email';
        isValid = false;
    }
    // Password validation
    if (!password) {
        passwordError.innerText = 'Password is required';
        isValid = false;
    } else if (password.length < 6) {
        passwordError.innerText = 'Password must be at least 6 characters';
        isValid = false;
    }
    if (isValid) {
        formMessage.style.color = '#28a745';
        formMessage.innerText = `✓ Form submitted successfully! Welcome, ${name}!`;
        document.getElementById('formValidation').reset();
    }
}
// Simple calculator
function appendToDisplay(value) {
    const display = document.getElementById('calcDisplay');
    display.value += value;
}
function clearDisplay() {
    document.getElementById('calcDisplay').value = '';
}
function deleteLastChar() {
    const display = document.getElementById('calcDisplay');
    display.value = display.value.slice(0, -1);
}
function calculateResult() {
    const display = document.getElementById('calcDisplay');
    const result = document.getElementById('calcResult');   
    try {
        // Evaluate the expression
        const answer = eval(display.value);
        result.innerText = `Result: ${answer}`;
    } catch (error) {
        result.innerText = 'Error in expression';
    }
}