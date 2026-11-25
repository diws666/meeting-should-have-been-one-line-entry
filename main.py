# Verified count: 109 characters, 111 UTF-8 bytes (the em-dash is 3 bytes).
LINE = "No, we are not doing that \u2014 this meeting was forty-five minutes of everyone agreeing with whoever spoke last."

import os

output_dir = os.environ.get('MAKEFUN_OUTPUT_DIR')
output_path = os.path.join(output_dir, 'entry.txt') if output_dir else '/output/entry.txt'

with open(output_path, 'w', encoding='utf-8') as f:
    f.write(LINE)

print(len(LINE))
