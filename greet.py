from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def greet():
    team_members = [
        {"name": "Akhil", "role": "Developer"},
        {"name": "Pavan", "role": "Designer"},
        {"name": "Icon", "role": "Project Manager"}
    ]
    return render_template('welcome.html', team_members=team_members)

@app.route('/member/<name_role>')
def about_member(name_role):
    name, role = name_role.split('-')
    return render_template('about_member.html', name=name, role=role)

if __name__ == '__main__':
    app.run(debug=False, host="0.0.0.0", port=5000)
    