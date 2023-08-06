import os
import javalang
from graphviz import Digraph

def parse_java_file(file_path):
    with open(file_path, "r") as file:
        java_code = file.read()
        tree = javalang.parse.parse(java_code)
        classes = {}
        connections = []

        for path, node in tree.filter(javalang.tree.ClassDeclaration):
            methods = []
            for method in node.methods:
                method_type = method.return_type.name.upper() if method.return_type else "VOID"
                methods.append((method.name, method_type))
            classes[node.name] = methods

            for field in node.fields:
                for declarator in field.declarators:
                    if isinstance(declarator, javalang.tree.ReferenceType) and declarator.name in classes:
                        connections.append((node.name, declarator.name))

        return classes, connections

def parse_java_files_in_folder(folder_path):
    all_classes = {}
    all_connections = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.java'):
                classes, connections = parse_java_file(os.path.join(root, file))
                all_classes.update(classes)
                all_connections.extend(connections)
    return all_classes, all_connections

def generate_uml(classes, connections):
    dot = Digraph(comment='The UML Diagram', node_attr={'shape': 'record'})

    for class_name, methods in classes.items():
        methods_str = ""
        for method_name, method_type in methods:
            methods_str += "- {}: {}\l".format(method_name, method_type)
        
        # Add class name as header
        header = "{{{}|{}}}".format(class_name, methods_str)
        dot.node(class_name, label=header, style='filled', fillcolor='lightgoldenrod1')

    for connection in connections:
        dot.edge(*connection)

    print(dot.source)
    dot.render('test-output/round-table.gv', view=True)

classes, connections = parse_java_files_in_folder("C:\\src")
generate_uml(classes, connections)
