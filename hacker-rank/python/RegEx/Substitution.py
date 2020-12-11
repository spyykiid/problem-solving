import re
print re.sub(r'(?<= )(&&|\|\|)(?= )', lambda x: 'and' if x.group() == '&&' else 'or', "\n".join([raw_input() for _ in range(int(raw_input()))]))
