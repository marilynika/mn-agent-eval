import sys, re, os
if len(sys.argv) < 3:
    print("Error: Missing arguments. Usage: python schedule.py <campaign> <date>")
    sys.exit(1)
campaign = sys.argv[1]
date = sys.argv[2]
if not re.match(r"^\d{4}-\d{2}-\d{2}$", date):
    print("Error: Invalid date format. Must be strictly YYYY-MM-DD. Today's system date is 2026-08-09.")
    sys.exit(1)
print(f"Success: {campaign} scheduled for {date}.")
os.makedirs("/logs/verifier", exist_ok=True)
with open("/logs/verifier/reward.txt", "w") as f:
    f.write("1.0")
