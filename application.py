from flask import Flask, url_for, request, redirect, abort, jsonify
from clientDao import clientDao

app = Flask(__name__, static_url_path='', static_folder='staticpages')


@app.route('/')
def index():
    return "hello"
#get all


@app.route('/clients')
def getAll():
    return jsonify(clientDao.getAll())
# find By id

# Give all the clients
# curl http://127.0.0.1:5000/clients 


@app.route('/clients/<int:ClientID>')
def findById(ClientID):
    return jsonify(clientDao.findById(ClientID))

#Find Clients by ID
#curl http://127.0.0.1:5000/clients/12

# create
# curl -X POST -d "{\"ClientID\":3,\"Names\":\"James\", \"Surname\":\"Smithtest\", \"Price\":120}" -H "content-type:application/json" http://127.0.0.1:5000/clients


@app.route('/clients', methods=['POST'])
def create():
   
    if not request.json:
        abort(400)

    client = {
        "ClientID": request.json["ClientID"],
        "Names": request.json["Names"],
        "Surname": request.json["Surname"],
        "Price": request.json["Price"]
    }
    return jsonify(clientDao.create(client))

    return "served by Create "

#update
# curl -X PUT -d "{\"Surname\":\"Smithtest2\", \"Price\":125}" -H "content-type:application/json" http://127.0.0.1:5000/clients/6


@app.route('/clients/<int:ClientID>', methods=['PUT'])
def update(ClientID):
    foundClient=clientDao.findById(ClientID)
    
    if foundClient == {}:
        return jsonify({}), 404
    currentClient = foundClient
    if 'Names' in request.json:
        currentClient['Names'] = request.json['Names']
    if 'Surname' in request.json:
        currentClient['Surname'] = request.json['Surname']
    if 'Price' in request.json:
        currentClient['Price'] = request.json['Price']
    clientDao.update(currentClient)

    return jsonify(currentClient)

#delete
# curl -X DELETE http://127.0.0.1:5000/clients/6


@app.route('/clients/<int:ClientID>', methods=['DELETE'])
def delete(ClientID):
    clientDao.delete(ClientID)

    return jsonify({"done": True})


if __name__ == "__main__":
    app.run(debug=True)