import re

pattern = r'[a-zA-Z]+'
origin_str = 'hello world'

re.search(pattern, origin_str)
re.match(pattern, origin_str)
re.fullmatch(pattern, origin_str)
re.findall(pattern, origin_str)
re.finditer(pattern, origin_str)

# After compile
cp = re.compile(pattern)
cp.search(pattern, origin_str)
cp.match(pattern, origin_str)
cp.fullmatch(pattern, origin_str)
cp.findall(pattern, origin_str)
cp.finditer(pattern, origin_str)