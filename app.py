from flask import Flask, render_template, request

app = Flask(__name__)
rows = []

@app.route("/",  methods=['GET', 'POST'])
def index():
    global rows
    # print(rows)
    if request.method == 'POST':
        rows.append(request.form.get("name"))
        
    return render_template('index.html', len_rows=len(rows), rows=rows)