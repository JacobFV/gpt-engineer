```python
class ArchitectureSpec:
    def __init__(self):
        self.spec = {}

    def add_element(self, element_name, element_info):
        self.spec[element_name] = element_info

    def write_spec(self):
        with open('architecture_spec.txt', 'w') as file:
            file.write(str(self.spec))


class CodeParser:
    def __init__(self, code):
        self.code = code
        self.elements = {}

    def parse_code(self):
        # Parsing logic goes here
        pass

    def get_elements(self):
        return self.elements


def main():
    code = ""  # The code to be parsed
    parser = CodeParser(code)
    parser.parse_code()

    spec = ArchitectureSpec()
    elements = parser.get_elements()

    for element_name, element_info in elements.items():
        spec.add_element(element_name, element_info)

    spec.write_spec()


if __name__ == "__main__":
    main()
```