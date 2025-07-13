"""
PDFJoiner

PDFJoiner ist aufgrund der verwendeten Bibliotheken unter der GNU Affero General Public License (AGPL) v3 lizenziert.

Verwendete Bibliotheken und deren Lizenzen:
-------------------------------------------------------------------------------
PySide6:
    PySide6 ist unter der GNU Lesser General Public License (LGPL) v3 lizenziert.
    Weitere Informationen: https://www.qt.io/licensing/lgpl-license
    Quellcode: https://code.qt.io/cgit/pyside/pyside-setup.git/

PyMuPDF:
    PyMuPDF (fitz) ist ein Python-Binding für MuPDF.
    MuPDF ist unter der GNU Affero General Public License (AGPL) v3 lizenziert.
    PyMuPDF selbst ist unter der GNU General Public License (GPL) v3 lizenziert.
    Weitere Informationen: https://pymupdf.readthedocs.io/en/latest/license.html
    Quellcode: https://github.com/pymupdf/PyMuPDF

-------------------------------------------------------------------------------
Weitere Hinweise zu Lizenzen finden Sie in der DATEI: LICENSE.txt
"""


from PySide6.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QHBoxLayout, QListWidget, QListWidgetItem,
    QPushButton, QFileDialog, QMessageBox, QLabel, QAbstractItemView, QSpacerItem, QSizePolicy
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QDragEnterEvent, QDropEvent
import fitz  # PyMuPDF
import sys
import os

class PDFListWidget(QListWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragDropMode(QAbstractItemView.InternalMove)
        self.setSelectionMode(QAbstractItemView.ExtendedSelection)

    def dragEnterEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls() or event.source() == self:
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)

    def dragMoveEvent(self, event: QDragEnterEvent):
        if event.mimeData().hasUrls() or event.source() == self:
            event.acceptProposedAction()
        else:
            super().dragMoveEvent(event)

    def dropEvent(self, event: QDropEvent):
        if event.source() == self:
            # Wenn der Drop von innerhalb des Widgets kommt, nutzen wir die Standard-Drop-Logik
            super().dropEvent(event)
        elif event.mimeData().hasUrls():
            # Wenn der Drop von externen Dateien kommt
            for url in event.mimeData().urls():
                file_path = url.toLocalFile()
                if file_path.lower().endswith(".pdf"):
                    self.add_pdf_item(file_path)
            event.acceptProposedAction()
        else:
            super().dropEvent(event)

    def add_pdf_item(self, file_path):
        item = QListWidgetItem(os.path.basename(file_path))
        item.setData(Qt.UserRole, file_path)
        self.addItem(item)

    def get_selected_files_in_order(self):
        # Gibt alle Elemente in der aktuell angezeigten Reihenfolge zurück.
        return [self.item(i).data(Qt.UserRole) for i in range(self.count())]

    def remove_selected_items(self):
        for item in self.selectedItems():
            self.takeItem(self.row(item))

class PDFToolApp(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PDFMerger")
        self.setup_ui()

    def setup_ui(self):
        main_layout = QVBoxLayout(self)

        # Hauptinhalt (Liste + Buttons)
        content_layout = QHBoxLayout()

        self.pdf_list = PDFListWidget()
        content_layout.addWidget(self.pdf_list, 3)

        button_panel = QVBoxLayout()
        button_panel.addWidget(QLabel("Dateiverwaltung"))

        add_button = QPushButton("Hinzufügen")
        add_button.clicked.connect(self.add_files)
        button_panel.addWidget(add_button)

        remove_button = QPushButton("Entfernen")
        remove_button.clicked.connect(self.pdf_list.remove_selected_items)
        button_panel.addWidget(remove_button)

        button_panel.addSpacing(20)
        button_panel.addWidget(QLabel("Aktionen"))

        unlock_button = QPushButton("Entsperren")
        unlock_button.clicked.connect(self.unlock_pdfs)
        button_panel.addWidget(unlock_button)

        merge_button = QPushButton("Zusammenführen")
        merge_button.clicked.connect(self.merge_pdfs)
        button_panel.addWidget(merge_button)

        button_panel.addStretch()
        content_layout.addLayout(button_panel, 1)

        main_layout.addLayout(content_layout)

        # Fußzeile unten rechts
        footer_layout = QHBoxLayout()
        footer_layout.addItem(QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum))
        footer_label = QLabel("Lizenz-Informationen:", self)
        link_url = "https://github.com/StrRD-len/PDFMerger/blob/main/LICENSE"
        link_text = "Lizenz-Informationen"
        link_color = "gray"
        footer_label.setText(f'<a href="{link_url}" style="color: {link_color};">{link_text}</a>')
        footer_label.setOpenExternalLinks(True)
        footer_label.setTextInteractionFlags(Qt.TextBrowserInteraction | Qt.LinksAccessibleByMouse)
        footer_label.setStyleSheet("color: gray; font-size: 10pt;")
        footer_layout.addWidget(footer_label)
        main_layout.addLayout(footer_layout)

    def add_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "PDF-Dateien auswählen", "", "PDF Files (*.pdf)")
        for file_path in files:
            self.pdf_list.add_pdf_item(file_path)

    def unlock_pdfs(self):
        selected_files = self.pdf_list.get_selected_files_in_order()
        if not selected_files:
            QMessageBox.warning(self, "Keine Auswahl", "Bitte zuerst PDF-Dateien auswählen.")
            return

        output_dir = QFileDialog.getExistingDirectory(self, "Zielordner für entsperrte PDFs")
        if not output_dir:
            return

        for file_path in selected_files:
            try:
                doc = fitz.open(file_path)
                output_path = os.path.join(output_dir, os.path.basename(file_path))
                doc.save(output_path)
                doc.close()
            except Exception as e:
                QMessageBox.critical(self, "Fehler", f"Fehler beim Entsperren von {file_path}:\n{str(e)}")
                return

        QMessageBox.information(self, "Fertig", "Alle ausgewählten PDFs wurden erfolgreich entsperrt.")

    def merge_pdfs(self):
        selected_files = self.pdf_list.get_selected_files_in_order()
        if not selected_files:
            QMessageBox.warning(self, "Keine Auswahl", "Bitte zuerst PDF-Dateien auswählen.")
            return

        output_path, _ = QFileDialog.getSaveFileName(self, "Ziel für zusammengeführte PDF", "", "PDF Files (*.pdf)")
        if not output_path:
            return

        try:
            merged_doc = fitz.open()
            toc = []
            page_count = 0
            for file_path in selected_files:
                doc = fitz.open(file_path)
                merged_doc.insert_pdf(doc)
                toc.append([1, os.path.basename(file_path), page_count + 1])
                page_count += doc.page_count
                doc.close()
            merged_doc.set_toc(toc)
            merged_doc.save(output_path)
            merged_doc.close()
            QMessageBox.information(self, "Fertig", "PDFs wurden erfolgreich zusammengeführt.")
        except Exception as e:
            QMessageBox.critical(self, "Fehler", f"Fehler beim Zusammenführen:\n{str(e)}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = PDFToolApp()
    window.show()
    sys.exit(app.exec())