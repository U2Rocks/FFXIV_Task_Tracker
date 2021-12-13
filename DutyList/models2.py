from DutyList import db


class Duty(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    duty_name = db.Column(db.String(length=100), nullable=False, unique=True)
    duty_type = db.Column(db.String(length=100), nullable=False)
    duty_level = db.Column(db.Integer(), nullable=False)
    duty_expansion = db.Column(db.String(length=70), nullable=False)
    duty_complete = db.Column(db.String(length=70))

    def __repr__(self):
        return f'Duty {self.duty_name}'

class ExpansionStatus(db.Model):
    exp_id = db.Column(db.Integer(), primary_key=True)
    exp_name = db.Column(db.String(length=100), nullable=False, unique=True)
    exp_status = db.Column(db.String(length=50), nullable=False)

    def __repr__(self):
        return f'Expansion {self.exp_name}'