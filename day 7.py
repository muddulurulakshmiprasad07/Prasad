# # text="python"
# # print(text[0])
# # print(text[-1]) #indexing

# # text="python"
# # print(text[0:4]) #slicing

# # text="python"
# # print(text[0],text[-1]) #indexing1

# # q=input("what is capital of india").lower()
# # if q=="delhi":
# #     print("correct ans")
# # else:
# #     print("wrong ans") # lower inbuid functions

# # q=input("what is capital of AP").upper()
# # if q=="AMARAVATHI":
# #     print("correct ans")
# # else:
# #     print("wrong ans") # upper inbuild functions

# from flask import Flask, request, render_template_string, session

# app = Flask(__name__)
# app.secret_key = "my_unique_python_quiz_secret_2026"
# {
#         "question": "What is the capital of India?",
#         "answer": "delhi",
#         "hint": "Enter the capital city of India."
#     },
# {
#         "question": "What is the capital of Andhra Pradesh?",
#         "answer": "amaravati",
#         "hint": "Enter the capital city of Andhra Pradesh."
#     }

# HTML = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Cinematic Python Quiz</title>

#     <style>
#         * {
#             margin: 0;
#             padding: 0;
#             box-sizing: border-box;
#         }

#         body {
#             min-height: 100vh;
#             font-family: Arial, sans-serif;
#             color: white;
#             display: flex;
#             align-items: center;
#             justify-content: center;
#             background:
#                 radial-gradient(circle at top, #243b70, transparent 45%),
#                 linear-gradient(135deg, #050816, #111827, #090b18);
#             overflow-x: hidden;
#         }

#         .background-glow {
#             position: fixed;
#             width: 280px;
#             height: 280px;
#             background: #6c35ff;
#             filter: blur(130px);
#             opacity: 0.4;
#             top: 10%;
#             left: 5%;
#             z-index: -1;
#         }

#         .container {
#             width: 90%;
#             max-width: 550px;
#             padding: 40px;
#             border: 1px solid rgba(255,255,255,0.18);
#             border-radius: 25px;
#             background: rgba(255,255,255,0.07);
#             backdrop-filter: blur(18px);
#             box-shadow: 0 0 50px rgba(70, 80, 255, 0.18);
#             animation: appear 0.8s ease;
#         }

#         .tag {
#             color: #9eafff;
#             letter-spacing: 4px;
#             font-size: 12px;
#             text-align: center;
#             margin-bottom: 15px;
#         }

#         h1 {
#             text-align: center;
#             font-size: 34px;
#             margin-bottom: 12px;
#         }

#         .subtitle {
#             text-align: center;
#             color: #b7bfd7;
#             margin-bottom: 30px;
#             line-height: 1.6;
#         }

#         .progress {
#             height: 6px;
#             background: #30364e;
#             border-radius: 10px;
#             margin-bottom: 30px;
#             overflow: hidden;
#         }

#         .progress-bar {
#             height: 100%;
#             background: linear-gradient(90deg, #6d5dfc, #00e5ff);
#             transition: width 0.4s ease;
#         }

#         .question {
#             font-size: 22px;
#             line-height: 1.5;
#             margin-bottom: 22px;
#         }

#         input {
#             width: 100%;
#             padding: 16px;
#             color: white;
#             background: rgba(0,0,0,0.25);
#             border: 1px solid #596385;
#             border-radius: 12px;
#             font-size: 16px;
#             outline: none;
#             margin-bottom: 18px;
#         }

#         input:focus {
#             border-color: #00e5ff;
#             box-shadow: 0 0 15px rgba(0,229,255,0.2);
#         }

#         button {
#             width: 100%;
#             padding: 15px;
#             border: none;
#             border-radius: 12px;
#             color: white;
#             font-weight: bold;
#             font-size: 16px;
#             cursor: pointer;
#             background: linear-gradient(90deg, #6655ee, #398bff);
#             transition: 0.3s;
#         }

#         button:hover {
#             transform: translateY(-3px);
#             box-shadow: 0 8px 25px rgba(80,100,255,0.4);
#         }

#         .message {
#             margin-top: 22px;
#             text-align: center;
#             font-size: 17px;
#             line-height: 1.6;
#         }

#         .correct {
#             color: #5dffb0;
#         }

