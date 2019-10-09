from flask import Flask, render_template, request

from rea.expenses.loan import loan_payment

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    rate = 5.75
    loan_amount = 165000
    term = 30

    if request.method == 'POST':
        amount = (float)(request.form['Loan Amount'])
        term = (float)(request.form['Loan Term'])
        rate = (float)(request.form['Loan Rate'])

        monthly_payment = loan_payment(rate, term, loan_amount=amount)
        return "Monthly Payment: ${:.2f}".format(monthly_payment)


    return render_template('loan.html')
