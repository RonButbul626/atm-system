from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage (dictionary)
accounts = {
    '123456': {'balance': 1000},
    '654321': {'balance': 500},
}

@app.route('/accounts/<account_number>/balance', methods=['GET'])
def get_balance(account_number):
    if account_number in accounts:
        return jsonify({'balance': accounts[account_number]['balance']})
    return jsonify({'error': 'Account not found'}), 404

@app.route('/accounts/<account_number>/withdraw', methods=['POST'])
def withdraw(account_number):
    if account_number not in accounts:
        return jsonify({'error': 'Account not found'}), 404

    amount = request.json.get('amount')
    if amount <= 0 or amount > accounts[account_number]['balance']:
        return jsonify({'error': 'Invalid amount'}), 400

    accounts[account_number]['balance'] -= amount
    return jsonify({'message': 'Withdrawal successful', 'balance': accounts[account_number]['balance']})

@app.route('/accounts/<account_number>/deposit', methods=['POST'])
def deposit(account_number):
    if account_number not in accounts:
        return jsonify({'error': 'Account not found'}), 404

    amount = request.json.get('amount')
    if amount <= 0:
        return jsonify({'error': 'Invalid amount'}), 400

    accounts[account_number]['balance'] += amount
    return jsonify({'message': 'Deposit successful', 'balance': accounts[account_number]['balance']})

if __name__ == '__main__':
    app.run(debug=True)
