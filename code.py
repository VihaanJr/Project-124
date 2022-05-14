from distutils.log import error
from flask import Flask , jsonify , request

app = Flask(__name__)

list = [
    {
        'id': 1,
        'Name': u'Paras',
        'Contact': u'8851424614', 
        'done': False
    },
    {
        'id': 2,
        'Name': u'Tejasv',
        'Contact': u'8860447672', 
        'done': False
    }
]

@app.route('/add-task' , methods = ['POST'])
def add_task():
    if not request.json:
        return jsonify({
            'status' : 'error',
            'message' : 'Please add the data'
        },400)

    else :
        lists = { 'id': list[-1]['id'] + 1, 
        'Name': request.json['Name'], 
        'Contact': request.json.get('Contact', ""), 
        'done': False }
        list.append(lists)
        return jsonify({
            'status' : 'Success',
            'message' : 'Task added successfully'
        })
    
@app.route('/get-task')
def get_task():
    return jsonify({
        'data':list
    })


if __name__== '__main__':
    app.run(debug=True)