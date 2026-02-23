import os
import webbrowser
import argparse
def create_frontend_project(target_dir: str) -> tuple:
    """Create a mini frontend project with home, register, login, and contact pages."""
    # Shared CSS
    css_content = '''* {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body {
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    min-height: 100vh;
    display: flex;
    flex-direction: column;
}
header {
    background: rgba(0, 0, 0, 0.7);
    padding: 15px 0;
    box-shadow: 0 2px 5px rgba(0, 0, 0, 0.2);
}
header .container {
    max-width: 1200px;
    margin: 0 auto;
    padding: 0 20px;
    display: flex;
    justify-content: space-between;
    align-items: center;
}
header h1 {
    color: #fff;
    font-size: 1.8rem;
}
nav a {
    color: #fff;
    text-decoration: none;
    margin: 0 15px;
    padding: 8px 15px;
    border-radius: 4px;
    transition: background 0.3s;
}
nav a:hover {
    background: #667eea;
}
nav a.active {
    background: #667eea;
    font-weight: bold;
}
main {
    flex: 1;
    padding: 40px 20px;
}
.container {
    max-width: 1200px;
    margin: 0 auto;
}
.hero {
    background: rgba(255, 255, 255, 0.95);
    padding: 60px 40px;
    border-radius: 12px;
    text-align: center;
    margin-bottom: 40px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}
.hero h1 {
    color: #667eea;
    font-size: 2.5rem;
    margin-bottom: 20px;
}
.hero p {
    color: #666;
    font-size: 1.1rem;
    margin-bottom: 30px;
}
.cta-buttons {
    display: flex;
    gap: 15px;
    justify-content: center;
    flex-wrap: wrap;
}
.btn {
    padding: 12px 30px;
    border: none;
    border-radius: 4px;
    font-size: 1rem;
    cursor: pointer;
    text-decoration: none;
    display: inline-block;
    transition: all 0.3s;
    font-weight: bold;
}
.btn-primary {
    background: #667eea;
    color: #fff;
}
.btn-primary:hover {
    background: #5568d3;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(102, 126, 234, 0.4);
}
.btn-secondary {
    background: #764ba2;
    color: #fff;
}
.btn-secondary:hover {
    background: #63398b;
    transform: translateY(-2px);
    box-shadow: 0 5px 15px rgba(118, 75, 162, 0.4);
}
.form-card {
    background: rgba(255, 255, 255, 0.95);
    padding: 40px;
    border-radius: 12px;
    max-width: 500px;
    margin: 0 auto;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}
.form-card h2 {
    color: #667eea;
    margin-bottom: 30px;
    text-align: center;
}
.form-group {
    margin-bottom: 20px;
}
.form-group label {
    display: block;
    margin-bottom: 8px;
    color: #333;
    font-weight: bold;
}
.form-group input,
.form-group textarea,
.form-group select {
    width: 100%;
    padding: 12px;
    border: 1px solid #ddd;
    border-radius: 4px;
    font-size: 1rem;
    font-family: inherit;
    transition: border-color 0.3s;
}
.form-group input:focus,
.form-group textarea:focus,
.form-group select:focus {
    outline: none;
    border-color: #667eea;
    box-shadow: 0 0 5px rgba(102, 126, 234, 0.3);
}
.form-group textarea {
    resize: vertical;
    min-height: 120px;
}
.form-actions {
    display: flex;
    gap: 10px;
    margin-top: 30px;
}
.form-actions .btn {
    flex: 1;
    text-align: center;
}
.form-actions .btn-secondary {
    background: #ccc;
    color: #333;
}
.form-actions .btn-secondary:hover {
    background: #aaa;
}
.error-text {
    color: #dc3545;
    font-size: 0.9rem;
    margin-top: 5px;
}
.success-message {
    background: #d4edda;
    color: #155724;
    padding: 15px;
    border-radius: 4px;
    margin-bottom: 20px;
}
.info-section {
    background: rgba(255, 255, 255, 0.95);
    padding: 40px;
    border-radius: 12px;
    margin-bottom: 40px;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
}
.info-section h3 {
    color: #667eea;
    margin-bottom: 15px;
    font-size: 1.3rem;
}
.info-section p {
    color: #666;
    line-height: 1.8;
    margin-bottom: 10px;
}
.features {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
    gap: 30px;
    margin-top: 40px;
}
.feature-card {
    background: rgba(255, 255, 255, 0.95);
    padding: 30px;
    border-radius: 8px;
    text-align: center;
    box-shadow: 0 5px 15px rgba(0, 0, 0, 0.1);
}
.feature-card h3 {
    color: #667eea;
    margin-bottom: 15px;
}
.feature-card p {
    color: #666;
}
footer {
    background: rgba(0, 0, 0, 0.7);
    color: #fff;
    text-align: center;
    padding: 20px;
    margin-top: auto;
}
footer p {
    margin: 5px 0;
}
@media (max-width: 768px) {
    .hero h1 {
        font-size: 1.8rem;
    }
    .form-card {
        padding: 30px 20px;
    }
    nav a {
        margin: 0 10px;
        font-size: 0.9rem;
    }
    .cta-buttons {
        flex-direction: column;
    }
    .cta-buttons .btn {
        width: 100%;
    }
}'''
    # Shared JavaScript
    js_content = '''// Form Validation
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
    const emailPattern = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
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
document.addEventListener('DOMContentLoaded', setActiveNav);'''

    # Home page
    home_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Home - Frontend Project</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Frontend Project</h1>
            <nav>
                <a href="index.html">Home</a>
                <a href="register.html">Register</a>
                <a href="login.html">Login</a>
                <a href="contact.html">Contact</a>
            </nav>
        </div>
    </header>

    <main>
        <div class="container">
            <section class="hero">
                <h1>Welcome to Our Mini Frontend Project</h1>
                <p>A demonstration of a simple yet complete web application with multiple pages including registration, login, and contact forms.</p>
                <div class="cta-buttons">
                    <a href="register.html" class="btn btn-primary">Get Started</a>
                    <a href="contact.html" class="btn btn-secondary">Contact Us</a>
                </div>
            </section>

            <section class="features">
                <div class="feature-card">
                    <h3>Responsive Design</h3>
                    <p>Beautiful and responsive layout that works on all devices - desktop, tablet, and mobile.</p>
                </div>
                <div class="feature-card">
                    <h3>Form Validation</h3>
                    <p>Client-side validation for registration, login, and contact forms with real-time error messages.</p>
                </div>
                <div class="feature-card">
                    <h3>User Friendly</h3>
                    <p>Intuitive navigation and clean interface designed for the best user experience.</p>
                </div>
                <div class="feature-card">
                    <h3>Modern Styling</h3>
                    <p>Gradient backgrounds, smooth transitions, and professional color scheme throughout.</p>
                </div>
            </section>

            <section class="info-section">
                <h3>About This Project</h3>
                <p>This is a mini frontend project created to demonstrate fundamental web development concepts including:</p>
                <p>✓ HTML5 semantic markup<br>
                   ✓ CSS3 styling with gradients and flexbox<br>
                   ✓ JavaScript form validation and interactivity<br>
                   ✓ Responsive design principles<br>
                   ✓ Clean code structure</p>
            </section>
        </div>
    </main>

    <footer>
        <p>&copy; 2026 Frontend Project. All rights reserved.</p>
        <p>Created with HTML, CSS, and JavaScript</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

    # Registration page
    register_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Register - Frontend Project</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Frontend Project</h1>
            <nav>
                <a href="index.html">Home</a>
                <a href="register.html">Register</a>
                <a href="login.html">Login</a>
                <a href="contact.html">Contact</a>
            </nav>
        </div>
    </header>

    <main>
        <div class="container">
            <div class="form-card">
                <h2>Create Account</h2>
                <form id="registerForm" onsubmit="handleRegisterSubmit(event)">
                    <div class="form-group">
                        <label for="fullName">Full Name</label>
                        <input type="text" id="fullName" name="fullName" placeholder="Enter your full name">
                    </div>

                    <div class="form-group">
                        <label for="email">Email Address</label>
                        <input type="email" id="email" name="email" placeholder="Enter your email">
                    </div>

                    <div class="form-group">
                        <label for="phone">Phone Number</label>
                        <input type="text" id="phone" name="phone" placeholder="Enter your phone number">
                    </div>

                    <div class="form-group">
                        <label for="password">Password</label>
                        <input type="password" id="password" name="password" placeholder="Enter a password (min 6 characters)">
                    </div>

                    <div class="form-group">
                        <label for="confirmPassword">Confirm Password</label>
                        <input type="password" id="confirmPassword" name="confirmPassword" placeholder="Confirm your password">
                    </div>

                    <div class="form-group">
                        <label for="address">Address</label>
                        <input type="text" id="address" name="address" placeholder="Enter your address">
                    </div>

                    <div class="form-group">
                        <label for="city">City</label>
                        <input type="text" id="city" name="city" placeholder="Enter your city">
                    </div>

                    <div class="form-group">
                        <label for="zipcode">Zip Code</label>
                        <input type="text" id="zipcode" name="zipcode" placeholder="Enter your zip code">
                    </div>

                    <div class="form-actions">
                        <button type="submit" class="btn btn-primary">Register</button>
                        <a href="index.html" class="btn btn-secondary">Cancel</a>
                    </div>
                </form>

                <p style="text-align: center; margin-top: 20px; color: #666;">
                    Already have an account? <a href="login.html" style="color: #667eea; text-decoration: none; font-weight: bold;">Login here</a>
                </p>
            </div>
        </div>
    </main>

    <footer>
        <p>&copy; 2026 Frontend Project. All rights reserved.</p>
        <p>Created with HTML, CSS, and JavaScript</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

    # Login page
    login_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Login - Frontend Project</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Frontend Project</h1>
            <nav>
                <a href="index.html">Home</a>
                <a href="register.html">Register</a>
                <a href="login.html">Login</a>
                <a href="contact.html">Contact</a>
            </nav>
        </div>
    </header>

    <main>
        <div class="container">
            <div class="form-card">
                <h2>Sign In</h2>
                <form id="loginForm" onsubmit="handleLoginSubmit(event)">
                    <div class="form-group">
                        <label for="loginEmail">Email Address</label>
                        <input type="email" id="loginEmail" name="loginEmail" placeholder="Enter your email">
                    </div>

                    <div class="form-group">
                        <label for="loginPassword">Password</label>
                        <input type="password" id="loginPassword" name="loginPassword" placeholder="Enter your password">
                    </div>

                    <div class="form-group" style="text-align: right;">
                        <a href="#" style="color: #667eea; text-decoration: none; font-size: 0.9rem;">Forgot password?</a>
                    </div>

                    <div class="form-actions">
                        <button type="submit" class="btn btn-primary">Login</button>
                        <a href="index.html" class="btn btn-secondary">Cancel</a>
                    </div>
                </form>

                <p style="text-align: center; margin-top: 20px; color: #666;">
                    Don't have an account? <a href="register.html" style="color: #667eea; text-decoration: none; font-weight: bold;">Register here</a>
                </p>
            </div>
        </div>
    </main>

    <footer>
        <p>&copy; 2026 Frontend Project. All rights reserved.</p>
        <p>Created with HTML, CSS, and JavaScript</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

    # Contact page
    contact_content = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contact - Frontend Project</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <header>
        <div class="container">
            <h1>Frontend Project</h1>
            <nav>
                <a href="index.html">Home</a>
                <a href="register.html">Register</a>
                <a href="login.html">Login</a>
                <a href="contact.html">Contact</a>
            </nav>
        </div>
    </header>

    <main>
        <div class="container">
            <div class="form-card">
                <h2>Contact Us</h2>
                <form id="contactForm" onsubmit="handleContactSubmit(event)">
                    <div class="form-group">
                        <label for="contactName">Full Name</label>
                        <input type="text" id="contactName" name="contactName" placeholder="Enter your full name">
                    </div>

                    <div class="form-group">
                        <label for="contactEmail">Email Address</label>
                        <input type="email" id="contactEmail" name="contactEmail" placeholder="Enter your email">
                    </div>

                    <div class="form-group">
                        <label for="subject">Subject</label>
                        <input type="text" id="subject" name="subject" placeholder="Enter subject">
                    </div>

                    <div class="form-group">
                        <label for="category">Category</label>
                        <select id="category" name="category">
                            <option value="">Select a category</option>
                            <option value="support">Support</option>
                            <option value="feedback">Feedback</option>
                            <option value="inquiry">Inquiry</option>
                            <option value="other">Other</option>
                        </select>
                    </div>

                    <div class="form-group">
                        <label for="message">Message</label>
                        <textarea id="message" name="message" placeholder="Enter your message"></textarea>
                    </div>

                    <div class="form-actions">
                        <button type="submit" class="btn btn-primary">Send Message</button>
                        <button type="reset" class="btn btn-secondary">Clear</button>
                    </div>
                </form>
            </div>

            <section class="info-section">
                <h3>Get in Touch</h3>
                <p><strong>Email:</strong> contact@example.com</p>
                <p><strong>Phone:</strong> +1 (555) 123-4567</p>
                <p><strong>Address:</strong> 123 Main Street, City, State 12345</p>
                <p><strong>Working Hours:</strong> Monday - Friday, 9:00 AM - 6:00 PM</p>
            </section>
        </div>
    </main>

    <footer>
        <p>&copy; 2026 Frontend Project. All rights reserved.</p>
        <p>Created with HTML, CSS, and JavaScript</p>
    </footer>

    <script src="script.js"></script>
</body>
</html>'''

    # Write all files
    files = {
        'styles.css': css_content,
        'script.js': js_content,
        'index.html': home_content,
        'register.html': register_content,
        'login.html': login_content,
        'contact.html': contact_content,
    }
    paths = {}
    for filename, content in files.items():
        filepath = os.path.join(target_dir, filename)
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(content)
        paths[filename] = filepath
    return paths
def open_file(path: str) -> None:
    """Open HTML file in default browser."""
    try:
        webbrowser.open('file://' + os.path.abspath(path).replace('\\', '/'))
    except Exception:
        try:
            os.startfile(path)
        except Exception:
            print('Could not open file automatically:', path)
def main():
    parser = argparse.ArgumentParser(description='Generate frontend project with home, register, login, and contact pages')
    parser.add_argument('--open', action='store_true', help='Open index.html after creating')
    args = parser.parse_args()
    base = os.path.dirname(__file__)
    paths = create_frontend_project(base)
    print('Frontend project created successfully!')
    for filename, path in paths.items():
        print(f'  Created: {filename}')
    if args.open:
        open_file(paths['index.html'])
if __name__ == '__main__':
    main()