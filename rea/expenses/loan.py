# Calculates mortgage loan information

def loan_payment(rate_pct, term_years,
                 loan_amount=None,
                 purchase_price=None, downpayment_pct=None):
    """
    """
    # Determine loan amount
    '''
    if loan_amount and (purchase_price or downpayment):
        print("ERROR")
    elif loan_amount:
        loan_amount = loan_amount
    elif purchase_price and downpayment:
        loan_amount = purchase_price * (1-downpayment_pct/100)
    '''

    P = loan_amount
    r = rate_pct / 100 / 12
    n = term_years * 12
    monthly_payment = P * (r * (1+r)**n) / ((1+r)**n - 1)

    return monthly_payment
