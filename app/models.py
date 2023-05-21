from app import db

class User(db.Model):
    __tablename__ = "User"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128), nullable=False)

    def __repr__(self):
        return '<User {}>'.format(self.name)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Farmer(db.Model):
    __tablename__ = "Farmer"
    id = db.Column(db.Integer, primary_key=True)
    location = db.Column(db.String, nullable=True)
    name = db.Column(db.String(120), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))
    phone = db.Column(db.String(40), nullable=True)

    def __repr__(self):
        return "<Farmer {}>".format(self.name)
