from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
# Enable CORS so the static HTML frontend can send requests
CORS(app)

@app.route('/api/test-drive', methods=['POST'])
def test_drive():
    try:
        data = request.json
        name = data.get('name')
        phone = data.get('phone')
        
        if not name or not phone:
            return jsonify({"error": "Name and phone number are required"}), 400
            
        with open('leads.txt', 'a', encoding='utf-8') as f:
            f.write(f"Name: {name}, Phone: {phone}\n")
            
        return jsonify({"message": "Successfully saved lead"}), 200
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    # Run slightly on specific port to test
    app.run(debug=True, port=5000)
