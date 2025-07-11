import groq
import os
from flask import Flask, request, jsonify
from groq import Groq

from dotenv import load_dotenv
load_dotenv()

def modelo(pregunta):
    client = Groq(        
            api_key=os.environ.get("GROQ_API_KEY"),
        )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",  # eres mi profe de DS
                "content": pregunta,
            }
        ],
        model="llama-3.3-70b-versatile", # mistral-saba-24b
        stream=False,
    )
    return chat_completion.choices[0].message.content

app = Flask(__name__)
app.config['DEBUG'] =True

@app.route('/')
def main():
    return 'api de conex al LLM'


@app.route('/prompt/<string:preg>')
def prompt(preg):
    resp= modelo(preg)
    return resp


# @app.route('/prompt2/')
# def prompt2():
#     preg = request.args.get['`preg']
#     resp = modelo(preg)
#     return

app.run()