from flask import Flask, request, jsonify

app = Flask(__name__)

# In-memory data storage (dictionary)
accounts = {
    '873214': {'balance': 1250},
    '452198': {'balance': 340},
    '367591': {'balance': 2300},
    '129874': {'balance': 180},
    '984321': {'balance': 950},
    '236547': {'balance': 1560},
    '573829': {'balance': 780},
    '648213': {'balance': 2150},
    '319875': {'balance': 430},
    '785412': {'balance': 3200},
    '453291': {'balance': 890},
    '612984': {'balance': 1100}
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
    app.run(host = '0.0.0.0', port=5000)
