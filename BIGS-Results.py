from flask import Flask, render_template, request

app = Flask(__name__)

course_map = {
    'A': "Game Design: Making a Difference",
    'B': "Streetwise: Designing the Future of Transportation",
    'C': "Think, Code, Create: Software Engineering with Python and AI",
    'D': "From Concept to Production: Sustainable Product Design",
    'E': "Taking Flight: Robotics in Aviation",
    'F': "Human Body Hacks: Engineering Biomedical Devices"
}

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    if request.method == 'POST':
        q0 = request.form.get('q0')
        q1 = request.form.get('q1')
        q2 = request.form.get('q2')
        q3 = request.form.get('q3')
        q4 = request.form.get('q4')
        q5 = request.form.get('q5')

        answers = [q0, q1, q2, q3, q4, q5]
        score = {'A': 0, 'B': 0, 'C': 0, 'D': 0, 'E': 0, 'F': 0}
        for ans in answers:
            if ans in score:
                score[ans] += 1
        top_choice = max(score, key=score.get)
        result = course_map[top_choice]
    return render_template('page1.html', result=result)

@app.route('/page2')
def page2():
    return render_template('page2.html')

@app.route('/quiz/<grade>/<question>')
def quiz_questions(grade, question):
    return render_template('question' + question + '(' + grade + ').html')

@app.route('/results.html')
def results():
    return render_template('results.html')

@app.route('/Static/styles.css')
def static_styles():
    return app.send_static_file('styles.css')

if __name__ == '__main__':
    app.run(debug=True)
