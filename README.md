# sorty
pythonscript that uses modul hachoir to rename and sort mediafiles

Das Script extrahiert aus verschiedenen Mediadateien (im script editierbar .jpg, .mov etc....) das "creation_date" und ändert dementsprechend den Dateinamen.

BEISPIEL: IMG_7115.jpg -> 2020-07-21_110606.jpg

Anschließend wird die Datei in eine Ordnerstruktur einsortiert. In unserem Beispiel:
/2020/Juli/2020-07-21_110606.jpg

Die Ordnerstruktur wird vom Script erstellt, sollte keine Vorhanden sein.
Werden keine Metadaten gefunden, wird die Datei übersprungen.

Ich habe auch ein Dockerimage mit dem Script erstellt, da ich es auf einem Unraid server nutze.
https://hub.docker.com/repository/docker/philibooy/sorty

🚀 TO-DO:
- Wenn eine Datei keine Metadatei enthält soll sie in einen extra ordner verschoben werden
- besser lesbaren log.
- Zeiterfassung für die Bearbeitungsdauer
