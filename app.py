from flask import *
import os
from z3 import *

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY')

@app.route('/', methods=['GET'])
def index():
    return 'Please refer to this <a href="https://github.com/ganeshsankaran/system-solver-api">GitHub repository</a>'

@app.route('/api/v1/solve', methods=['GET'])
def solve():
    s = Solver()
    x = Real('x')
    y = Real('y')

    a_1_1 = request.args['a_1_1']
    a_1_2 = request.args['a_1_2']
    a_2_1 = request.args['a_2_1']
    a_2_2 = request.args['a_2_2']
    b_1 = request.args['b_1']
    b_2 = request.args['b_2']

    s.add(a_1_1 * x + a_1_2 * y == b_1)
    s.add(a_2_1 * x + a_2_2 * y == b_2)

    if s.check() == sat:
        m = s.model()
        s.add(Or(x != m[x], y != m[y]))

        if s.check() == sat:
            return jsonify({'x': None, 'y': None, 'notes': 'Dependent system'})
        else:
            return jsonify({'x': str(m[x]), 'y': str(m[y]), 'notes': 'Independent system'})

    else:
        return jsonify({'x': None, 'y': None, 'notes': 'Inconsistent system'})

if __name__ == '__main__':
    app.run(debug=True)
