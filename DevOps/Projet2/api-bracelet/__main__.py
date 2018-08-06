import time
import random
import argparse
from bottle import route, run, template

from _version import __version__


@route('/id', method='GET')
def index():
    return {'id': random.randint(1, 10)}


@route('/footstep/<id>', method='GET')
def footstep_number_by_id(id):
    return {'footstep': random.randint(400, 5000)}


@route('/heartbeat/<id>', method='GET')
def heartbeat_number_by_id(id):
    return {'heartbeat': random.randint(20, 200), 'last_modified': int(time.time())}


def main():
     # Define argument parser
    parser = argparse.ArgumentParser()
    # Add each available arguments
    parser.add_argument('-v', '--version', action='version', version='%(prog)s ' + __version__)
    parser.add_argument('-H', '--hostname', help='Hostname used to expose the API', type=str, default="localhost")
    parser.add_argument('-p', '--port', help='Port used to expose the API', type=int, default=80, choices=range(1, 65535))

    args = parser.parse_args()

    hostname = args.hostname
    port = args.port

    run(host=hostname, port=port)

# =====================================
# MAIN : Entrypoint of the program
# =====================================
if __name__ == "__main__":
    main()
