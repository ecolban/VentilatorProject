import time

# from adafruit_motorkit import MotorKit
from flask import Flask, request

# from adafruit_motorkit import MotorKit
# from adafruit_motor import stepper

from motor_kit_simulator import MotorKitSimulator, Stepper

app = Flask(__name__)


@app.route('/')
@app.route('/instructions')
def index():
    return """Follow instructions in the README"""


@app.route('/testdrive')
def testdrive():
    args = request.args
    direction = getattr(Stepper, args.get('direction', 'FORWARD'))
    style = getattr(Stepper, args.get('style', 'SINGLE'))
    sleep = float(args.get('sleep', '0.01'))
    steps = int(args.get('steps', 100))

    # kit = MotorKit()
    kit = MotorKitSimulator()

    for i in range(steps):
        kit.stepper1.onestep(direction=direction, style=style)
        time.sleep(sleep)
    kit.stepper1.release()
    return 'Done!', 200


if __name__ == "__main__":
    testdrive()
