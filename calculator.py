"""
PROGRAM: Basic Calculator
AUTHORS: Vraj Patel, Lithurshanan Sureskumar
DESCRIPTION: 1st Collobaorative Project, Basic Calculator Application
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    try:
        # force=True ensures Flask reads the text securely
        data = request.get_json(force=True)
        expression = data.get('expression', '')
        
        # Clean up the string just in case
        expression = expression.strip()
        
        # If the user clicks nothing, return empty
        if not expression:
            return jsonify({'success': True, 'result': ''})

        # Evaluate the math expression securely behind the scenes
        # This automatically handles +, -, *, and /
        result = str(eval(expression))
        return jsonify({'success': True, 'result': result})
        
    except Exception as e:
        print(f"Backend Math Error: {e}") # This prints to your black terminal window
        return jsonify({'success': False, 'result': 'Error'})

if __name__ == '__main__':
    app.run(debug=True)



#Title
print("------ CALCULATOR -----")

restart = "y"

while restart.lower() == "y":
    # User's Input
    Calculator_Function = int(input("Please select what math operation you would like to use: \n 1. Addition \n 2. Subtraction \n 3. Multiplication \n 4. Divison \n Enter your option (1-4): "))
    
# If the user put's selects incorrect input
    while Calculator_Function < 1 or Calculator_Function > 4:
        print("Invalid selection. Please try again")
        Calculator_Function = int(input("Please select what math operation you would like to use: \n" 
        " 1. Addition \n" 
        " 2. Subtraction \n" 
        " 3. Multiplication \n" 
        " 4. Divison\n" 
        "Enter your option (1-4): "))

    if Calculator_Function == 1:
        num1 = float(input("You have selected addition, please enter number 1: "))
        num2 = float(input("Please enter number 2: "))
        sum = num1 + num2
        print(f"The sum of {num1} + {num2} is {sum}")
    elif Calculator_Function == 2:
        num1 = float(input("You have selected subtraction, please enter number 1: "))
        num2 = float(input("Please enter number 2: "))
        difference = num1 - num2
        print(f"The difference of {num1} - {num2} is {difference}")
        
    elif Calculator_Function == 3:
        num1 = float(input("You have selected multiplication, please enter number 1: "))
        num2 = float(input("Please enter number 2: "))
        product = num1 * num2
        print(f"The product of {num1} * {num2} is {product}")
    elif Calculator_Function == 4:
        division_input = int(input("You have selected division, please select which type of division: \n"
        " 1. Floor Division \n"
        " 2. Regular Division \n" 
        " 3. Modulo \n"
        "Enter your option (1-3): "))

        if division_input == 1:
            num1 = float(input("You have selected Floor Division, please enter the number for the dividend: "))
            num2 = float(input("You have selected Floor Division, please enter the number for the divisor: "))
            quotient = num1 // num2
            print(f"The quotient of {num1} and {num2} is {quotient}")
        elif division_input == 2:
            num1 = float(input("You have selected Regular Division, please enter the number for the dividend: "))
            num2 = float(input("You have selected Regular Division, please enter the number for the divisor: "))
            quotient = num1 / num2
            print(f"The quotient of {num1} and {num2} is {quotient}")
        elif division_input == 3:
            num1 = float(input("You have selected Modulo Division, please enter the number for the dividend: "))
            num2 = float(input("You have selected Modulo Division, please enter the number for the divisor: "))
            quotient = num1 % num2
            print (f"The quotient is of {num1} and {num2} is {quotient}")
    

    restart = input("Would you like to do another calculation? (y/n): ")

print("Goodbye")
    
        
        




















