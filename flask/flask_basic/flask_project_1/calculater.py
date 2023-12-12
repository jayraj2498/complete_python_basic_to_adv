from flask import Flask, render_template, request

app = Flask(__name__)

# Your SimpleCalculator class
class SimpleCalculator:
    def add(self, num1, num2):
        """Perform addition."""
        return num1 + num2

    def subtract(self, num1, num2):
        """Perform subtraction."""
        return num1 - num2

    def multiply(self, num1, num2):
        """Perform multiplication."""
        return num1 * num2

    def divide(self, num1, num2):
        """
        Perform division.
        If the divisor is 0, display an error message and return None.
        """
        if num2 != 0:
            return num1 / num2
        else:
            print("Error: Division by zero.")
            return None

calculator = SimpleCalculator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    num1 = float(request.form['num1'])
    num2 = float(request.form['num2'])
    operation = request.form['operation']

    if operation == 'add':
        result = calculator.add(num1, num2)
        operation_str = '+'
    elif operation == 'subtract':
        result = calculator.subtract(num1, num2)
        operation_str = '-'
    elif operation == 'multiply':
        result = calculator.multiply(num1, num2)
        operation_str = '*'
    elif operation == 'divide':
        result = calculator.divide(num1, num2)
        if result is not None:
            operation_str = '/'
        else:
            return "Error: Division by zero"

    return render_template('result.html', num1=num1, num2=num2, operation=operation_str, result=result)

if __name__ == '__main__':
    app.run(debug=True)
