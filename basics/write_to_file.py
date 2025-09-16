from pathlib import Path

path = Path('pi_write.txt')
contents = "I love programming.\n"
contents += "I love creating new games.\n"
contents += "I also love working with data.\n"
path.write_text(contents)
