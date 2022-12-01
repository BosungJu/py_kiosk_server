from flask import Blueprint, request
from ..DBConnect import setup, insert, select, delete

bp = Blueprint('main', __name__, url_prefix='/')

# http://localhost:5000/
@bp.route('/')
def query():
    setup()

    if request.method == 'GET':
        type = request.args.get('queryType')
        tableName = request.args.get('tableName')
        datas = 'null'

        if type == 'insert':
            datas = request.args.get('datas')
            insert(tableName=tableName, datas=datas)
        elif type == 'select':
            params = request.args.get('params')
            data = request.args.get('data')
            datas = select(tableName=tableName, params=params, data=data)

            if len(datas) == 0:
                return [{'what': f'{tableName} is null'}]

            return datas
        elif type == 'delete':
            data = request.args.get('data')
            delete(tableName=tableName, data=data)

    return [{'what': f'execute insert or delete'}]
