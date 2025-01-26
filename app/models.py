from app import db

class ExamResult(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    student_id = db.Column(db.String(20), unique=True, nullable=False)
    math = db.Column(db.String(5), nullable=False)
    science = db.Column(db.String(5), nullable=False)
    english = db.Column(db.String(5), nullable=False)
    history = db.Column(db.String(5), nullable=False)
    geography = db.Column(db.String(5), nullable=False)
    physics = db.Column(db.String(5), nullable=False)
    chemistry = db.Column(db.String(5), nullable=False)
    biology = db.Column(db.String(5), nullable=False)
    computer_science = db.Column(db.String(5), nullable=False)
    art = db.Column(db.String(5), nullable=False)
    music = db.Column(db.String(5), nullable=False)
    physical_education = db.Column(db.String(5), nullable=False)
    economics = db.Column(db.String(5), nullable=False)
    business_studies = db.Column(db.String(5), nullable=False)
    foreign_language = db.Column(db.String(5), nullable=False)

    def __repr__(self):
        return f"<ExamResult {self.student_id}>"