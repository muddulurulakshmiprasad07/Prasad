# user_name=input("enter your name")
# user_password=input("enter your password")
# inbuid_user_name="prasad"
# inbuid_user_password="prasad123"
# if user_name == inbuid_user_name and user_password == inbuid_user_password:
#     print("loginsuccesful")
# else:
#     print("invalid username or incorrect password")  #create password


# from flask import Flask, request, render_template_string

# app = Flask(__name__)

# # Built-in login credentials
# inbuid_user_name = "prasad"
# inbuid_user_password = "prasad123"

# HTML = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Cinematic Login</title>

#     <style>
#         * {
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#             font-family: Arial, sans-serif;
#         }

#         body {
#             min-height: 100vh;
#             display: flex;
#             justify-content: center;
#             align-items: center;
#             background:
#                 linear-gradient(rgba(5, 10, 25, 0.55),
#                                 rgba(5, 10, 25, 0.8)),
#                 url("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcS2hNgQ0TP-Lyc_fNij7aYSJresD3-J3A_sQ2ek8WnH2g&s");
#             background-size: cover;
#             background-position: center;
#             background-attachment: fixed;
#         }

#         .login-box {
#             width: 360px;
#             padding: 38px 30px;
#             border: 1px solid rgba(255,255,255,0.3);
#             border-radius: 20px;
#             background: rgba(255,255,255,0.10);
#             backdrop-filter: blur(15px);
#             box-shadow: 0 10px 40px rgba(0,0,0,0.5);
#             color: white;
#             text-align: center;
#         }

#         .icon {
#             font-size: 48px;
#             margin-bottom: 12px;
#         }

#         h1 {
#             font-size: 29px;
#             margin-bottom: 10px;
#         }

#         .subtitle {
#             color: #d5dbea;
#             margin-bottom: 28px;
#             font-size: 14px;
#         }

#         .input-box {
#             text-align: left;
#             margin-bottom: 20px;
#         }

#         label {
#             display: block;
#             margin-bottom: 8px;
#             font-size: 14px;
#         }

#         input {
#             width: 100%;
#             padding: 13px;
#             border: 1px solid rgba(255,255,255,0.4);
#             border-radius: 9px;
#             outline: none;
#             background: rgba(255,255,255,0.12);
#             color: white;
#             font-size: 15px;
#         }

#         input::placeholder {
#             color: #d5dbea;
#         }

#         input:focus {
#             border-color: #65d9ff;
#             box-shadow: 0 0 8px rgba(101,217,255,0.5);
#         }

#         button {
#             width: 100%;
#             padding: 14px;
#             border: none;
#             border-radius: 9px;
#             background: linear-gradient(90deg, #00c6ff, #0072ff);
#             color: white;
#             font-size: 16px;
#             font-weight: bold;
#             cursor: pointer;
#             transition: 0.3s;
#         }

#         button:hover {
#             transform: translateY(-2px);
#             box-shadow: 0 5px 20px rgba(0,114,255,0.5);
#         }

#         .message {
#             margin-top: 18px;
#             padding: 12px;
#             border-radius: 8px;
#             font-size: 14px;
#         }

#         .success {
#             color: #b7ffca;
#             background: rgba(0,180,70,0.2);
#         }

#         .error {
#             color: #ffbaba;
#             background: rgba(255,0,0,0.2);
#         }

#         .footer {
#             margin-top: 25px;
#             color: #d5dbea;
#             font-size: 12px;
#         }

#         @media (max-width: 420px) {
#             .login-box {
#                 width: calc(100% - 32px);
#                 padding: 30px 22px;
#             }
#         }
#     </style>
# </head>

# <body>
#     <div class="login-box">
#         <div class="icon">🔐</div>
#         <h1>Welcome Back</h1>
#         <p class="subtitle">Login to access your account</p>

#         <form method="POST">
#             <div class="input-box">
#                 <label for="username">Username</label>
#                 <input type="text" id="username" name="username"
#                        placeholder="Enter your username" required>
#             </div>

#             <div class="input-box">
#                 <label for="password">Password</label>
#                 <input type="password" id="password" name="password"
#                        placeholder="Enter your password" required>
#             </div>

#             <button type="submit">LOGIN</button>
#         </form>

#         {% if message %}
#             <div class="message {{ status }}">{{ message }}</div>
#         {% endif %}

#         <p class="footer">Secure Login Portal</p>
#     </div>
# </body>
# </html>
# """

# @app.route("/", methods=["GET", "POST"])
# def login():
#     message = ""
#     status = ""

#     if request.method == "POST":
#         user_name = request.form.get("username", "")
#         user_password = request.form.get("password", "")

#         if (user_name == inbuid_user_name and
#                 user_password == inbuid_user_password):
#             message = "Login successful! Welcome, Prasad."
#             status = "success"
#         else:
#             message = "Invalid username or incorrect password."
#             status = "error"

#     return render_template_string(
#         HTML, message=message, status=status
#     )

# if __name__ == "__main__":
#     app.run(debug=True)  #create a website in chrome to enter password



