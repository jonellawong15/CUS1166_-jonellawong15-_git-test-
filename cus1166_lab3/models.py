from flask_sqlaclchemy import SQLAlchemy
db = SQLAlchemy()

class Course(db.Model):
    _tablename_= "courses"

    id = db.Column(db.Integer, primary_key = True)
    course_number = db.Column(db.String, nullable = False)
    course_title = db.Column(db.String, nullable = False)

    students = db.relationship("Student", backref="courses", lazy=True)
    professor = db.relationship("Professor", backref="courses", lazy=True)

    def add_student(self, name, seat):
        new_student = Student(name=name,seat=seat,id=self.id)
        db.session.add(new_student)
        db.session.commit()
    def add_professor(self,name):
        new_professor = Professor(name=name, id=self.id)
        db.session.add(new_professor)
        db.session.commit()


    class RegisteredStudent(db.Model):
        _tablename_= "registeredstudents"

        id = db.Column(db.Integer, primary_key = True)
        name = db.Column(db.String, nullable = False)
        grade = db.Column(db.Integer, nullable = False)

