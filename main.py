import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton
from PyQt5.QtGui import QFont
from PyQt5 import QtCore
import requests

class AgePredictionApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('Prédiction d\'âge')
        self.setGeometry(300, 300, 400, 200)

        # Styling
        self.setStyleSheet("QWidget { background-color: #f0f0f0; }"
                           "QLabel { font-size: 14px; color: #333; }"
                           "QLineEdit, QPushButton { font-size: 14px; }"
                           "QPushButton { background-color: #4CAF50; color: white; border: none; padding: 10px; }"
                           "QPushButton:hover { background-color: #45a049; }"
                           )

        # Widgets
        self.name_input = QLineEdit(self)
        self.name_input.setPlaceholderText("Entrez un nom...")
        self.age_label = QLabel(self)
        self.age_label.setAlignment(QtCore.Qt.AlignCenter)
        self.submit_button = QPushButton('Obtenir l\'âge', self)
        self.submit_button.clicked.connect(self.get_age)

        # Layout
        layout = QVBoxLayout()
        layout.addWidget(QLabel('Entrez un nom :'))
        layout.addWidget(self.name_input)
        layout.addWidget(self.submit_button)
        layout.addWidget(self.age_label)
        layout.setSpacing(15)
        layout.setContentsMargins(20, 20, 20, 20)

        self.setLayout(layout)

    def get_age(self):
        name = self.name_input.text()
        age_result = get_age_prediction(name)
        self.age_label.setText(age_result)


def get_age_prediction(name):
    api_url = f"https://api.agify.io?name={name}"

    try:
        response = requests.get(api_url)
        response.raise_for_status()

        data = response.json()

        if 'age' in data:
            age_prediction = data['age']
            return f"L'âge probable de '{name}' est : {age_prediction} ans." if age_prediction!= None else f"Il n'y a pas destimation d'âge pour : {name}"
        else:
            return "Impossible d'obtenir une prédiction d'âge pour ce nom."

    except requests.exceptions.RequestException as e:
        return f"Une erreur s'est produite lors de la requête à l'API Agify : {e}"


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = AgePredictionApp()
    window.show()
    sys.exit(app.exec_())