from flask import Flask, request, jsonify
from data import *
app = Flask(__name__)

def _get_rule_by_id(id):
    return next(item for item in rules if item["id"] == id)

@app.get("/rules")
def get_rules():
    return jsonify(rules)

@app.post("/rules")
def create_rule():
    if request.is_json:
        rule = request.get_json()
        rule = rule | {"id" : len(rules) + 1}
        rules.append(rule)
        return rules, 201
    return {"error": "Request must be JSON"}, 415

@app.get("/rules/<int:id>")
def get_rule_by_id(id):
    rule = _get_rule_by_id(id)
    return rule, 201

@app.post("/rules/<int:id>")
def edit_rule(id):
    new_expression = request.args.get("expression")
    rule = _get_rule_by_id(id)
    rule["expression"] = new_expression
    return rule, 201

@app.route("/rules/<int:id>", methods=["DELETE"])
def delete_rule(id):
    rule = _get_rule_by_id(id)
    rules.pop(rule)
    return rule, 201

@app.get("/rules/<int:id>/actions")
def get_actions_of_rule_id(id):
    rule = _get_rule_by_id(id)
    rule["actions"]
    return rule["actions"], 201

'''
@app.post("/rules/<int:id>/actions")
def run_action_of_rule_id(id):
    #action = request.args.get("action_id")
    #run action

@app.get("/rules/<int:product_type_id>")
def get_all_rules_from_product_type(product_type_id):
    product = request.args.get("product_type_id")
#todo return list of rules based on product type
#ideal return rules of a generic element type

'''