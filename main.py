import os

MAX_CHARS = 200

PART1 = "Investors, I already run the "
PART2 = "city's fastest delivery network: "
PART3 = "ten thousand wings, zero fuel, "
PART4 = "and I poop on your competitors' "
PART5 = "statues for free."
LINE = PART1 + PART2 + PART3 + PART4 + PART5

assert 1 <= len(LINE) <= MAX_CHARS, "entry must be 1-200 characters"
assert LINE.count(".") == 1 and LINE.endswith("."), "entry must be exactly one sentence"

os.makedirs("/output", exist_ok=True)
with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
    f.write(LINE)
with open("/output/entry.txt", "r", encoding="utf-8", newline="") as f:
    assert f.read() == LINE, "round-trip mismatch"
print(len(LINE))
