import time

from flask import Flask

# from adafruit_motorkit import MotorKit
# from adafruit_motor import stepper

from motor_kit_simulator import MotorKitSimulator, stepper

app = Flask(__name__)


@app.route('/')
@app.route('/instructions')
def index():
    return """Follow instructions in the README"""


@app.route('/testdrive')
def testdrive(steps=100):
    # kit = MotorKit()
    kit = MotorKitSimulator()
    for i in range(steps):
        kit.stepper1.onestep(direction=stepper.FORWARD, style=stepper.SINGLE)
        time.sleep(0.01)
    kit.stepper1.release()
    return "Done!"


if __name__ == "__main__":
    testdrive(100)
