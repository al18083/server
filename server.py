from flask import Flask, request, render_template
app = Flask(__name__)
file_path = "./sensor_data.csv"
port_num = 18083

@app.route('/', methods=['GET'])
def get_html():
    return render_template('./index.html')

@app.route('/distance', methods=['POST'])
def update_distance():
    time = request.form["time"]
    distance = request.form["distance"]
    try:
        f = open(file_path, 'w')
        f.write(time + "," + distance)
        return "succeeded to write"
    except Exception as e:
        print(e)
        return "failed to write"
    finally:
        f.close()

@app.route('/distance', methods=['GET'])
def get_distance():
    try:
        f = open(file_path, 'r')
        for row in f:
            distance = row
    except Exception as e:
        print(e)
    finally:
        f.close()
        return distance

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=port_num)