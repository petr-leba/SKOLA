import os

# Nastavení názvu souboru s příjmeními
filename = "prijmeni.txt"

# Nastavení názvu databáze a uživatele
dbname = "prijmeni"
username = "prijmeni"
password = "prijmeni123."

# Načtení seznamu příjmení ze souboru
with open(filename) as f:
    prijmeni = f.read().splitlines()

# Vytvoření SQL skriptu pro každé příjmení
for prijmeni_item in prijmeni:
    sql_script = f"CREATE DATABASE {prijmeni_item} CHARACTER SET utf8 COLLATE utf8_czech_ci;\n" \
                f"CREATE USER '{prijmeni_item}'@'localhost' IDENTIFIED BY '{password}';\n" \
                f"GRANT ALL PRIVILEGES ON {prijmeni_item}.* TO '{prijmeni_item}'@'localhost' WITH GRANT OPTION;\n"

    # Uložení SQL skriptu do souboru
    with open(f"{prijmeni_item}.sql", "w") as f:
        f.write(sql_script)

    # Spuštění SQL skriptu pro vytvoření databáze a uživatele
    os.system(f"mysql -u {username} -p{password} < {prijmeni_item}.sql")