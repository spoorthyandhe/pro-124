from flask import Flask,jsonify, request

app = Flask(__name__)

List = [
    {
        'id':1,
        'Name':u'Vineetha',
        'Contact':u'6475636376',
        'done':False
    },
    {
        'id':2,
        'Name':u'spoorthy',
        'Contact':u'9845623154',
        'done':False
    }
]

@app.route("/add-data", methods=["POST"])
def add_task():
    if not request.json:
        return jsonify({
            "status":"error",
            "message": "Please provide the data!"
        },400)

    contact = {
        'id':tasks[-1]['id']+1,
        'Name':request.json['Name'],
        'Contact':request.json.get('Contact',""),
        'done':False
}
    List.append(contact)
    return jsonify({
        "status":"success",
        "message": "contact added succesfully!"
    })
    

@app.route("/get-data")
def get_task():
    return jsonify({
        "data" : List
    }) 

if (__name__ == "__main__"):
    app.run(debug=True)
