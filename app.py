# Import libraries
from flask import Flask, render_template, request, url_for

# Instantiate Flask functionality
app = Flask("financial transaction recording system")

# Sample data
transactions = [
    {'id': 1, 'date': '2023-06-01', 'amount': 100},
    {'id': 2, 'date': '2023-06-02', 'amount': -200},
    {'id': 3, 'date': '2023-06-03', 'amount': 300}
]

# Read operation
@app.route("/")
def get_transactions():
    return render_template("transactions.html", transactions = transactions)

# Create operation
@app.route("/add-transactions" methods = ['GET', 'POST'])
def add_trasaction():
    if request.method == 'POST':
        transation = {
            'id': len(transactions)+1
            'date': request.form['date']
            'amount': float(request.form['amount'])
            }

        transactions.append(transaction)
    
    return redirect(url_for(get_transactions))

# Update operation
@app.route('/edit/<int:transaction_id>')
def edit_transaction(transaction_id):
    if request.method == 'POST':
        date = request.form['date']
        amount = request.form['amount']

        for transaction in transactions:
            if transaction['id'] == transaction_id:
                transaction['date'] = date
                transaction['amount'] = amount
                break
            
        return redirect(url_for("get_transactions"))


    if request.method == 'GET':
        for transaction in transactions:
            if transaction['id'] == transaction_id:
                return render_template('edit.html', transaction = transaction)

    return {'msg': 'Transaction toh hai hi nhi....ky hi edit karun??'}, 404

# Delete operation
@app.route('/delete/<int:transaction_id>')
def delete_transaction(transaction_id):
    for transaction in transactions:
        if transaction['id'] == transaction_id:
            transactions.remove(transaction)
            break
                
    return redirect(url_for('get_transactions'))
# Run the Flask app
    