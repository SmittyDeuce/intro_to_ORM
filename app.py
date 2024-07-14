
''' I leave out with app.app_context():
    db.create_all() because my flask does not work with it i get error  
    and I KNOW its not my password or the flask configuration
    
    
    
    Traceback (most recent call last):
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/bin/flask", line 8, in <module>
    sys.exit(main())
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/flask/cli.py", line 1105, in main
    cli.main()
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/click/core.py", line 1078, in main
    rv = self.invoke(ctx)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/click/core.py", line 1688, in invoke
    return _process_result(sub_ctx.command.invoke(sub_ctx))
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/click/core.py", line 1434, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/click/decorators.py", line 92, in new_func
    return ctx.invoke(f, obj, *args, **kwargs)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/click/core.py", line 783, in invoke
    return __callback(*args, **kwargs)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/flask/cli.py", line 953, in run_command
    raise e from None
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/flask/cli.py", line 937, in run_command
    app: WSGIApplication = info.load_app()
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/flask/cli.py", line 339, in load_app
    app = locate_app(import_name, None, raise_if_not_found=False)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/flask/cli.py", line 245, in locate_app
    __import__(module_name)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/app.py", line 253, in <module>
    db.create_all()
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/flask_sqlalchemy/extension.py", line 900, in create_all
    self._call_for_binds(bind_key, "create_all")
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/flask_sqlalchemy/extension.py", line 881, in _call_for_binds
    getattr(metadata, op_name)(bind=engine)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/sql/schema.py", line 5871, in create_all
    bind._run_ddl_visitor(
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/engine/base.py", line 3250, in _run_ddl_visitor
    with self.begin() as conn:
  File "/usr/lib/python3.10/contextlib.py", line 135, in __enter__
    return next(self.gen)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/engine/base.py", line 3240, in begin
    with self.connect() as conn:
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/engine/base.py", line 3276, in connect
    return self._connection_cls(self)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/engine/base.py", line 148, in __init__
    Connection._handle_dbapi_exception_noconnection(
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/engine/base.py", line 2440, in _handle_dbapi_exception_noconnection
    raise sqlalchemy_exception.with_traceback(exc_info[2]) from e
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/engine/base.py", line 146, in __init__
    self._dbapi_connection = engine.raw_connection()
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/engine/base.py", line 3300, in raw_connection
    return self.pool.connect()
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/pool/base.py", line 449, in connect
    return _ConnectionFairy._checkout(self)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/pool/base.py", line 1263, in _checkout
    fairy = _ConnectionRecord.checkout(pool)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/pool/base.py", line 712, in checkout
    rec = pool._do_get()
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/pool/impl.py", line 179, in _do_get
    with util.safe_reraise():
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/util/langhelpers.py", line 146, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/pool/impl.py", line 177, in _do_get
    return self._create_connection()
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/pool/base.py", line 390, in _create_connection
    return _ConnectionRecord(self)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/pool/base.py", line 674, in __init__
    self.__connect()
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/pool/base.py", line 900, in __connect
    with util.safe_reraise():
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/util/langhelpers.py", line 146, in __exit__
    raise exc_value.with_traceback(exc_tb)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/pool/base.py", line 896, in __connect
    self.dbapi_connection = connection = pool._invoke_creator(self)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/engine/create.py", line 643, in connect
    return dialect.connect(*cargs, **cparams)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/sqlalchemy/engine/default.py", line 620, in connect
    return self.loaded_dbapi.connect(*cargs, **cparams)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/mysql/connector/pooling.py", line 322, in connect
    return CMySQLConnection(*args, **kwargs)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/mysql/connector/connection_cext.py", line 151, in __init__
    self.connect(**kwargs)
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/mysql/connector/abstracts.py", line 1399, in connect
    self._open_connection()
  File "/home/smittydeuce/temple/assignments/api_rest/intro_to_ORM/myenv/lib/python3.10/site-packages/mysql/connector/connection_cext.py", line 339, in _open_connection
    raise get_mysql_exception(
sqlalchemy.exc.ProgrammingError: (mysql.connector.errors.ProgrammingError) 1045 (28000): Access denied for user 'USER'@'localhost' (using password: YES)
(Background on this error at: https://sqlalche.me/e/20/f405)
 '''






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

# Define Marshmallow schema for Trainer
class TrainerSchema(ma.Schema):
    name = fields.String(required=True)

    class Meta:
        fields = ("id", "name")

# Instantiate schemas for single trainer and multiple trainers
trainer_schema = TrainerSchema()
trainers_schema = TrainerSchema(many=True)

# Route to add a new trainer
@app.route("/trainers", methods=["POST"])
def add_trainer():
    try:
        trainer_data = trainer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    new_trainer = Trainer(name=trainer_data["name"])
    db.session.add(new_trainer)
    db.session.commit()
    return jsonify({"message": "New trainer added successfully"}), 201

# Route to get all trainers
@app.route("/trainers", methods=["GET"])
def get_trainers():
    trainers = Trainer.query.all()
    return trainers_schema.jsonify(trainers)

# Route to update a trainer
@app.route("/trainers/<int:id>", methods=["PUT"])
def update_trainer(id):
    trainer = Trainer.query.get(id)
    if not trainer:
        abort(404, description=f"Trainer with id {id} not found")

    try:
        trainer_data = trainer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400

    trainer.name = trainer_data["name"]
    db.session.commit()
    return jsonify({"message": "Trainer details updated successfully"})

# Route to delete a trainer
@app.route("/trainers/<int:id>", methods=["DELETE"])
def delete_trainer(id):
    trainer = Trainer.query.get(id)
    if not trainer:
        abort(404, description=f"Trainer with id {id} not found")

    db.session.delete(trainer)
    db.session.commit()
    return jsonify({"message": f"Trainer with id {id} deleted successfully"}), 200

# Create the database tables
with app.app_context():
    db.create_all()

# Run the application if this file is executed directly
if __name__ == "__main__":
    app.run(debug=True)
