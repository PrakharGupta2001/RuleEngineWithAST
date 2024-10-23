# backend/test_database.py

from database import init_db, save_rule, get_all_rules, get_rule_by_id, update_rule, delete_rule

# Initialize the database
conn = init_db()

# Add a new rule
rule_id = save_rule(conn, "age > 30 AND salary > 50000")
print(f"Rule saved with ID: {rule_id}")

# Retrieve all rules
rules = get_all_rules(conn)
print("All Rules:", rules)

# Get a specific rule by ID
rule = get_rule_by_id(conn, rule_id)
print(f"Rule with ID {rule_id}:", rule)

# Update the rule
update_rule(conn, rule_id, "age > 35 AND salary > 60000")
print(f"Rule with ID {rule_id} updated.")

# Retrieve the updated rule
rule = get_rule_by_id(conn, rule_id)
print(f"Updated Rule with ID {rule_id}:", rule)

# Delete the rule
delete_rule(conn, rule_id)
print(f"Rule with ID {rule_id} deleted.")

# Verify deletion
rules = get_all_rules(conn)
print("All Rules after deletion:", rules)
