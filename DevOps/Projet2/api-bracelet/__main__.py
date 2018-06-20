import random
import time
from bottle import route, run, template


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
    run(host='localhost', port=80)

# =====================================
# MAIN : Entrypoint of the program
# =====================================
if __name__ == "__main__":
    main()
