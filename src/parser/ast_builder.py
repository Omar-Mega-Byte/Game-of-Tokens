class ASTBuilder:
    def __init__(self):
        pass

    def build_ast(self, matched_rules):
        """Simulates building an Abstract Syntax Tree (AST)."""
        if matched_rules:
            return {"type": "Program", "body": matched_rules}
        return None

if __name__ == '__main__':
    builder = ASTBuilder()
    sample_rules = ["Rule: A -> B", "Rule: C -> D"]
    ast = builder.build_ast(sample_rules)
    if ast:
        import json
        print("Simulated AST:")
        print(json.dumps(ast, indent=2))

