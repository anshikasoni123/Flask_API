from flask import Flask,jsonify,request

app = Flask(__name__)

data = [
    {
        'Contact':9987644456,
        'Name':'Raju',
        'Done':False,
        'Id':1
    },
    {
        'Contact':9876543222,
        'Name':'Rahul',
        'Done':False,
        'Id':2
    }
]

@app.route('/')

def hello_world():
    return 'Hello World!!'

@app.route('/add-data',methods=['POST'])

def add_data():
    if not request.json:
        return jsonify({
            'status':"error",
            'message':'Need to provide data'
        },400)
    task = {
        'id':data[-1]['id']+1,
        'name':request.json['Name'],
        'Contact':request.json.get['Contact'],
        'Done':False
    }
    data.append(task)
    return jsonify({
        'status':'Success',
        'message':'Data provided'
    })

@app.route('/get-data')

def get_data():
    return jsonify({
        'data':data
    })

if(__name__ == '__main__'):
    app.run(debug=True)