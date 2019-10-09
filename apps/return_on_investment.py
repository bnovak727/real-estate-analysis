from flask import Flask, render_template, request

from rea.expenses.loan import loan_payment

app = Flask(__name__)

@app.route("/", methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        amount = (float)(request.form['Loan Amount'])
        term = (float)(request.form['Loan Term'])
        rate = (float)(request.form['Loan Rate'])

        monthly_payment = return_on_investment(rate, term, loan_amount=amount)
        return "Monthly Payment: ${:.2f}".format(monthly_payment)


    return render_template('roi.html')
