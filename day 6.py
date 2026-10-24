# for x in "1 2 3 4 5 6 ":
#     print(x) #for loop

# for x in range(3):
#     print(x) #range as stop 

# for x in range(3,7):
#     print(x) #range as start,stop

# for x in range(6,15,2):
#     print(x) #range as start,stop,step

# for x in "rama":
#     if x=="m":
#        break
#     else:
#         print(x) # break statement

# for x in "rama":
#     if x=="m":
#         pass
#     else:
#         print(x) # pass statement

# ctr=0
# while ctr<5:
#    print(ctr)
#    ctr+=1 # while loop

# correct_password="admin123"
# for attempt in range(1,4):
#     password=input("enter your password:")
#     if password==correct_password:
#         print("login succesful")
#         break
#     else:
#         print("wrong password")
#         if attempt==3:
#             print("account locked") # for loop 


# from flask import Flask, request, render_template_string

# app = Flask(__name__)

# HTML = """
# <!DOCTYPE html>
# <html>
# <head>
# <title>Python Loops Playground</title>
# <style>
# body {
#     font-family: Arial, sans-serif;
#     background: #0f172a;
#     color: white;
#     padding: 30px;
# }
# .container {
#     max-width: 700px;
#     margin: auto;
# }
# .card {
#     background: #1e293b;
#     padding: 25px;
#     border-radius: 15px;
#     margin-bottom: 20px;
# }
# h1 { color: #38bdf8; text-align: center; }
# label { display: block; margin: 12px 0; }
# select, input, button {
#     width: 100%;
#     padding: 12px;
#     margin-bottom: 12px;
#     border-radius: 7px;
#     border: none;
#     box-sizing: border-box;
# }
# button {
#     background: #38bdf8;
#     font-weight: bold;
#     cursor: pointer;
# }
# button:hover { background: #7dd3fc; }
# pre {
#     background: #020617;
#     color: #4ade80;
#     padding: 18px;
#     border-radius: 8px;
#     white-space: pre-wrap;
# }
# p { color: #cbd5e1; }
# </style>
# </head>
# <body>
# <div class="container">
#     <h1>Python Loops Playground</h1>
#     <p style="text-align:center">Learn Python loops interactively</p>

#     <div class="card">
#         <h2>Explore Python Loops</h2>
#         <form method="POST">
#             <input type="hidden" name="action" value="loop">
#             <label>Select an example:</label>
#             <select name="example">
#                 <option value="string">For Loop - String</option>
#                 <option value="range">Range (3)</option>
#                 <option value="startstop">Range (3, 7)</option>
#                 <option value="step">Range (6, 15, 2)</option>
#                 <option value="break">Break Statement</option>
#                 <option value="pass">Pass Statement</option>
#                 <option value="while">While Loop</option>
#             </select>
#             <button type="submit">Run Python Code</button>
#         </form>

#         <h3>Output:</h3>
#         <pre>{{ result }}</pre>
#     </div>

#     <div class="card">
#         <h2>Password Login</h2>
#         <p>Demo password: admin123</p>
#         <form method="POST">
#             <input type="hidden" name="action" value="login">
#             <input type="password" name="password"
#                    placeholder="Enter password" required>
#             <button type="submit">Login</button>
#         </form>
#         <pre>{{ login_result }}</pre>
#     </div>
# </div>
# </body>
# </html>
# """

# def run_loop(example):
#     output = []

#     if example == "string":
#         for x in "1 2 3 4 5 6 ":
#             output.append(x)

#     elif example == "range":
#         for x in range(3):
#             output.append(x)

#     elif example == "startstop":
#         for x in range(3, 7):
#             output.append(x)

#     elif example == "step":
#         for x in range(6, 15, 2):
#             output.append(x)

#     elif example == "break":
#         for x in "rama":
#             if x == "m":
#                 break
#             else:
#                 output.append(x)

#     elif example == "pass":
#         for x in "rama":
#             if x == "m":
#                 pass
#             else:
#                 output.append(x)

#     elif example == "while":
#         ctr = 0
#         while ctr < 5:
#             output.append(ctr)
#             ctr += 1

#     return "\\n".join(map(str, output))


# @app.route("/", methods=["GET", "POST"])
# def home():
#     result = "Select a loop and click Run Python Code."
#     login_result = "Login output appears here."

