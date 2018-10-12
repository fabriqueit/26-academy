import argparse
import requests
import threading
from pymongo import MongoClient

from _version import __version__


def get_bracelet_id(api_bracelet):
    response = requests.get('http://{}/id'.format(api_bracelet))
    return str(response.json()['id'])


def get_bracelet_footstep(api_bracelet, collection):
    threading.Timer(3600, get_bracelet_footstep, [api_bracelet, collection]).start()

    bracelet_id = get_bracelet_id(api_bracelet)
    response = requests.get('http://{}/footstep/'.format(api_bracelet) + bracelet_id)
    print(response)

    collection.find_one_and_update({'id': bracelet_id}, {"$set": response.json()}, upsert=True)


def get_bracelet_heartbeat(api_bracelet, collection):
    threading.Timer(10, get_bracelet_heartbeat, [api_bracelet, collection]).start()

    bracelet_id = get_bracelet_id(api_bracelet)
    response = requests.get('http://{}/heartbeat/'.format(api_bracelet) + bracelet_id)
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
    parser.add_argument('-A', '--api_hostname', help='Hostname used to connect to API-bracelet', type=str, default="localhost")

    args = parser.parse_args()

    hostname = args.hostname
    port = args.port
    database = args.database
    user = args.user
    password = args.password
    api_bracelet = args.api_hostname

    # Init connexion to mongodb
    # for exemple : mongodb+srv://26academy:<PASSWORD>@cluster0-bihus.mongodb.net/test?retryWrites=true
    client = MongoClient('mongodb://{}:{}@{}:{}'.format(user, password, hostname, port))
    
    database = client[database]
    collection = database['bracelet']

    get_bracelet_footstep(api_bracelet, collection)
    get_bracelet_heartbeat(api_bracelet, collection)

# =====================================
# MAIN : Entrypoint of the program
# =====================================
if __name__ == "__main__":
    main()
