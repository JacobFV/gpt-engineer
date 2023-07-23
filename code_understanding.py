```python
import ast

class CodeParser:
    def __init__(self):
        self.CodeElements = []

    def parse_code(self, code):
        tree = ast.parse(code)
        self.CodeElements = [node.id for node in ast.walk(tree) if isinstance(node, ast.Name)]
        return self.CodeElements

class ArchitectureSpec:
    def __init__(self, code_elements):
        self.code_elements = code_elements

    def write_spec(self):
        spec = {}
        for element in self.code_elements:
            spec[element] = {"type": type(element).__name__, "value": element}
        return spec

def main():
    code = """
    def hello_world():
        print("Hello, World!")
    """

    parser = CodeParser()
    elements = parser.parse_code(code)

    spec = ArchitectureSpec(elements)
    architecture_spec = spec.write_spec()

    print(architecture_spec)

if __name__ == "__main__":
    main()
```