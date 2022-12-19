from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=False, nullable=False)
    is_active = db.Column(db.Boolean(), unique=False, nullable=False)

    def __repr__(self):
        return f'<User {self.email}>'

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Todos(db.Model):
    __tablename__ = "todos"
    id = db.Column(db.Integer, primary_key = True)
    label = db.Column(db.String(50), nullable = False) 
    done = db.Column(db.Boolean(), nullable = False)
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))
    user = db.relationship(User)

    def __repr__(self):
        return f'<Todos {self.id}>'

    def serialize(self):
        return {
            "label": self.label,
            "done": self.done,
            "user_id":self.user_id,
        }

