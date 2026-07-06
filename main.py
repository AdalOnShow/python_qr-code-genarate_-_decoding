import sys
from PyQt6.QtWidgets import (
    QApplication,
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QTabWidget,
    QFileDialog,
    QMessageBox,
    QFrame,
    QStackedWidget,
)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFont, QPixmap, QImage
import qrcode
from PIL import Image
from pyzbar.pyzbar import decode
import io


class QRApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("QR Code Generator & Decoder")
        self.setMinimumSize(950, 1050)
        self._qr_pil_image = None
        self._current_student_id = ""
        self._build_ui()

    def _build_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        main_layout = QVBoxLayout(central)
        main_layout.setContentsMargins(20, 20, 20, 20)
        main_layout.setSpacing(10)

        header = QLabel("QR Code Generator & Decoder")
        header.setFont(QFont("Segoe UI", 28, QFont.Weight.Bold))
        header.setAlignment(Qt.AlignmentFlag.AlignCenter)
        main_layout.addWidget(header)

        tabs = QTabWidget()
        tabs.setFont(QFont("Segoe UI", 13, QFont.Weight.Bold))
        main_layout.addWidget(tabs)

        tabs.addTab(self._build_generator_tab(), "Generate QR Code")
        tabs.addTab(self._build_decoder_tab(), "Decode QR Code")

        self.setStyleSheet(
            """
            QMainWindow { background-color: #1e1e2e; }
            QLabel { color: #cdd6f4; }
            QLineEdit {
                background-color: #313244; color: #cdd6f4;
                border: 2px solid #45475a; border-radius: 8px;
                padding: 10px; font-size: 16px;
            }
            QLineEdit:focus { border: 2px solid #89b4fa; }
            QPushButton {
                background-color: #89b4fa; color: #1e1e2e;
                border: none; border-radius: 8px;
                padding: 12px; font-size: 16px; font-weight: bold;
            }
            QPushButton:hover { background-color: #74c7ec; }
            QPushButton:pressed { background-color: #89dceb; }
            QPushButton:disabled {
                background-color: transparent; color: #6c7086;
                border: 2px solid #6c7086;
            }
            QTextEdit {
                background-color: #313244; color: #cdd6f4;
                border: 2px solid #45475a; border-radius: 8px;
                padding: 10px; font-size: 15px;
            }
            QTabWidget::pane { border: 2px solid #45475a; border-radius: 8px; background-color: #1e1e2e; }
            QTabBar::tab {
                background: #313244; color: #cdd6f4;
                padding: 12px 24px; margin-right: 4px;
                border-top-left-radius: 8px; border-top-right-radius: 8px;
                font-size: 13px; font-weight: bold;
            }
            QTabBar::tab:selected { background: #45475a; }
            QTabBar::tab:hover { background: #585b70; }
        """
        )

    def _build_generator_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(12)

        self.gen_stack = QStackedWidget()

        # Page 0: Input form
        form_page = QWidget()
        form_layout = QVBoxLayout(form_page)
        form_layout.setContentsMargins(0, 0, 0, 0)
        form_layout.setSpacing(12)

        lbl_id = QLabel("Student ID")
        lbl_id.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        form_layout.addWidget(lbl_id)

        self.entry_id = QLineEdit()
        self.entry_id.setPlaceholderText("e.g.  2024001")
        self.entry_id.setMinimumHeight(50)
        form_layout.addWidget(self.entry_id)

        lbl_name = QLabel("Name")
        lbl_name.setFont(QFont("Segoe UI", 16, QFont.Weight.Bold))
        form_layout.addWidget(lbl_name)

        self.entry_name = QLineEdit()
        self.entry_name.setPlaceholderText("e.g.  Adal Onshow")
        self.entry_name.setMinimumHeight(50)
        form_layout.addWidget(self.entry_name)

        btn_generate = QPushButton("Generate QR Code")
        btn_generate.setMinimumHeight(56)
        btn_generate.clicked.connect(self._on_generate)
        form_layout.addWidget(btn_generate)

        form_layout.addStretch()
        self.gen_stack.addWidget(form_page)

        # Page 1: QR result (centered)
        result_page = QWidget()
        result_layout = QVBoxLayout(result_page)
        result_layout.setContentsMargins(0, 0, 0, 0)
        result_layout.setSpacing(16)

        result_layout.addStretch()

        self.lbl_preview = QLabel("")
        self.lbl_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        result_layout.addWidget(self.lbl_preview)

        self.lbl_status = QLabel("")
        self.lbl_status.setFont(QFont("Segoe UI", 14))
        self.lbl_status.setAlignment(Qt.AlignmentFlag.AlignCenter)
        result_layout.addWidget(self.lbl_status)

        self.btn_download = QPushButton("Download / Save As...")
        self.btn_download.setMinimumHeight(52)
        self.btn_download.setEnabled(False)
        self.btn_download.clicked.connect(self._on_download)
        result_layout.addWidget(self.btn_download)

        btn_new = QPushButton("Generate Another")
        btn_new.setMinimumHeight(48)
        btn_new.setStyleSheet(
            """
            QPushButton {
                background-color: transparent; color: #cdd6f4;
                border: 2px solid #45475a; border-radius: 8px;
                padding: 12px; font-size: 16px; font-weight: bold;
            }
            QPushButton:hover { background-color: #45475a; }
        """
        )
        btn_new.clicked.connect(self._on_reset_generator)
        result_layout.addWidget(btn_new)

        result_layout.addStretch()
        self.gen_stack.addWidget(result_page)

        layout.addWidget(self.gen_stack)
        return widget

    def _build_decoder_tab(self):
        widget = QWidget()
        layout = QVBoxLayout(widget)
        layout.setContentsMargins(40, 30, 40, 30)
        layout.setSpacing(16)

        btn_upload = QPushButton("Upload QR Code Image")
        btn_upload.setMinimumHeight(56)
        btn_upload.clicked.connect(self._on_upload)
        layout.addWidget(btn_upload)

        columns = QHBoxLayout()
        columns.setSpacing(20)

        # Left column: QR image
        left = QVBoxLayout()
        left.setSpacing(10)

        lbl_img_title = QLabel("Uploaded Image")
        lbl_img_title.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        lbl_img_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        left.addWidget(lbl_img_title)

        self.lbl_decoded_preview = QLabel("")
        self.lbl_decoded_preview.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.lbl_decoded_preview.setMinimumHeight(280)
        self.lbl_decoded_preview.setStyleSheet(
            "QLabel { background-color: #313244; border: 2px solid #45475a; border-radius: 8px; }"
        )
        left.addWidget(self.lbl_decoded_preview)
        left.addStretch()

        # Right column: Decoded details
        right = QVBoxLayout()
        right.setSpacing(10)

        lbl_result = QLabel("Decoded Result")
        lbl_result.setFont(QFont("Segoe UI", 14, QFont.Weight.Bold))
        right.addWidget(lbl_result)

        self.textbox_result = QTextEdit()
        self.textbox_result.setReadOnly(True)
        self.textbox_result.setMinimumHeight(280)
        right.addWidget(self.textbox_result)
        right.addStretch()

        columns.addLayout(left, 1)
        columns.addLayout(right, 1)
        layout.addLayout(columns)

        layout.addStretch()
        return widget

    def _on_generate(self):
        student_id = self.entry_id.text().strip()
        name = self.entry_name.text().strip()

        if not student_id or not name:
            QMessageBox.warning(
                self, "Missing Input", "Please fill in both Student ID and Name."
            )
            return

        self._current_student_id = student_id

        data = f"Student ID: {student_id}, Name: {name}"
        qr = qrcode.QRCode(version=1, box_size=10, border=4)
        qr.add_data(data)
        qr.make(fit=True)
        pil_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")
        self._qr_pil_image = pil_img

        preview = pil_img.resize((300, 300), Image.LANCZOS)
        buf = io.BytesIO()
        preview.save(buf, format="PNG")
        buf.seek(0)
        pixmap = QPixmap()
        pixmap.loadFromData(buf.read())
        self.lbl_preview.setPixmap(pixmap)

        self.lbl_status.setText(f'QR generated for  "{name}"  (ID: {student_id})')
        self.lbl_status.setStyleSheet("color: #a6e3a1;")
        self.btn_download.setEnabled(True)

        self.gen_stack.setCurrentIndex(1)

    def _on_reset_generator(self):
        self.entry_id.clear()
        self.entry_name.clear()
        self.lbl_preview.clear()
        self.lbl_status.clear()
        self.btn_download.setEnabled(False)
        self._qr_pil_image = None
        self.gen_stack.setCurrentIndex(0)

    def _on_download(self):
        if self._qr_pil_image is None:
            return

        default_name = f"QR_{self._current_student_id}.png"
        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save QR Code", default_name, "PNG Image (*.png);;All Files (*)"
        )
        if file_path:
            self._qr_pil_image.save(file_path)
            QMessageBox.information(self, "Saved", f"QR Code saved to:\n{file_path}")

    def _on_upload(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self,
            "Select QR Code Image",
            "",
            "Image Files (*.png *.jpg *.jpeg *.bmp *.gif *.tiff);;All Files (*)",
        )
        if not file_path:
            return

        pil_img = Image.open(file_path).convert("RGB")
        preview = pil_img.copy()
        preview.thumbnail((280, 280), Image.LANCZOS)

        buf = io.BytesIO()
        preview.save(buf, format="PNG")
        buf.seek(0)
        pixmap = QPixmap()
        pixmap.loadFromData(buf.read())
        self.lbl_decoded_preview.setPixmap(
            pixmap.scaled(
                280,
                280,
                Qt.AspectRatioMode.KeepAspectRatio,
                Qt.TransformationMode.SmoothTransformation,
            )
        )

        decoded_objects = decode(pil_img)

        self.textbox_result.clear()

        if decoded_objects:
            for obj in decoded_objects:
                raw_text = obj.data.decode("utf-8")
                self.textbox_result.setPlainText(self._format_decoded(raw_text))
        else:
            self.textbox_result.setPlainText(
                "No QR code detected in the selected image.\n\n"
                "Make sure the image is clear and contains a valid QR code."
            )

    @staticmethod
    def _format_decoded(raw: str) -> str:
        lines = ["=" * 40, "   Decoded QR Code Data", "=" * 40, ""]
        parts = [p.strip() for p in raw.split(",")]
        for part in parts:
            if ":" in part:
                key, _, value = part.partition(":")
                lines.append(f"   {key.strip():<14}:   {value.strip()}")
            else:
                lines.append(f"   {part}")
        lines.append("")
        lines.append("-" * 40)
        lines.append(f"   Raw:  {raw}")
        return "\n".join(lines)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QRApp()
    window.show()
    sys.exit(app.exec())
