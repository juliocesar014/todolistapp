from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
app = Flask(__name__)

tasks = ['Teste01','Teste02','Teste03']
qtd_tasks = len(tasks)
date = datetime.now()
date_format = date.strftime(("%d %b"))
print(qtd_tasks)

@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        task_content = request.form.get("content")
        tasks.append((task_content))
        print(tasks)
        
    
    return render_template('index.html', tasks=tasks, qtd_tasks=qtd_tasks,date_format=date_format)


@app.route('/delete')   
def delete_task():
    return 'Delete'


if __name__ == "__main__":
    app.run(debug=True)