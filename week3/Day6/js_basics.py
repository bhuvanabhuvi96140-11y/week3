import os
import webbrowser
import argparse

def create_demo_files(target_dir: str) -> tuple:
    """Create index.html, script.js, and styles.css for JavaScript basics demo."""
    
    html_content = '''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>JavaScript Basics Demo</title>
  <link rel="stylesheet" href="styles.css">
</head>
<body>
  <div class="container">
    <h1>JavaScript Basics Tutorial</h1>

    <!-- 1. Alert on Button Click -->
    <div class="demo-section">
      <h2>1. Alert on Button Click</h2>
      <p>Click the button below to display a JavaScript alert.</p>
      <button id="alertBtn" onclick="showAlert()">Click for Alert</button>
    </div>

    <!-- 2. Change Text on Click -->
    <div class="demo-section">
      <h2>2. Change Text on Click</h2>
      <p>Click the text below to change it dynamically.</p>
      <div id="changeText" onclick="changeText()">Click me to change text!</div>
    </div>

    <!-- 3. Form Validation -->
    <div class="demo-section">
      <h2>3. Form Validation</h2>
      <p>Fill out the form and submit. JavaScript will validate your input.</p>
      <form id="formValidation" onsubmit="validateForm(event)">
        <div class="form-group">
          <label for="fullName">Full Name:</label>
          <input type="text" id="fullName" name="fullName" placeholder="Enter your name">
          <div class="error-text" id="nameError"></div>
        </div>

        <div class="form-group">
          <label for="email">Email:</label>
          <input type="email" id="email" name="email" placeholder="Enter your email">
          <div class="error-text" id="emailError"></div>
        </div>

        <div class="form-group">
          <label for="password">Password:</label>
          <input type="password" id="password" name="password" placeholder="Enter password (min 6 chars)">
          <div class="error-text" id="passwordError"></div>
        </div>

        <button type="submit" class="submit-btn">Submit Form</button>
        <div id="formMessage"></div>
      </form>
    </div>

    <!-- 4. Simple Calculator -->
    <div class="demo-section">
      <h2>4. Simple Calculator</h2>
      <p>Perform basic math operations (+, -, *, /).</p>
      <div class="calc-container">
        <input type="text" id="calcDisplay" placeholder="0" readonly>
        <div class="calc-buttons">
          <button class="calc-btn num" onclick="appendToDisplay('7')">7</button>
          <button class="calc-btn num" onclick="appendToDisplay('8')">8</button>
          <button class="calc-btn num" onclick="appendToDisplay('9')">9</button>
          <button class="calc-btn op" onclick="appendToDisplay('/')">/</button>

          <button class="calc-btn num" onclick="appendToDisplay('4')">4</button>
          <button class="calc-btn num" onclick="appendToDisplay('5')">5</button>
          <button class="calc-btn num" onclick="appendToDisplay('6')">6</button>
          <button class="calc-btn op" onclick="appendToDisplay('*')">*</button>

          <button class="calc-btn num" onclick="appendToDisplay('1')">1</button>
          <button class="calc-btn num" onclick="appendToDisplay('2')">2</button>
          <button class="calc-btn num" onclick="appendToDisplay('3')">3</button>
          <button class="calc-btn op" onclick="appendToDisplay('-')">-</button>

          <button class="calc-btn num" onclick="appendToDisplay('0')">0</button>
          <button class="calc-btn num" onclick="appendToDisplay('.')">.</button>
          <button class="calc-btn op" onclick="appendToDisplay('+')">+</button>
          <button class="calc-btn op" onclick="calculateResult()">=</button>

          <button class="calc-btn clear" onclick="clearDisplay()">Clear</button>
          <button class="calc-btn delete" onclick="deleteLastChar()">Delete</button>
        </div>
        <div id="calcResult"></div>
      </div>
    </div>
  </div>

  <script src="script.js"></script>
</body>
</html>'''

    js_content = '''// Alert on button click
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
    const emailPattern = /^[^\\s@]+@[^\\s@]+\\.[^\\s@]+$/;
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
}'''
    css_content = '''*{margin:0;padding:0;box-sizing:border-box}
body{font-family:Segoe UI,Arial,Helvetica,sans-serif;background:#f2f4f6;padding:20px}
.container{max-width:1000px;margin:0 auto}
h1{text-align:center;color:#0b79d0;margin-bottom:30px}
.demo-section{background:#fff;padding:20px;margin-bottom:20px;border-radius:8px;box-shadow:0 2px 4px rgba(0,0,0,0.1)}
.demo-section h2{color:#333;margin-bottom:12px;font-size:1.3rem;border-bottom:2px solid #0b79d0;padding-bottom:8px}
.demo-section p{color:#666;margin-bottom:12px;line-height:1.6}

/* Alert Demo */
#alertBtn{background:#0b79d0;color:#fff;padding:10px 20px;border:none;border-radius:4px;cursor:pointer;font-size:1rem;transition:background 0.3s}
#alertBtn:hover{background:#0956a0}

/* Change Text Demo */
#changeText{background:#fff3cd;color:#333;padding:15px;border-radius:4px;cursor:pointer;transition:all 0.3s;text-align:center;font-weight:bold;border:2px solid #ffc107}
#changeText:hover{background:#ffe082;transform:scale(1.05)}

/* Form Validation */
.form-group{margin-bottom:15px}
label{display:block;margin-bottom:5px;color:#333;font-weight:bold}
input[type="text"],input[type="email"],input[type="password"]{width:100%;padding:8px 12px;border:1px solid #ddd;border-radius:4px;font-size:0.95rem}
input:focus{outline:none;border-color:#0b79d0;box-shadow:0 0 5px rgba(11,121,208,0.3)}
.error-text{color:#dc3545;font-size:0.9rem;margin-top:3px}
.submit-btn{background:#28a745;color:#fff;padding:10px 20px;border:none;border-radius:4px;cursor:pointer;font-size:1rem;transition:background 0.3s;width:100%}
.submit-btn:hover{background:#218838}
#formMessage{margin-top:15px;padding:10px;border-radius:4px;text-align:center;font-weight:bold}

/* Calculator */
.calc-container{max-width:300px;background:#333;padding:15px;border-radius:8px;margin:0 auto}
#calcDisplay{width:100%;padding:10px;font-size:1.5rem;border:2px solid #0b79d0;border-radius:4px;background:#444;color:#fff;text-align:right;margin-bottom:10px}
.calc-buttons{display:grid;grid-template-columns:repeat(4,1fr);gap:8px;margin-bottom:10px}
.calc-btn{padding:15px;font-size:1.1rem;border:none;border-radius:4px;cursor:pointer;transition:background 0.2s;font-weight:bold}
.calc-btn.num{background:#555;color:#fff}
.calc-btn.num:hover{background:#666}
.calc-btn.op{background:#0b79d0;color:#fff}
.calc-btn.op:hover{background:#0956a0}
.calc-btn.clear{background:#dc3545;color:#fff;grid-column:span 2}
.calc-btn.clear:hover{background:#c82333}
.calc-btn.delete{background:#ffc107;color:#333;grid-column:span 2}
.calc-btn.delete:hover{background:#ffb700}
#calcResult{background:#ffc107;color:#333;padding:10px;border-radius:4px;text-align:center;font-weight:bold}'''

    # Write files
    html_path = os.path.join(target_dir, 'index.html')
    js_path = os.path.join(target_dir, 'script.js')
    css_path = os.path.join(target_dir, 'styles.css')
    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    with open(js_path, 'w', encoding='utf-8') as f:
        f.write(js_content)
    with open(css_path, 'w', encoding='utf-8') as f:
        f.write(css_content)
    return html_path, js_path, css_path
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
    parser = argparse.ArgumentParser(description='Generate JavaScript Basics demo files')
    parser.add_argument('--open', action='store_true', help='Open index.html after creating')
    args = parser.parse_args()
    base = os.path.dirname(__file__)
    html_path, js_path, css_path = create_demo_files(base)
    print('Created:', html_path)
    print('Created:', js_path)
    print('Created:', css_path)
    if args.open:
        open_file(html_path)
if __name__ == '__main__':
    main()