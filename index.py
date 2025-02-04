import ollama
from flask import Flask, jsonify, request
from flask_restful import Api, Resource

app = Flask(__name__) 
api = Api(app) 

class ChatRequest(Resource):
    def post(self):
        # Get message content from the request JSON
        data = request.json  
        user_message = data.get("message")  # Default to "Hello" if not provided
        
        # Call Ollama chat API
        response = ollama.chat(
            model="deepseek-coder", 
            messages=[{"role": "user", "content": user_message}]
        )
        
        # Extract and return the response message
        return jsonify({"response": response["message"]["content"]})

# Add the resource to the API
api.add_resource(ChatRequest, '/chat')

if __name__ == '__main__':
    app.run(debug=True)
