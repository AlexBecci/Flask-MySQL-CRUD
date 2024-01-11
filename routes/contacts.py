from flask import Blueprint

contacts = Blueprint('contacts', __name__)

@contacts.route('/')
def home():
    return "contact list"

@contacts.route('/new')
def addContact():
    return "saving a contact"