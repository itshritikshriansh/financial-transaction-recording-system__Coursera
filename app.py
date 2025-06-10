# Import libraries
from flask import Flask, render_template, request, url_for, redirect

# Instantiate Flask functionality
app = Flask("__main__")

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
@app.route("/add-transactions", methods = ['GET', 'POST'])
def add_transaction():
    if request.method == 'POST':
        transaction = {
            'id': len(transactions)+1,
            'date': request.form['date'],
            'amount': float(request.form['amount'])
            }

        transactions.append(transaction)
        return redirect(url_for('get_transactions'))

    return render_template('form.html')

# Update operation
@app.route('/edit/<int:transaction_id>', methods = ['GET', 'POST'])
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

@app.route("/search", methods = ['GET', 'POST'])
def search_transactions():
    if request.method == 'POST':
        filtered_transaction = []
        min = float(request.form['min_amount'])
        max = float(request.form['max_amount'])

        for transaction in transactions:
            if transaction['amount'] == min:
                filtered_transaction.append(transaction)
            
            if transaction['amount'] == max:
                filtered_transaction.append(transaction)

        return render_template('transactions.html', transactions = filtered_transaction)

    return render_template('search.html')

# Run the Flask app
if __name__ == "__main__":
    app.run(debug=True)