from flask import Flask, jsonify, request, abort
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from marshmallow import fields, ValidationError

# Initialize Flask application
app = Flask(__name__)

# Configure SQLAlchemy database URI and track modifications
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+mysqlconnector://USER:PASSWORD@localhost/gym_db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy and Marshmallow instances
db = SQLAlchemy(app)
ma = Marshmallow(app)

# Define Marshmallow schema for Member
class MemberSchema(ma.Schema):
    name = fields.String(required=True)
    age = fields.Integer(required=True)
    trainer_id = fields.Integer(required=True)

    class Meta:
        fields = ("name", "age", "trainer_id")

# Instantiate schemas for single member and multiple members
member_schema = MemberSchema()
members_schema = MemberSchema(many=True)

# Define Member model for database
class Member(db.Model):
    __tablename__ = "members"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey("trainers.id"), nullable=False)
    workouts = db.relationship("WorkoutSession", backref="member")

# Define WorkoutSession model for database
class WorkoutSession(db.Model):
    __tablename__ = "Workout_Sessions"
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.Date, nullable=False)
    duration_minutes = db.Column(db.Integer, nullable=False)
    calories_burned = db.Column(db.Integer, nullable=False)
    member_id = db.Column(db.Integer, db.ForeignKey("members.id"), nullable=False)
    trainer_id = db.Column(db.Integer, db.ForeignKey("trainers.id"), nullable=False)

# Define Trainer model for database
class Trainer(db.Model):
    __tablename__ = "trainers"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    members = db.relationship("Member", backref="trainer")
    workouts = db.relationship("WorkoutSession", backref="trainer")

# Route for home page
@app.route("/")
def home():
    return "Welcome to The Gym"

# Route to get all members
@app.route("/members", methods=["GET"])
def get_members():
    members = Member.query.all()
    return members_schema.jsonify(members)

# Route to add a new member
@app.route("/members", methods=["POST"])
def add_member():
    try:
        member_data = member_schema.load(request.json)

    except ValidationError as err:
        return jsonify(err.messages), 400

    new_member = Member(
        name=member_data["name"],
        age=member_data["age"],
        trainer_id=member_data["trainer_id"]
    )
    db.session.add(new_member)
    db.session.commit()
    return jsonify({"message": "New member added successfully"}), 201

# Route to update a member
@app.route("/members/<int:id>", methods=["PUT"])
def update_member(id):
    member = Member.query.get(id)
    if not member:
        abort(404, description=f"Member with id {id} not found")

    try:
        member_data = member_schema.load(request.json)

    except ValidationError as err:
        return jsonify(err.messages), 400

    member.name = member_data["name"]
    member.age = member_data["age"]
    member.trainer_id = member_data["trainer_id"]

    db.session.commit()
    return jsonify({"message": "Member details updated successfully"})

# Route to delete a member
@app.route("/members/<int:id>", methods=["DELETE"])
def delete_member(id):
    member = Member.query.get(id)
    if not member:
        abort(404, description=f"Member with id {id} not found")

    db.session.delete(member)
    db.session.commit()
    return jsonify({"message": f"Member with id {id} deleted successfully"}), 200

# Define Marshmallow schema for WorkoutSession
class WorkoutSessionSchema(ma.Schema):
    date = fields.Date(required=True)
    duration_minutes = fields.Integer(required=True)
    calories_burned = fields.Integer(required=True)
    member_id = fields.Integer(required=True)
    trainer_id = fields.Integer(required=True)

    class Meta:
        fields = ("id", "date", "duration_minutes", "calories_burned", "member_id", "trainer_id")

# Instantiate schemas for single workout session and multiple workout sessions
workout_session_schema = WorkoutSessionSchema()
workout_sessions_schema = WorkoutSessionSchema(many=True)

# Route to schedule a new workout session
@app.route("/workout-sessions", methods=["POST"])
def schedule_workout_session():
    try:
        session_data = workout_session_schema.load(request.json)

    except ValidationError as err:
        return jsonify(err.messages), 400

    new_session = WorkoutSession(
        date=session_data["date"],
        duration_minutes=session_data["duration_minutes"],
        calories_burned=session_data["calories_burned"],
        member_id=session_data["member_id"],
        trainer_id=session_data["trainer_id"]
    )
    db.session.add(new_session)
    db.session.commit()
    return jsonify({"message": "Workout session scheduled successfully"}), 201

# Route to get all workout sessions
@app.route("/workout-sessions", methods=["GET"])
def get_all_workout_sessions():
    sessions = WorkoutSession.query.all()
    return workout_sessions_schema.jsonify(sessions)

# Route to update a workout session
@app.route("/workout-sessions/<int:id>", methods=["PUT"])
def update_workout_session(id):
    session = WorkoutSession.query.get(id)
    if not session:
        abort(404, description=f"Workout session with id {id} not found")

    try:
        session_data = workout_session_schema.load(request.json)

    except ValidationError as err:
        return jsonify(err.messages), 400

    session.date = session_data["date"]
    session.duration_minutes = session_data["duration_minutes"]
    session.calories_burned = session_data["calories_burned"]
    session.member_id = session_data["member_id"]
    session.trainer_id = session_data["trainer_id"]

    db.session.commit()
    return jsonify({"message": "Workout session updated successfully"})

# Route to get all workout sessions for a specific member
@app.route("/members/<int:member_id>/workout-sessions", methods=["GET"])
def get_member_workout_sessions(member_id):
    sessions = WorkoutSession.query.filter_by(member_id=member_id).all()
    if not sessions:
        abort(404, description=f"No workout sessions found for member with id {member_id}")
    return workout_sessions_schema.jsonify(sessions)

# Run the application if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)
