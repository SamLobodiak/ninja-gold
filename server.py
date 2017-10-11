from flask import Flask, render_template, request, redirect, session
from datetime import datetime
from collections import defaultdict
import random
app = Flask(__name__)
app.secret_key = "goldeneye"

@app.route('/')
def ROOT():
    print('In the ROOT ROUTE')
    if 'total_gold' not in session:
        session['total_gold'] = 0
    if 'x' not in session:
        session['x'] = list()
    print(session['x'])
    return render_template('index.html')

@app.route('/process_money', methods=['POST'])
def processMoney():
    print("Going through route '/process_money'")
    building = request.form['building']
    money = 0
    if building == 'farm':
        money = random.randint(10, 20)
        # print("You made", money, "gold in the", building)
        # session['x']="You made", money, "gold in the", building
        # print(session['x'])



    elif building == 'cave':
        money = random.randint(5, 10)
        # print("You made", money, "gold in the", building)
    elif building == 'house':
        money = random.randint(2, 5)
        # print("You made", money, "gold in the", building)
    elif building == 'casino':
        money = random.randint(-50, 50)

    # print("You made", money, "gold in the", building)
    session['x'].append("You made " + str(money) + " gold in the " + str(building)+".")
    print(session['x'])

    session['total_gold'] += money


    return redirect('/')

@app.route('/reset', methods=['POST'])
def reset():
    session['total_gold'] = 0
    print("Resetting Gold back to zero")
    return redirect('/')


app.run(debug=True)
