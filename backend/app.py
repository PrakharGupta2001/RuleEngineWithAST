# backend/app.py

from flask import Flask, request, jsonify
from rule_engine import create_rule, combine_rules, evaluate_rule
from database import init_db, save_rule, get_all_rules, get_rule_by_id, update_rule, delete_rule

app = Flask(__name__)
conn = init_db()

@app.route('/create_rule', methods=['POST'])
def create_rule_endpoint():
    try:
        rule_string = request.json['rule']
        node = create_rule(rule_string)
        if node:
            # Save rule to the database
            rule_id = save_rule(conn, rule_string)
            return jsonify({'message': 'Rule created successfully', 'rule_id': rule_id}), 201
        return jsonify({'message': 'Failed to create rule'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/rules', methods=['GET'])
def list_rules():
    try:
        all_rules = get_all_rules(conn)
        return jsonify({'rules': all_rules}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/rules/<int:rule_id>', methods=['GET'])
def get_rule(rule_id):
    try:
        rule = get_rule_by_id(conn, rule_id)
        if rule:
            return jsonify({'rule': rule}), 200
        return jsonify({'message': 'Rule not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/rules/<int:rule_id>', methods=['PUT'])
def update_rule_endpoint(rule_id):
    try:
        rule_string = request.json['rule']
        node = create_rule(rule_string)
        if node:
            # Update rule in the database
            update_rule(conn, rule_id, rule_string)
            return jsonify({'message': 'Rule updated successfully'}), 200
        return jsonify({'message': 'Failed to update rule'}), 400
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/rules/<int:rule_id>', methods=['DELETE'])
def delete_rule_endpoint(rule_id):
    try:
        delete_rule(conn, rule_id)
        return jsonify({'message': 'Rule deleted successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@app.route('/evaluate_rule', methods=['POST'])
def evaluate_rule_endpoint():
    try:
        rule_id = request.json['rule_id']
        data = request.json['data']
        # Retrieve the rule from the database
        rule = get_rule_by_id(conn, rule_id)
        if not rule:
            return jsonify({'message': 'Rule not found'}), 404
        # Create the AST from the rule text and evaluate
        node = create_rule(rule[1])  # rule[1] is the rule text
        result = evaluate_rule(node, data)
        return jsonify({'result': result}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
