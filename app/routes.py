from flask import render_template, request, redirect, url_for
from app import app, db
from app.models import ExamResult

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        student_id = request.form['student_id']
        result = ExamResult.query.filter_by(student_id=student_id).first()
        return render_template('index.html', result=result)
    return render_template('index.html')

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        student_id = request.form['student_id']
        new_result = ExamResult(
            student_id=student_id,
            math=request.form['math'],
            science=request.form['science'],
            english=request.form['english'],
            history=request.form['history'],
            geography=request.form['geography'],
            physics=request.form['physics'],
            chemistry=request.form['chemistry'],
            biology=request.form['biology'],
            computer_science=request.form['computer_science'],
            art=request.form['art'],
            music=request.form['music'],
            physical_education=request.form['physical_education'],
            economics=request.form['economics'],
            business_studies=request.form['business_studies'],
            foreign_language=request.form['foreign_language']
        )
        db.session.add(new_result)
        db.session.commit()
        return redirect(url_for('admin'))
    results = ExamResult.query.all()
    return render_template('admin.html', results=results)

@app.route('/delete/<int:id>')
def delete_result(id):
    result = ExamResult.query.get_or_404(id)
    db.session.delete(result)
    db.session.commit()
    return redirect(url_for('admin'))