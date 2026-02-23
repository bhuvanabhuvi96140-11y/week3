// Form Validation
function validateForm(formId) {
    const form = document.getElementById(formId);
    const inputs = form.querySelectorAll('input[type="text"], input[type="email"], input[type="password"], textarea');
    let isValid = true;

    inputs.forEach(input => {
        const errorDiv = input.nextElementSibling;
        if (errorDiv && errorDiv.classList.contains('error-text')) {
            errorDiv.innerText = '';
        }
        if (input.value.trim() === '') {
            isValid = false;
            showError(input, 'This field is required');
        } else if (input.type === 'email' && !isValidEmail(input.value)) {
            isValid = false;
            showError(input, 'Please enter a valid email');
        } else if (input.id === 'password' && input.value.length < 6) {
            isValid = false;
            showError(input, 'Password must be at least 6 characters');
        } else if (input.id === 'confirmPassword') {
            const password = document.getElementById('password');
            if (input.value !== password.value) {
                isValid = false;
                showError(input, 'Passwords do not match');
            }
        }
    });
    return isValid;
}
function showError(input, message) {
    let errorDiv = input.nextElementSibling;
    if (!errorDiv || !errorDiv.classList.contains('error-text')) {
        errorDiv = document.createElement('div');
        errorDiv.className = 'error-text';
        input.parentNode.insertBefore(errorDiv, input.nextSibling);
    }
    errorDiv.innerText = message;
}
function isValidEmail(email) {
    const emailPattern = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return emailPattern.test(email);
}
// Form Submit Handlers
function handleRegisterSubmit(event) {
    event.preventDefault();
    if (validateForm('registerForm')) {
        showSuccessMessage('Registration successful! Redirecting to login...');
        setTimeout(() => {
            window.location.href = 'login.html';
        }, 1500);
    }
}
function handleLoginSubmit(event) {
    event.preventDefault();
    if (validateForm('loginForm')) {
        showSuccessMessage('Login successful! Redirecting to home...');
        setTimeout(() => {
            window.location.href = 'index.html';
        }, 1500);
    }
}
function handleContactSubmit(event) {
    event.preventDefault();
    if (validateForm('contactForm')) {
        showSuccessMessage('Message sent successfully! Thank you for contacting us.');
        document.getElementById('contactForm').reset();
        setTimeout(() => {
            document.body.querySelector('.success-message').remove();
        }, 3000);
    }
}
function showSuccessMessage(message) {
    const successDiv = document.createElement('div');
    successDiv.className = 'success-message';
    successDiv.innerText = message;
    const mainElement = document.querySelector('main');
    mainElement.insertBefore(successDiv, mainElement.firstChild);
}
// Set active nav link
function setActiveNav() {
    const currentPage = window.location.pathname.split('/').pop() || 'index.html';
    const navLinks = document.querySelectorAll('nav a');
    navLinks.forEach(link => {
        const href = link.getAttribute('href');
        if (href === currentPage || (currentPage === '' && href === 'index.html')) {
            link.classList.add('active');
        } else {
            link.classList.remove('active');
        }
    });
}
// Initialize on page load
document.addEventListener('DOMContentLoaded', setActiveNav);