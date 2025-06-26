# Loginout
script zu protokollieren login und logout in eine computer

# anmeldung.py
Schreibt eine linie in CSV Datei mit der Anfang zeit.

# abmeldung.py
Schreibt in die angefangene linie von Anmeldung die Abmeldungszeit

# Nutzung:
Man sollte Anmeldung als LogonScript einrichten sowie Abmeldung.py als logout Script

# Probleme:
Der Script ist mit user rechte ausgefuhrt, d.h. der benutzer kann die Werte ändern.
Workaround: eine "Demon" uberwach die Ordner/Datei nach Änderungen und verschieb die CSV Datei ständig weit von Benutzer Hände.
