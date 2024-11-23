from flask import Flask, render_template, request

app = Flask(__name__)

# Route to display the home page
@app.route('/')
def home():
    return render_template('home.html')

# Route to handle form submission and calculate CO2 emission
@app.route('/calculate', methods=['POST'])
def calculate_emission():
    # Get user input from the form
    distance = float(request.form['distance'])
    emission_factor = 0.3  # Example emission factor (you can change this)
    co2_emission = distance * emission_factor
    
    return render_template('home.html', co2_emission=co2_emission)

if __name__ == '__main__':
    app.run(debug=True)