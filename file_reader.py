from pathlib import Path

path = Path("pi.txt")
path2 = Path("files/one_million_lines.txt")
contents = path.read_text()
contents = contents.rstrip()
contents2 = path2.read_text()
contents2 = contents2.rstrip()
lines = contents2.splitlines()

pi_string = ''
for line in lines:
  pi_string += line.lstrip()
    
print(f"{pi_string[:52]}...")
print(len(pi_string))
# print(contents, lines, pi_string)
