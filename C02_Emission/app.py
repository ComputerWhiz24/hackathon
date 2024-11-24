from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)



@app.route('/')
def home():
    return render_template('home.html') 

@app.route('/calculator')
def calculator():
    return render_template('calculatorTest.html')  

@app.route('/calculate', methods=['POST'])
def calculate():
    user_input = request.json['query'] 
    if not user_input:
        return jsonify({'data': 'No query provided.'}), 400
    messages = [
        {"role": "system", "content": "You are an AI assistant that calculates CO2 emissions and " +
"I want a rough estimate of exactly how much CO2 is produced. Give me a single sentences describing how much is produced from what I describe and how. Add how I can"
+ "reduce my emissions"},
        {"role": "user", "content":  user_input}
    ]
    
    response = openai.ChatCompletion.create(
        model="gpt-4",  
        messages=messages,  
        max_tokens=200  
    )
    
    ai_response = response['choices'][0]['message']['content'] 

    return jsonify({'data': ai_response})


if __name__ == '__main__':
    app.run(debug=True)
