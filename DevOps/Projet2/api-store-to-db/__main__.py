import argparse
import requests
import threading
from pymongo import MongoClient

from _version import __version__


def get_bracelet_id():
    response = requests.get('http://localhost/id')
    return str(response.json()['id'])


def get_bracelet_footstep(collection):
    threading.Timer(3600, get_bracelet_footstep, [collection]).start()

    bracelet_id = get_bracelet_id()
    response = requests.get('http://localhost/footstep/' + bracelet_id)
    print(response)

    collection.find_one_and_update({'id': bracelet_id}, {"$set": response.json()}, upsert=True)


def get_bracelet_heartbeat(collection):
    threading.Timer(10, get_bracelet_heartbeat, [collection]).start()

    bracelet_id = get_bracelet_id()
    response = requests.get('http://localhost/heartbeat/' + bracelet_id)
    print(response)

    collection.find_one_and_update({'id': bracelet_id}, {"$push": response.json()}, upsert=True)


def main():
    # Define argument parser
    parser = argparse.ArgumentParser()
    # Add each available arguments
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('-H', '--hostname', help='Hostname used to connect to the Mongo database', type=str, default="localhost")
    parser.add_argument('-P', '--port', help='Port used to connect to the Mongo database', type=int, default=27017, choices=range(1, 65535))
    parser.add_argument('-D', '--database', help='Name used to connect to the Mongo database', type=str)
    parser.add_argument('-u', '--user', help='User used to connect to the Mongo database', type=str)
    parser.add_argument('-p', '--password', help='Password used to connect to the Mongo database', type=str)

    args = parser.parse_args()

    hostname = args.hostname
    port = args.port
    database = args.database
    user = args.user
    password = args.password

    # Init connexion to mongodb mongodb+srv://26academy:<PASSWORD>@cluster0-bihus.mongodb.net/test?retryWrites=true
    client = MongoClient('mongodb://{}:{}@{}:{}'.format(user, password, hostname, port))
    client = MongoClient('mongodb+srv://26academy:26academy@cluster0-bihus.mongodb.net/test?retryWrites=true')
    
    database = client[database]
    collection = database['bracelet']

    get_bracelet_footstep(collection)
    get_bracelet_heartbeat(collection)

# =====================================
# MAIN : Entrypoint of the program
# =====================================
if __name__ == "__main__":
    main()
