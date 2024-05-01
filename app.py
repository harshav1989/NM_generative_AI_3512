from flask import Flask, render_template, request, redirect, url_for
import google.generativeai as genai

app = Flask(__name__)

API_KEY = 'you_api_key'

# Configure the Gemini AI model with your API key
genai.configure(api_key=API_KEY)
model_name = 'gemini-1.0-pro'
gemini = genai.GenerativeModel(model_name)

# Define your 404 error handler to redirect to the index page
@app.errorhandler(404)
def page_not_found(e):
    return redirect(url_for('index'))

@app.route('/', methods=['POST', 'GET'])
def index():
    if request.method == 'POST':
        try:
            user_input = request.form['prompt']
            response = gemini.start_chat().send_message(user_input)
            return response.text
        except Exception as e:
            print("Exception:", e)  # Print the exception for debugging purposes
            return "Sorry, but Gemini didn't want to answer that!"

    return render_template('index.html', **locals())

if __name__ == '__main__':
    app.run(debug=True)
