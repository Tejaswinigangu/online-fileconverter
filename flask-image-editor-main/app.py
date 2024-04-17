from flask import Flask, render_template, request, jsonify 
import openai 
  
  
app = Flask(__name__) 
  
# OpenAI API Key 
openai.api_key = 'YOUR_API_KEY'
  
def get_completion(prompt): 
    print(prompt) 
    query = openai.Completion.create( 
        engine="text-davinci-003", 
        prompt=prompt, 
        max_tokens=1024, 
        n=1, 
        stop=None, 
        temperature=0.5, 
    ) 
  
    response = query.choices[0].text 
    return response 
  
@app.route("/", methods=['POST', 'GET']) 
def query_view(): 
    if request.method == 'POST': 
        print('step1') 
        prompt = request.form['prompt'] 
        response = get_completion(prompt) 
        print(response) 
  
        return jsonify({'response': response}) 
    return render_template('index.html') 
  
  
if __name__ == "__main__": 
    app.run(debug=True) 



    from flask import Flask, render_template, request
from pymongo import MongoClient

app = Flask(__name__)
client = MongoClient('mongodb://localhost:27017/')
db = client['contact_form']
collection = db['submissions']

@app.route('/')
def index():
    submissions = list(collection.find())
    return render_template('submissions.html', submissions=submissions)

@app.route('/submissions', methods=['POST'])
def submit_form():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        
        # Insert form data into MongoDB
        collection.insert_one({'name': name, 'email': email, 'message': message})
        
        # Print received form data for debugging
        print(f"Received form data: Name={name}, Email={email}, Message={message}")

        # Redirect to the home page after form submission
        return "Form submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)




