from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def tip_calculator():
    if request.method == 'POST':
        bill_amount = float(request.form['bill_amount'])
        tip_percentage = float(request.form['tip_percentage'])

        tip_amount = bill_amount * (tip_percentage / 100)
        total_amount = bill_amount + tip_amount

        return render_template('result.html', bill_amount=bill_amount, tip_percentage=tip_percentage, tip_amount=tip_amount, total_amount=total_amount)
    else:
        return render_template('calculator.html')

if __name__ == '__main__':
    app.run(debug=True)
