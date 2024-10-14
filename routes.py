# defines all the routes (or views) that were originally in the my_app.py file.

from flask import Blueprint, request, jsonify
from .data import users, students

# Define the blueprint
main = Blueprint('main', __name__)

# Get all users
@main.route('/myusers', methods=['GET'])
def getusers():
    return jsonify({"users": users, "message": "This is a list of all the users"})


# Get user by age
@main.route('/user/<int:age>', methods=['GET'])
def get_user(age):
    found_user = [user for user in users if user["age"] == age]
    return jsonify({"users with the same age": found_user})


# Add new user
@main.route('/newuser', methods=['POST'])
def newuser():
    mynewuser = {
        "firstName": request.json["firstName"],
        "secondName": request.json["secondName"],
        "age": request.json["age"],
        "occupation": request.json["occupation"]
    }
    users.append(mynewuser)
    return jsonify({"list of all the users": users})


# Update user by first name
@main.route('/update/<name>', methods=['PUT'])
def update_user(name):
    for user in users:
        if user["firstName"] == name:
            user["firstName"] = request.json.get("firstName", user["firstName"])
            user["secondName"] = request.json.get("secondName", user["secondName"])
            user["occupation"] = request.json.get("occupation", user["occupation"])
            user["age"] = request.json.get("age", user["age"])

    return jsonify({"the updated user": user}), 200


# Delete user by age
@main.route('/user_ages/<int:user_age>', methods=['DELETE'])
def delete_user(user_age):
    user_to_delete = [user for user in users if user['age'] == user_age]
    
    if user_to_delete:
        users.remove(user_to_delete[0])
        return jsonify({'message': f'user: {user_to_delete} has been deleted successfully!'})
    return jsonify({'message': 'No user found with that age'}), 404


# Student registration
@main.route('/registration', methods=['POST'])
def student_registration():
    student = {
        "userName": request.json["userName"],
        "phoneNumber": request.json["phoneNumber"],
        "password": request.json["password"]
    }
    students.append(student)
    return jsonify({"registered user": student, "message": "The user has been registered successfully"})


# Get all students
@main.route('/all_students', methods=['GET'])
def get_students():
    return jsonify(students)


# Student login
@main.route('/login', methods=['POST'])
def login_user():
    username = request.json.get('userName')
    password = request.json.get('password')

    for student in students:
        if student["userName"] == username and student["password"] == password:
            return jsonify(f"Successful login, {username}")
    return jsonify("Try again. Wrong details used")
