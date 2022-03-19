import json
from collections import defaultdict

with open("iris.json", "r") as f:
    lines = f.readlines()

lst = []
for line in lines:
    if "[" in line or "]" in line:
        continue
    line = line.strip().strip(",")
    lst.append(json.loads(line))

print("list: ")
print(lst)

for flower in lst:
    max_min_dict = defaultdict(lambda: defaultdict(int))
    petalArea = flower["petalLength"] * flower["petalWidth"]
    sepalArea = flower["sepalLength"] * flower["sepalWidth"]
    species = flower["species"]
    if max_min_dict[species]["petalArea"] > petalArea:
        max_min_dict[species]["petalArea"] = petalArea
    if max_min_dict[species]["sepalArea"] < sepalArea:
        max_min_dict[species]["sepalArea"] = sepalArea
    if flower["species"] == "setosa":
        print(flower)

lst.sort(
    key=lambda dct: dct["petalLength"] * dct["petalWidth"]
    + dct["sepalLength"] * dct["sepalWidth"]
)
print("Sorted list: ")
print(lst)
