from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime
from bd import collection
from bson.objectid import ObjectId

app = Flask(__name__)

#tasks = []
date = datetime.now()
date_format = date.strftime(("%d %b"))


@app.route('/', methods=["GET","POST"])
def home():
    if request.method == "POST":
        task_content = request.form.get("content")
        collection.insert_one({"tasks":task_content})
        
    tasks_all = [
        (
            task["tasks"]
        )
        
        for task in collection.find({})
    ]
        
    qtd_tasks = len(tasks_all)
    return render_template('index.html', tasks=tasks_all,date_format=date_format, qtd_tasks=qtd_tasks)


@app.route('/delete')   
def delete_task():
    collection.find_one_and_delete({})
    return redirect('/')
    

if __name__ == "__main__":
    app.run(debug=True)
    