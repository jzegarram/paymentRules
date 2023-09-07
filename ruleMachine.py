def evaluate_rule(rule, user_answers, operators):
    field = rule['field']
    rule_type = rule['ruleType']
    value = rule['value']

    if field not in user_answers:
        return False

    user_value = user_answers[field]

    if rule_type == 'BOOLEAN':
        return user_value == value
    elif rule_type == 'RANGE':
        operator = rule['operator']
        op_func = operators.get(operator, lambda x, y: False)
        return op_func(user_value, value)
    elif rule_type == 'SELECT':
        return user_value == value

    return False

def evaluate_group(group, user_answers, operators):
    conjunction = group['properties']['conjunction']
    children = group['children']

    if conjunction == 'AND':
        return all(evaluate_rule(child, user_answers, operators) if child['type'] == 'RULE' else evaluate_group(child, user_answers, operators) for child in children)
    elif conjunction == 'OR':
        return any(evaluate_rule(child, user_answers, operators) if child['type'] == 'RULE' else evaluate_group(child, user_answers, operators) for child in children)

    return False

def ruleMachine(payment_gateways, user_answers, operators, actionTypes):
    available_actions = []

    for gateway in sorted(payment_gateways, key=lambda x: x['priority']):
        condition = gateway['condition']
        if evaluate_group(condition, user_answers, operators):
            action_type = gateway['action']['type']
            action_value = gateway['action']['value']
            available_actions.append(f"{action_value}")

    return available_actions