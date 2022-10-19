# server.py

from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server is on."


@app.route("/info", methods=["GET"])
def information():
    x = "This website will calculated blood cholesterol levels.\n"
    x += "It is written by Satya Pusuluri."
    return x


@app.route("/hdl_check", methods=["POST"])
def hdl_check_from_internet():
    """
        incoming_json = {"name": <name_str>,
                        "hdl_value": <hdl_value_int>}
    """
    from blood_calculator import check_HDL
    in_data = request.get_json()
    hdl_value = in_data["hdl_value"]
    print("The received value was {}.".format(hdl_value))
    answer = check_HDL(hdl_value)
    return jsonify(answer)


@app.route("/add_numbers", methods=["POST"])
def add_numbers_from_internet():
    """
        incoming_json = {"a": <int>,
                        "b": <int>}
    """
    in_data = request.get_json()
    return str(in_data['a'] + in_data['b'])


if __name__ == "__main__":
    app.run()
