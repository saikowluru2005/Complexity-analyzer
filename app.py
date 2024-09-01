from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/analyze', methods=['POST'])
def analyze_code():
    data = request.json
    code = data['code']
    time_complexity, space_complexity = analyze_complexity(code)
    return jsonify({'time': time_complexity, 'space': space_complexity})

def analyze_complexity(code):
    time_complexity = "O(n)"
    space_complexity = "O(1)"
    return time_complexity, space_complexity

if __name__ == '__main__':
    app.run(debug=True)
