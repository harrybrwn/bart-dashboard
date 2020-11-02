import sqlite3

from flask import (
    Flask,
    request,
    send_from_directory,
)
import pyexcel

app = Flask(__name__, static_url_path='/public')
db = sqlite3.connect('db/dashboard.db')

DEBUG = True

VALID_CONTENT_TYPES = {
    "application/vnd.ms-excel",
    "application/vnd.ms-excel.sheet.macroEnabled.12",
    "application/vnd.ms-excel.template.macroEnabled.12",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    "application/vnd.openxmlformats-officedocument.spreadsheetml.template",
    "text/csv",
}


@app.route('/', defaults={'path': None})
@app.route('/<path>', methods=['GET'])
def home(path):
    '''
    return the home page and any other public files
    '''
    if not path:
        path = 'index.html'
    return send_from_directory('../public', path)


@app.route('/api/test', methods=['GET', 'POST'])
def api_test():
    return {'db': repr(db), 'app': repr(app)}


@app.route('/api/upload', methods=['POST'])
def handle_uploads():
    '''handle_uploads handles the spreadsheet file uploads'''
    f = request.files['file']
    if f.content_type not in VALID_CONTENT_TYPES:
        return {"error": "Unknown content type"}, 400
    if not f.filename:
        return {"error": "No filename"}, 400
    ext = f.filename.split('.')[-1]
    book = pyexcel.get_book(file_type=ext, file_content=f.read())
    # TODO do stuff with sheet
    return {'success': f'{f.filename} uploaded successfully'}, 200 # status "ok"


@app.route('/api/asset/<assetnum>', methods=['GET'])
def get_asset(assetnum):
    result = db.execute(
        '''
        SELECT *
        FROM assets_table
        WHERE
            assetnum = ?''',
        (assetnum, ),
    )
    raise NotImplemented


@app.route('/api/asset', methods=['POST'])
def create_asset():
    raise NotImplemented


@app.route('/api/asset/<assetnum>/readings', methods=['GET'])
def asset_readings(assetnum):
    result = db.execute('''
        SELECT reading FROM meter_reading
        WHERE assetnum = ?''', (assetnum, ))
    data = []
    for row in result:
        data.append(row[0])
    return {'readings': data}

#Workorder API

#MPU Post Workorder
@app.route('/api/workorder/<id>', methods=['POST'])
def post_workorder(id):
    raise NotImplemented

#MPU get Workorder
@app.route('/api/workorder/<id>', methods=['GET'])
def get_workorder(id):
    raise NotImplemented

#MPU Delete Workorder
@app.route('/api/workorder/<id>', methods=['DELETE'])
def del_workorder(id):
    raise NotImplemented

#MPU Put Workorder
@app.route('/api/workorder/<id>', methods=['PUT'])
def put_workorder(id):
    raise NotImplemented

# Start of code things for MPU

#MPU
#MPU list
@app.route('/api/mpu', methods=['GET'])
def ListMPU():
    if request.method == 'GET':
        #get the list of MPUS
        result = db.execute(
            # TODO list the MPU data
            'select * from mpu'
        )
        d = dict()
        for mpu in result:
            d[mpu[2]] = mpu
        return d


#MPU IDs
#MPU post IDs
@app.route('/api/mpu', methods=['POST'])
def create_new_mpu():
        # insert the new asset into the db
        result = db.execute(
            '''
            INSERT INTO mpu
            ... whatever the rest of this query is...''',
            (id, ),
        )


#MPU get IDs
@app.route('/api/mpu/<id>', methods=['GET'])
def get_mpu(id):
        #get MPUS with ID
        result = db.execute(
           '''
            SELECT *
            FROM mpu
            WHERE
                id = ?''',
            (id, ),
        )
        return result

#Delete MPU by IDs
@app.route('/api/mpu/<id>', methods=['DELETE'])
def del_mpu(id):
        #Delete ID
        result = db.execute(
            #TODO remove ID
        )

#MPU PUT IDs
@app.route('/api/mpu/<id>', methods=['PUT'])
def put_mpu(id):
        #Put MPUs
            result = db.execute(
            #TODO PUT ID
        )

#MPU Milestones
#MPU Post Milestones
@app.route('/api/mpu/<id>/milestone', methods=['POST'])
def post_mpu_milestone(id): pass

#MPU get Milestones
@app.route('/api/mpu/<id>/milestone', methods=['GET'])
def get_mpu_milestone(id): pass

#MPU Delete Milestones
@app.route('/api/mpu/<id>/milestone', methods=['DELETE'])
def del_mpu_milestone(id): pass

#MPU Put Milestones
@app.route('/api/mpu/<id>/milestone', methods=['PUT'])
def put_mpu_milestone(id): pass

#MPU Funds
#MPU Post Funds
@app.route('/api/mpu/<id>/fund', methods=['POST'])
def post_mpu_fund(id): pass

#MPU get Funds
@app.route('/api/mpu/<id>/fund', methods=['GET'])
def get_mpu_fund(id): pass

#MPU Delete Funds
@app.route('/api/mpu/<id>/fund', methods=['DELETE'])
def del_mpu_fund(id): pass

#MPU Put Funds
@app.route('/api/mpu/<id>/fund', methods=['PUT'])
def put_mpu_fund(id): pass

#MPU Criteria
#MPU Post Criteria
@app.route('/api/mpu/<id>/criteria', methods=['POST'])
def post_mpu_criteria(id): pass

#MPU get Criteria
@app.route('/api/mpu/<id>/criteria', methods=['GET'])
def get_mpu_criteria(id): pass

#MPU Delete Criteria
@app.route('/api/mpu/<id>/criteria', methods=['DELETE'])
def del_mpu_criteria(id): pass

#MPU Put Criteria
@app.route('/api/mpu/<id>/criteria', methods=['PUT'])
def put_mpu_criteria(id): pass
