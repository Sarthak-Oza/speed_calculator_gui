from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QGridLayout, QLineEdit, QWidget, \
    QComboBox, QPushButton, QMessageBox


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        layout = QGridLayout()
        self.setWindowTitle("Speed Calculator")

        # Create Widgets

        distance_label = QLabel("Distance")
        self.distance_input_box = QLineEdit()
        self.distance_unit = QComboBox()
        self.distance_unit.addItems(["Kilometers", "Miles"])

        time_label = QLabel("Time (Hour)")
        self.time_input_box = QLineEdit()

        self.output = QLabel()

        calculate_button = QPushButton("Calculate")
        # Run calculate method upon button click

        calculate_button.clicked.connect(self.calculate)

        # Add Widgets

        layout.addWidget(distance_label, 0, 0)
        layout.addWidget(self.distance_input_box, 0, 1)
        layout.addWidget(self.distance_unit, 0, 2)

        layout.addWidget(time_label, 1, 0)
        layout.addWidget(self.time_input_box, 1, 1)

        layout.addWidget(calculate_button, 3, 1)
        layout.addWidget(self.output, 4, 1)

        widget = QWidget()
        widget.setLayout(layout)

        self.setCentralWidget(widget)

    # Method to calculate speed
    def calculate(self):
        try:
            dis = float(self.distance_input_box.text())
            time = float(self.time_input_box.text())
            dis_unit = self.distance_unit.currentText()
            speed = round(dis / time, 2)
            self.output.setText(f"Speed: {speed} {dis_unit} / Hour")

        # Handle error
        except:
            self.distance_input_box.setText("")
            self.time_input_box.setText("")
            message_box = QMessageBox(self)
            message_box.setWindowTitle("Error")
            message_box.setText("Please enter valid values!")
            message_box.exec()

app = QApplication([])

window = MainWindow()
window.show()

app.exec()
