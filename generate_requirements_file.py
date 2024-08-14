import os

def generate_requirements_file(directory, output_file='requirements.txt'):
    requirements = set()
    
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith('.py'):
                with open(os.path.join(root, file), 'r') as f:
                    for line in f:
                        if line.startswith('import ') or line.startswith('from '):
                            parts = line.split()
                            if line.startswith('import'):
                                requirements.add(parts[1])
                            elif line.startswith('from'):
                                requirements.add(parts[1])
    
    with open(output_file, 'w') as f:
        for requirement in sorted(requirements):
            f.write(f"{requirement}\n")