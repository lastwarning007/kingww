from flask import Flask, request, jsonify
import PKK

app = Flask(__name__)

@app.route('/api/login', methods=['GET'])
def login():
    email_password = request.args.get('email_password')

    if not email_password or ':' not in email_password:
        return jsonify({"error": "Invalid input format. Use email:password"}), 400

    email, password = email_password.split(':', 1)

    try:
        hh = PKK.Hotmail.Login(email.strip(), password.strip())
        status = "Good" if hh.get('Login') == 'Good' else "Bad"
        return jsonify({"email": email, "status": status})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True)
