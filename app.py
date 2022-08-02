from flask import Flask, jsonify, request, render_template
from math import sqrt

app = Flask(__name__)

##Returns current version of this application.
@app.route('/version')
def return_version():
    ##Create key-value
    data = {
            'Version' : 13.37,
        }
    ##return it as JSON.
    return jsonify(data)

##Returns True or False to indicate if provided number is prime.
@app.route('/is-prime', methods =['GET', 'POST'])
def is_prime():
    if request.method == 'POST':
        value = int(request.form.get('integer-value'))
        solution = {
            'Value' : value,
            'Is-Prime' : find_if_prime(value)
        }
        return jsonify(solution)
    ##TODO add styling
    return render_template('form.html')

def find_if_prime(x):
    if(x > 3):
        ##We reduce the value to its square root to reduce the amount of iterations.
        for i in range(2, int(sqrt(x)) + 1):
            ##If no iterations find a remainder, we can break out of the loop because the number isn't prime.
            if (x % i == 0):
                prime = False
                break
            ##If we do find a remainder, we need to adjust the state before we break the loop.
            else:
                prime = True
        if (prime):
            return 'True'
        else:
            return 'False'
    ##We add exceptions for 1 - 3, since we know the results, but they're too small for our algorithm.
    elif (x == 2):
        return 'True'
    elif (x == 3):
        return 'True'
    else:
        return 'False'

##TODO Find a better way to host
if __name__ == '__main__':
    app.run(host='0.0.0.0')