from flask import Flask, Response, request, abort, jsonify, render_template, session
from src.gateway import *
from src.models.shared import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']=DB_CONNECTION_STRING
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

## set up database session
session = flask_scoped_session(session_factory, app)
db.app = app
db.init_app(app)
db.create_all()

@app.route('/')
def index():
    return render_template('index.html', title='Home')

@app.route('/start_meeting')
def start_meeting():
    return render_template('base.html', title='Home')


@app.route('/__healthcheck__', methods=['GET', 'POST'])
def health_check():
    '''
    Health check responds for GET and POST
    GET: returns time time of server receiving request.
    POST: echos parameters and data passeed by request.
    '''
    ## Query parameter argumeents
    query_string_params = request.args

    ## data parameters from http request
    data_params = request.get_json()
    print(data_params)
    if request.method == 'GET':
        posted = { 'params': query_string_params, 'data': data_params}
        return render_template( 'healthcheck.html',
                                title='Healthcheck',
                                ttr={'time of response': time.time(), 'date': datetime.now()},
                                echo=posted)

    if request.method == 'POST':
        form_param = request.form['form_param']
        posted = { 'params': query_string_params, 'data': data_params , 'form_param': form_param}
        return render_template( 'healthcheck.html',
                                title='Healthcheck',
                                ttr={'time of response': time.time(), 'date': datetime.now()},
                                echo=posted)

@app.route('/db_tables')
def db_tables():
    print(engine.table_names())
    building = {}
    i = 0
    for tn in engine.table_names():
        building[i] = tn
    return building
