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
def edit_transaction()

# Delete operation

# Run the Flask app
    