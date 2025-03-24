from flask import Flask, request, jsonify, render_template

app = Flask(__name__, static_folder='static', template_folder='templates')

@app.route('/')
def home():
    return render_template('index.html')

# Function to handle arithmetic operations
def calculate(num1, num2, operation):
    try:
        num1 = float(num1)
        num2 = float(num2)

        if operation == 'add':
            return {'result': num1 + num2}
        elif operation == 'subtract':
            return {'result': num1 - num2}
        elif operation == 'multiply':
            return {'result': num1 * num2}
        elif operation == 'divide':
            if num2 == 0:
                return {'error': 'Division by zero is not allowed.'}
            return {'result': num1 / num2}
        else:
            return {'error': 'Invalid operation.'}
    except ValueError:
        return {'error': 'Invalid input. Please provide valid numbers.'}

# Route to process operations
@app.route('/calculate', methods=['POST'])
def process_operation():
    try:
        data = request.json
        if not data:
            return jsonify({'error': 'No data provided.'}), 400

        num1 = data.get('num1')
        num2 = data.get('num2')
        operation = data.get('operation')

        if num1 is None or num2 is None or operation is None:
            return jsonify({'error': 'Missing input fields.'}), 400

        result = calculate(num1, num2, operation)
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': 'An unexpected error occurred.'}), 500

if __name__ == '__main__':
    app.run(debug=True)