#     if request.method == "POST":
#         if request.form.get("action") == "loop":
#             result = run_loop(request.form.get("example", ""))

#         elif request.form.get("action") == "login":
#             password = request.form.get("password", "")

#             if password == "admin123":
#                 login_result = "Login successful!"
#             else:
#                 login_result = "Wrong password."

#     return render_template_string(
#         HTML, result=result, login_result=login_result
#     )


# if __name__ == "__main__":
#     app.run(debug=True)  # for loop example1


# from flask import Flask, request, render_template_string
# from io import StringIO
# from contextlib import redirect_stdout

# app = Flask(__name__)

# examples = {
#     "1": {
#         "title": "Loop Through a String",
#         "code": 'for x in "123456":\n    print(x)',
#         "description": "Print each character in a string."
#     },
#     "2": {
#         "title": "Range from Zero",
#         "code": "for x in range(3):\n    print(x)",
#         "description": "Print numbers from 0 to 2."
#     },
#     "3": {
#         "title": "Range with Start and Stop",
#         "code": "for x in range(3, 7):\n    print(x)",
#         "description": "Print numbers from 3 to 6."
#     },
#     "4": {
#         "title": "Range from 6 to 14",
#         "code": "for x in range(6, 15):\n    print(x)",
#         "description": "Print numbers from 6 to 14."
#     },
#     "5": {
#         "title": "Loop Through a List",
#         "code": 'for x in ["Python", "Flask", "HTML", "CSS"]:\n    print(x)',
#         "description": "Print each item in a list."
#     }
# }

# HTML = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
# <meta charset="UTF-8">
# <meta name="viewport" content="width=device-width, initial-scale=1.0">
# <title>Cinematic Python Lab</title>
# <style>
# * {
#     margin: 0;
#     padding: 0;
#     box-sizing: border-box;
# }

# body {
#     font-family: Consolas, monospace;
#     background: #050713;
#     color: #eef5ff;
#     min-height: 100vh;
#     overflow-x: hidden;
# }

# body::before {
#     content: "";
#     position: fixed;
#     inset: 0;
#     background:
#         radial-gradient(ellipse at 15% 20%, #123a6a88, transparent 45%),
#         radial-gradient(ellipse at 85% 80%, #561c7380, transparent 40%);
#     pointer-events: none;
#     z-index: -1;
# }

# nav {
#     padding: 22px 8%;
#     display: flex;
#     justify-content: space-between;
#     align-items: center;
#     border-bottom: 1px solid #ffffff15;
#     background: #070a16bb;
# }

# .logo {
#     font-size: 20px;
#     font-weight: bold;
#     color: #60eaff;
#     letter-spacing: 2px;
# }

# nav span {
#     color: #aab7d1;
#     font-size: 12px;
# }

# .hero {
#     text-align: center;
#     padding: 65px 20px 40px;
#     animation: appear 1s ease;
# }

# .tag {
#     color: #63efff;
#     border: 1px solid #63efff66;
#     padding: 8px 15px;
#     border-radius: 30px;
#     font-size: 11px;
#     letter-spacing: 2px;
# }

# h1 {
#     margin: 28px 0 15px;
#     font-size: clamp(35px, 6vw, 68px);
#     letter-spacing: -2px;
#     background: linear-gradient(90deg, #ffffff, #63efff, #c69aff);
#     -webkit-background-clip: text;
#     -webkit-text-fill-color: transparent;
# }

# .hero p {
#     color: #a5b4d0;
#     line-height: 1.8;
#     font-size: 14px;
# }

# .container {
#     width: min(1100px, 90%);
#     margin: auto;
#     padding-bottom: 60px;
# }

# .grid {
#     display: grid;
#     grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
#     gap: 18px;
# }

# .card {
#     background: linear-gradient(145deg, #151c30dd, #0b1020ee);
#     border: 1px solid #ffffff19;
#     border-radius: 18px;
#     padding: 24px;
#     transition: .3s;
#     box-shadow: 0 10px 35px #00000020;
# }

# .card:hover {
#     transform: translateY(-6px);
#     border-color: #5eeaff88;
#     box-shadow: 0 0 28px #27d9ff15;
# }

# .number {
#     color: #63efff;
#     font-size: 12px;
#     letter-spacing: 2px;
# }

