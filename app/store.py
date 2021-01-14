import csv
from pathlib import Path

def add_user(username,hashed_password):
    parent_dir = Path().absolute().parent.parent
    with open(f"{parent_dir}/users.csv","w",encoding="UTF-8") as f:
        cs = csv.writer(f)
        cs.writerow((username,hashed_password))