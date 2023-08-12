from flask import Flask, jsonify,request

app = Flask(__name__)
items = []
# Blueprint
@app.route("/addUser", methods = ["POST"])
def add_user():
    data = request.get_json()
    if data is None or 'user' not in data:
        return jsonify({'error':'Item name is required'})
    
    # need to replace this 
    new_item = {'id':len(items)+1, 'user': data['user']}
    items.append(new_item)
    return jsonify(items), 201

@app.route("/updateUser", methods = ["PUT"])
def update_user():
    data = request.get_json()
    
    len(items)
    return 'new task'

@app.route("/deleteUser", methods = ["DELETE"])
def delete_user():
    return 'delete an user'

@app.route("/getUsers", methods = ["GET"])
def get_users():
    results = jsonify(items)
    return results, 200

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)