# h2 {
#     font-size: 18px;
#     margin: 15px 0 10px;
# }

# .card p {
#     color: #9eacc6;
#     font-size: 12px;
#     line-height: 1.7;
#     min-height: 35px;
# }

# pre {
#     background: #050914;
#     border: 1px solid #ffffff12;
#     padding: 16px;
#     margin: 18px 0;
#     border-radius: 10px;
#     color: #a8ffca;
#     font-size: 13px;
#     line-height: 1.8;
#     white-space: pre-wrap;
#     overflow-wrap: anywhere;
# }

# button {
#     width: 100%;
#     padding: 13px;
#     background: linear-gradient(90deg, #00c9e8, #8172ff);
#     border: none;
#     border-radius: 9px;
#     color: #050713;
#     font-family: inherit;
#     font-weight: bold;
#     cursor: pointer;
#     transition: .25s;
# }

# button:hover {
#     box-shadow: 0 0 22px #46dfff55;
#     transform: scale(1.02);
# }

# .output {
#     margin-top: 35px;
#     padding: 28px;
#     background: #080d1b;
#     border: 1px solid #63efff66;
#     border-radius: 18px;
#     box-shadow: 0 0 30px #00d9ff10;
# }

# .output h2 {
#     color: #63efff;
# }

# .output pre {
#     min-height: 90px;
#     color: #a8ffca;
# }

# .status {
#     color: #8dffbb;
#     font-size: 12px;
# }

# footer {
#     text-align: center;
#     padding: 25px;
#     color: #71809d;
#     border-top: 1px solid #ffffff12;
#     font-size: 11px;
#     letter-spacing: 1px;
# }

# @keyframes appear {
#     from { opacity: 0; transform: translateY(20px); }
#     to { opacity: 1; transform: translateY(0); }
# }

# @media (max-width: 600px) {
#     nav { padding: 18px 5%; }
#     .hero { padding-top: 45px; }
#     .container { width: 92%; }
# }
# </style>
# </head>
# <body>

# <nav>
#     <div class="logo">◈ PYTHON LAB</div>
#     <span>FLASK · LEARN · BUILD</span>
# </nav>

# <section class="hero">
#     <span class="tag">INTERACTIVE CODING EXPERIENCE</span>
#     <h1>Cinematic Loop Lab</h1>
#     <p>Explore Python for loops in a futuristic coding environment.<br>
#        Select an experiment and watch your output appear.</p>
# </section>

# <main class="container">
#     <div class="grid">
#         {% for key, item in examples.items() %}
#         <section class="card">
#             <span class="number">EXPERIMENT 0{{ key }}</span>
#             <h2>{{ item.title }}</h2>
#             <p>{{ item.description }}</p>
#             <pre>{{ item.code }}</pre>
#             <form method="POST">
#                 <input type="hidden" name="example" value="{{ key }}">
#                 <button type="submit">▶ RUN CODE</button>
#             </form>
#         </section>
#         {% endfor %}
#     </div>

#     <section class="output" id="output">
#         <h2>⌁ Terminal Output</h2>
#         {% if selected %}
#             <p class="status">● EXECUTION COMPLETED</p>
#             <pre>{{ result }}</pre>
#         {% else %}
#             <p>Choose an experiment above to see the result.</p>
#             <pre>Waiting for your code...</pre>
#         {% endif %}
#     </section>
# </main>

# <footer>PYTHON LOOP PLAYGROUND · POWERED BY FLASK</footer>

# {% if selected %}
# <script>
# window.addEventListener("load", function () {
#     document.getElementById("output").scrollIntoView({
#         behavior: "smooth",
#         block: "center"
#     });
# });
# </script>
# {% endif %}

# </body>
# </html>
# """

# @app.route("/", methods=["GET", "POST"])
# def home():
#     result = ""
#     selected = False

#     if request.method == "POST":
#         key = request.form.get("example", "")

#         if key in examples:
#             output = StringIO()
#             code = examples[key]["code"]

#             # Run only the predefined examples.
#             with redirect_stdout(output):
#                 exec(compile(code, "<loop-example>", "exec"), {})

#             result = output.getvalue()
#             selected = True

#     return render_template_string(
#         HTML,
#         examples=examples,
#         result=result,
#         selected=selected
#     )

# if __name__ == "__main__":
#     app.run(debug=True)  # cinematic design
