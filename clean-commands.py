#!/usr/bin/python
# Clean up Clang's compile_commands.json

import json

with open("compile_commands.json") as f:
    data = json.loads(f.read())

data = [x for x in data if not 'conftest' in x['command']]

with open("compile_commands.json", "w") as f:
    f.write(json.dumps(data, indent=4))

