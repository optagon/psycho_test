from reading import Reading, Combination, Result
from flask import Flask, render_template, request, session
from reading import Reading, Combination
import os


app = Flask(__name__)
SESSION_TYPE = "redis"
PERMANENT_SESSION_LIFETIME = 1800

app.config.update(SECRET_KEY=os.urandom(24))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/shortterm-memory-reading")
def shortterm_memory_reading():
    list_of_combinations = []
    list_of_results = []
    for i in range(10):
        reading = Reading()
        first_number = reading[0]
        second_number = reading[1]
        first_letter = reading[2]
        second_letter = reading[3]
        result = Result(first_number, second_number, first_letter, second_letter)
        list_of_results.append(result)

        session['key'] = list_of_results
        combination = Combination(first_number, second_number, first_letter, second_letter)
        list_of_combinations.append(combination)


    combinations = {
        'combination': list_of_combinations,
    }
    print(combinations)
    print(type(combinations))

    return render_template('shortterm-memory-reading.html', combinations=combinations)

@app.route("/shortterm-memory-listening")
def shortterm_memory_listening():
    list_of_combinations = []
    list_of_results = []
    for i in range(10):
        reading = Reading()
        first_number = reading[0]
        second_number = reading[1]
        first_letter = reading[2]
        second_letter = reading[3]
        result = Result(first_number, second_number, first_letter, second_letter)
        list_of_results.append(result)

        session['key'] = list_of_results
        combination = Combination(first_number, second_number, first_letter, second_letter)
        list_of_combinations.append(combination)


    combinations = {
        'combination': list_of_combinations,
    }
    print(combinations)
    print(type(combinations))

    return render_template('/shortterm-memory-listening.html', combinations=combinations)

@app.route('/results', methods=["POST"])
def form():
    if request.method == 'POST':
        user_inputs = request.form.getlist('input')
        sublist_of_results = session.get('key', None)
        list_of_results = []
        for a in sublist_of_results:
            for item in a:
                list_of_results.append(item)

        missing = list(set(list_of_results)-set(user_inputs))
        print("chybne odpovedi: ", missing)
        final_result = (1 - (len(missing)) / 20) * 100
        final_result = round(final_result, 1)

        if final_result >= 80:
            success_msg = "uspěl(a)"
        elif final_result < 80:
            success_msg = "neuspěl(a)"
        else:
            success_msg = "error"

    return render_template("results.html", user_inputs=user_inputs, combinations=list_of_results, final_result=final_result, success_msg=success_msg)


if __name__ == "__main__":
    app.run(debug=False, host = '0.0.0.0', port=5000)
