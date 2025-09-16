from pathlib import Path
import json

numbers = [1, 2, 3, 4, 5]
path = Path("files/numbers.json")
data = json.dumps(numbers)
path.write_text(data)

contents = path.read_text()
loaded_nums = json.loads(contents)
print(data, contents, loaded_nums)
