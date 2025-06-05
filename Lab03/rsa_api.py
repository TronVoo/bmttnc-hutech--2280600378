import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.rsa import Ui_MainWindow
import requests


class MyApp(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # Kết nối các nút với hàm xử lý
        self.ui.btn_generate.clicked.connect(self.call_api_gen_keys)
        self.ui.btn_encrypt.clicked.connect(self.call_api_encrypt)
        self.ui.btn_decrypt.clicked.connect(self.call_api_decrypt)
        self.ui.btn_sign.clicked.connect(self.call_api_sign)
        self.ui.btn_verify.clicked.connect(self.call_api_verify)

    def show_error_message(self, message, response=None):
        """Hiển thị thông báo lỗi cho người dùng."""
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setWindowTitle("Error")
        if response and response.status_code != 200:
            try:
                error_data = response.json()
                message += f"\nServer error: {error_data.get('error', 'No details provided')}"
            except ValueError:
                message += f"\nServer response: {response.text[:100]}"
        msg.setText(message)
        msg.exec_()

    def call_api_gen_keys(self):
        url = "http://127.0.0.1:5000/api/rsa/generate_keys"
        try:
            response = requests.get(url)
            if response.status_code == 200:
                try:
                    data = response.json()
                    if "message" in data:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText(data["message"])
                        msg.setWindowTitle("Success")
                        msg.exec_()
                    else:
                        self.show_error_message("API response missing 'message' key.", response)
                except ValueError:
                    self.show_error_message("API returned invalid JSON.", response)
            else:
                self.show_error_message(f"API Error: Status code {response.status_code}", response)
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Error: {str(e)}")

    def call_api_encrypt(self):
        message = self.ui.plaintxtedit.toPlainText().strip()
        if not message:
            self.show_error_message("Please enter a message to encrypt.")
            return
        if len(message.encode()) > 245:  # Giới hạn cho RSA 2048-bit
            self.show_error_message("Message is too long for RSA encryption (max ~245 bytes).")
            return

        url = "http://127.0.0.1:5000/api/rsa/encrypt"
        payload = {
            "message": message,
            "key_type": "public"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                try:
                    data = response.json()
                    if "encrypted_message" in data:
                        self.ui.ciphertxtedit.setPlainText(data["encrypted_message"])
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Encrypted Successfully")
                        msg.setWindowTitle("Success")
                        msg.exec_()
                    else:
                        self.show_error_message("API response missing 'encrypted_message' key.", response)
                except ValueError:
                    self.show_error_message("API returned invalid JSON.", response)
            else:
                self.show_error_message(f"API Error: Status code {response.status_code}", response)
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Error: {str(e)}")

    def call_api_decrypt(self):
        ciphertext = self.ui.ciphertxtedit.toPlainText().strip()
        if not ciphertext:
            self.show_error_message("Please enter a ciphertext to decrypt.")
            return

        url = "http://127.0.0.1:5000/api/rsa/decrypt"
        payload = {
            "ciphertext": ciphertext,
            "key_type": "private"
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                try:
                    data = response.json()
                    if "decrypted_message" in data:
                        self.ui.plaintxtedit.setPlainText(data["decrypted_message"])
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Decrypted Successfully")
                        msg.setWindowTitle("Success")
                        msg.exec_()
                    else:
                        self.show_error_message("API response missing 'decrypted_message' key.", response)
                except ValueError:
                    self.show_error_message("API returned invalid JSON.", response)
            else:
                self.show_error_message(f"API Error: Status code {response.status_code}", response)
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Error: {str(e)}")

    def call_api_sign(self):
        message = self.ui.infortxtedit.toPlainText().strip()
        if not message:
            self.show_error_message("Please enter a message to sign.")
            return

        url = "http://127.0.0.1:5000/api/rsa/sign"
        payload = {
            "message": message
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                try:
                    data = response.json()
                    if "signature" in data:
                        self.ui.sigtxtedit.setPlainText(data["signature"])
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setText("Signed Successfully")
                        msg.setWindowTitle("Success")
                        msg.exec_()
                    else:
                        self.show_error_message("API response missing 'signature' key.", response)
                except ValueError:
                    self.show_error_message("API returned invalid JSON.", response)
            else:
                self.show_error_message(f"API Error: Status code {response.status_code}", response)
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Error: {str(e)}")

    def call_api_verify(self):
        message = self.ui.infortxtedit.toPlainText().strip()
        signature = self.ui.sigtxtedit.toPlainText().strip()
        if not message or not signature:
            self.show_error_message("Please enter both message and signature to verify.")
            return

        url = "http://127.0.0.1:5000/api/rsa/verify"
        payload = {
            "message": message,
            "signature": signature
        }
        try:
            response = requests.post(url, json=payload)
            if response.status_code == 200:
                try:
                    data = response.json()
                    if "is_verified" in data:
                        msg = QMessageBox()
                        msg.setIcon(QMessageBox.Information)
                        msg.setWindowTitle("Verification Result")
                        if data["is_verified"]:
                            msg.setText("Verified Successfully")
                        else:
                            msg.setText("Verification Failed")
                        msg.exec_()
                    else:
                        self.show_error_message("API response missing 'is_verified' key.", response)
                except ValueError:
                    self.show_error_message("API returned invalid JSON.", response)
            else:
                self.show_error_message(f"API Error: Status code {response.status_code}", response)
        except requests.exceptions.RequestException as e:
            self.show_error_message(f"Error: {str(e)}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MyApp()
    window.show()
    sys.exit(app.exec_())