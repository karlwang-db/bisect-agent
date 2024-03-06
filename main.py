import subprocess
import sys
from pprint import pprint
from typing import List


get_ordered_values_cmd = sys.argv[1]
verify_cmd = sys.argv[2]


def get_ordered_list() -> List[str]:
    print(f"Executing {get_ordered_values_cmd}")
    proc = subprocess.run(get_ordered_values_cmd, stdout=subprocess.PIPE, shell=True)
    res = proc.stdout.decode("utf-8")
    return list(filter(lambda s: len(s) > 0, res.split("\n")))


def verify(value: str) -> bool:
    for i in range(3):
        print(f"attempt: {i}")
        proc = subprocess.run(f"{verify_cmd} {value}", shell=True)
        if proc.returncode in [0, 1]:
            return proc.returncode == 0

    print(f"Unknown error when processing {value}")
    sys.exit()


values = get_ordered_list()

print(values)
left = 0
right = len(values)
res = []
while left < right:
    mid = (left + right) // 2
    value = values[mid]
    print(f"Verifying {value}")
    if verify(value):
        print(f"{value} succeeded")
        left = mid
        res.append((value, True))
    else:
        print(f"{value} failed")
        right = mid - 1
        res.append((value, False))
    print()

print("FINISHED")
pprint(res)
