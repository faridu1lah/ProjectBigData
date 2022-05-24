# ProjectBigData

## Commands
---
```bash
# run stream lit
streamlit run main.py

# download packages
python3 -m pip install -r requirements.txt
```

## Git an GitHub
```bash
# create new branch
git checkout -b yourbranchname

# push/add to an upstream branch
git push --set-upstream origin melih

```

## Database 
---

We gebruiken de database server van de HVA (Oege) voor dit project. Je kan beter eigen server gebruiken om te testen zodat we elkaar niet in de weg zitten. Hiervoor kan je de volgende stappen volgen.

1. Pull de main branch via HTTPS (met jouw GitHub gegevens)
2. Download mysql-connector-python met: pip install mysql-connector-python (anders krijg je melding dat mysql.connector niet gevonden kan worden)
3. Vraag een MySQL account aan op: https://oege.ie.hva.nl/registratie/
4. Wijzig de db.py naar je de gegevens die je per e-mail hebt ontvangen (gebruikersnaam, databasenaam en wachtwoord)

5. Voeg het db.py bestand toe aan .gitignore zodat deze niet gepushed wordt met elke commit.

(Optioneel) Stap 6: Maak een databaseconnectie via jouw SQL-client (bijv Workbench). Je kan ook online PhpMyAdmin gebruiken via: https://oege.ie.hva.nl/phpmyadmin/. Hier log je in met de accountgegevens die je per e-mail hebt ontvangen

- Update db : https://big-data.faridullah.com/?token=bestgroup


## docker uitleg:
- https://www.rockyourcode.com/run-streamlit-with-docker-and-docker-compose/
