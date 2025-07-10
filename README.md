# PDFMerger - Entsperren & Zusammenführen

I. Über das Projekt

Dies ist eine einfache, plattformübergreifende Desktop-Anwendung, die mit PySide6 und PyMuPDF (fitz) entwickelt wurde, um zwei gängige Aufgaben im Umgang mit PDF-Dateien zu vereinfachen:

* **PDFs entsperren:** Entfernt Passwörter und Einschränkungen von PDF-Dateien, um die Bearbeitung oder den Druck zu ermöglichen.
* **PDFs zusammenführen:** Fügt mehrere PDF-Dateien in einer einzigen Ausgabedatei zusammen, wobei die Reihenfolge der ausgewählten Dateien beibehalten wird.

Die Anwendung bietet eine intuitive grafische Benutzeroberfläche (GUI) mit Drag-and-Drop-Unterstützung für PDF-Dateien.

II. Funktionen

* **PDF-Dateien hinzufügen:** Einfaches Hinzufügen von PDF-Dateien per Dateiauswahldialog oder Drag-and-Drop.
* **Dateien verwalten:** PDFs in der Liste neu anordnen (für das Zusammenführen) und unerwünschte Dateien entfernen.
* **PDFs entsperren:** Ausgewählte PDF-Dateien entsperren und in einem wählbaren Zielordner speichern.
* **PDFs zusammenführen:** Mehrere ausgewählte PDFs zu einer einzigen Datei zusammenführen, inklusive der Erstellung eines einfachen Inhaltsverzeichnisses (TOC) basierend auf den ursprünglichen Dateinamen.
* **Benutzerfreundliche GUI:** Klare und einfache Oberfläche für eine effiziente Nutzung.

III. Installation

Um die PDF Tool App lokal auszuführen, befolge diese Schritte:

1.  **Stelle sicher, dass Python installiert ist.** Du kannst es von [python.org](https://www.python.org/downloads/) herunterladen.
2.  **Klone dieses Repository:**
    ```bash
    git clone [https://github.com/StrRD-len/PDFMerger.git](https://github.com/StrRD-len/PDFMerger.git)
    ```
3.  **Navigiere in das Projektverzeichnis:**
    ```bash
    cd PDFMerger
    ```
4.  **Installiere die erforderlichen Abhängigkeiten:**
    ```bash
    pip install -r requirements.txt
    ```
    *Falls die `requirements.txt` noch nicht existiert, erstelle sie mit folgendem Inhalt und speichere sie im Projektverzeichnis:*
    ```
    PySide6
    PyMuPDF
    ```

IV. Nutzung

1.  **Starte die Anwendung:**
    ```bash
    python gui_app.py
    ```
2.  **Dateien hinzufügen:**
    * Klicke auf den "Hinzufügen"-Button, um PDF-Dateien über den Dateiauswahldialog hinzuzufügen.
    * Ziehe PDF-Dateien direkt per Drag-and-Drop in die Liste.
3.  **Dateien verwalten:**
    * Wähle Dateien aus und klicke auf "Entfernen", um sie aus der Liste zu löschen.
    * Ordne Dateien in der Liste per Drag-and-Drop neu an, um die Reihenfolge für das Zusammenführen festzulegen.
4.  **Aktionen ausführen:**
    * **Entsperren:** Wähle eine oder mehrere PDF-Dateien aus und klicke auf "Entsperren". Wähle einen Zielordner, in dem die entsperrten Kopien gespeichert werden sollen.
    * **Zusammenführen:** Wähle die PDF-Dateien in der gewünschten Reihenfolge aus und klicke auf "Zusammenführen". Wähle einen Speicherort und Dateinamen für die zusammengeführte PDF-Datei.

V. Entwicklung

Dieses Projekt verwendet:
* [**PySide6**](https://doc.qt.io/qtforpython/): Für die grafische Benutzeroberfläche.
* [**PyMuPDF (fitz)**](https://pymupdf.readthedocs.io/en/latest/): Eine schnelle PDF-Bibliothek für die PDF-Manipulation (entsperren, zusammenführen).

VI. Lizenz

Dieses Projekt steht unter der AGPLv3-Lizenz. Weitere Details finden Sie in der `LICENSE`-Datei.

VII. Mitwirkende

* StrRD-len
* Gemini 2.5

VIII. Kontakt

Bei Fragen oder Anregungen können Sie ein Issue in diesem Repository erstellen oder den Autor direkt kontaktieren.