#         .wrong {
#             color: #ff8297;
#         }

#         .score {
#             color: #8ceaff;
#             text-align: center;
#             margin-top: 15px;
#         }

#         .footer {
#             text-align: center;
#             margin-top: 28px;
#             color: #858da8;
#             font-size: 12px;
#         }

#         @keyframes appear {
#             from {
#                 opacity: 0;
#                 transform: translateY(25px);
#             }
#             to {
#                 opacity: 1;
#                 transform: translateY(0);
#             }
#         }

#         @media (max-width: 480px) {
#             .container {
#                 padding: 25px;
#             }

#             h1 {
#                 font-size: 27px;
#             }

#             .question {
#                 font-size: 19px;
#             }
#         }
#     </style>
# </head>

# <body>
# <div class="background-glow"></div>

# <div class="container">
#     <div class="tag">PYTHON • FLASK • QUIZ</div>

#     <h1>Knowledge Quest</h1>

#     <p class="subtitle">
#         Test your knowledge.<br>
#         Learn Python through an interactive quiz.
#     </p>

#     <div class="progress">
#         <div class="progress-bar"
#              style="width: {{ progress }}%">
#         </div>
#     </div>

#     {% if finished %}
#         <h2 style="text-align:center;">Quiz Completed!</h2>

#         <p class="message correct">
#             Great job! You finished the quiz.
#         </p>

#         <p class="score">
#             Your score: {{ score }} / {{ total }}
#         </p>

#         <br>

#         <form method="POST">
#             <button type="submit" name="restart" value="yes">
#                 Play Again
#             </button>
#         </form>

#     {% else %}
#         <p class="tag" style="text-align:left;">
#             QUESTION {{ number }} OF {{ total }}
#         </p>

#         <div class="question">
#             {{ question }}
#         </div>

#         <form method="POST">
#             <input
#                 type="text"
#                 name="answer"
#                 placeholder="Type your answer..."
#                 required
#                 autocomplete="off"
#                 autofocus
#             >

#             <button type="submit">
#                 Submit Answer →
#             </button>
#         </form>

#         {% if message %}
#             <div class="message {{ result_class }}">
#                 {{ message }}
#             </div>
#         {% endif %}

#         <p class="score">Score: {{ score }} / {{ total }}</p>
#     {% endif %}

#     <div class="footer">
#         POWERED BY PYTHON & FLASK
#     </div>
# </div>
# </body>
# </html>
# """

# @app.route("/", methods=["GET", "POST"])
# def home():
#     # Keep your existing quiz logic here
#     return render_template_string(HTML)
# def home():
#     if request.method == "POST" and request.form.get("restart"):
#         return render_template_string(
#             HTML,
#             finished=False,
#             number=1,
#             total=len(questions),
#             question=questions[0]["question"],
#             score=0,
#             progress=0,
#             message="",
#             result_class=""
#         )

#     # Track quiz progress using the browser session form
#     from flask import session
#     app.secret_key = "python-quiz-demo-key"

#     if request.method == "GET":
#         session["index"] = 0
#         session["score"] = 0

#     index = session.get("index", 0)
#     score = session.get("score", 0)
#     message = ""
#     result_class = ""

#     if request.method == "POST":
#         answer = request.form.get("answer", "").strip()

#         if index < len(questions):
#             correct_answer = questions[index]["answer"]

#             # Using your Python lower() concept
#             if answer.lower() == correct_answer.lower():
#                 message = "✓ Correct answer! Well done!"
#                 result_class = "correct"
#                 score += 1
#             else:
#                 message = (
#                     "✗ Wrong answer! Correct answer: "
#                     + correct_answer.title()
#                 )
#                 result_class = "wrong"

#             session["score"] = score
#             session["index"] = index + 1
#             index += 1

#     if index >= len(questions):
#         return render_template_string(
#             HTML,
#             finished=True,
#             score=session.get("score", 0),
#             total=len(questions),
#             progress=100
#         )

#     return render_template_string(
#         HTML,
#         finished=False,
#         number=index + 1,
#         total=len(questions),
#         question=questions[index]["question"],
#         score=session.get("score", 0),
#         progress=(index / len(questions)) * 100,
#         message=message,
#         result_class=result_class
#     )


# if __name__ == "__main__":
#     app.run(debug=True) # server 





