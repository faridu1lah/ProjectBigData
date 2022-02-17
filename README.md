# ProjectBigData

### Database 

We gebruiken de database server van de HVA (Oege) voor dit project. Je kan beter eigen server gebruiken om te testen zodat we elkaar niet in de weg zitten. Hiervoor kan je de volgende stappen volgen.

Stap 1:
Pull de main branch via HTTPS (met jouw GitHub gegevens)

Stap 2:
Download mysql-connector-python met: pip install mysql-connector-python (anders krijg je melding dat mysql.connector niet gevonden kan worden)

Stap 3:
Vraag een MySQL account aan op: https://oege.ie.hva.nl/registratie/

Stap 4:
Wijzig de db.py naar je de gegevens die je per e-mail hebt ontvangen (gebruikersnaam, databasenaam en wachtwoord)

Stap 5:
Voeg het db.py bestand toe aan .gitignore zodat deze niet gepushed wordt met elke commit.

(Optioneel) Stap 6:
Maak een databaseconnectie via jouw SQL-client (bijv Workbench). Je kan ook online PhpMyAdmin gebruiken via: https://oege.ie.hva.nl/phpmyadmin/. Hier log je in met de accountgegevens die je per e-mail hebt ontvangen
