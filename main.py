from reading import Reading, Combination, Result
from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def reading():
    true_statement = 1
    while true_statement == 1:
        reading = Reading()
        first_number = reading[0]
        second_number = reading[1]
        first_letter = reading[2]
        second_letter = reading[3]

        combination = Combination(str(first_number), str(second_number), first_letter, second_letter)
        result = Result(str(first_number), str(second_number), first_letter, second_letter)
        return jsonify({"combination": combination,
                        "result": result})

if __name__ == "__main__":
    app.debug= True
    app.run(host = '0.0.0.0', port = 5000)
