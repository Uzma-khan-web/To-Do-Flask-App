from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'your_secret_key'  # Required for flash messages

# Each task is a dictionary
tasks = []

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/todo')
def todo():
    return render_template('todo.html', tasks=tasks)

@app.route('/add', methods=['POST'])
def add():
    task_name = request.form.get('task')
    if task_name.strip():
        tasks.append({'name': task_name.strip(), 'done': False})
        flash('✅ Task added successfully!', 'success')
    else:
        flash('⚠️ Please enter a valid task.', 'warning')
    return redirect(url_for('todo'))

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        deleted = tasks.pop(task_id)
        flash(f'🗑️ Task "{deleted["name"]}" deleted.', 'danger')
    else:
        flash('❌ Invalid task ID.', 'danger')
    return redirect(url_for('todo'))

@app.route('/done/<int:task_id>')
def mark_done(task_id):
    if 0 <= task_id < len(tasks):
        tasks[task_id]['done'] = True
        flash(f'✅ Task "{tasks[task_id]["name"]}" marked as done.', 'success')
    else:
        flash('❌ Task not found.', 'danger')
    return redirect(url_for('todo'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
