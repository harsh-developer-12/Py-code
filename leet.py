#   <- palendrom <-

# 
# pal= input("enter aa word")
# if str(pal) == str(pal)[::-1]:
#      print ("word is palendrom")
# else:
#  print ("not palendrom ")



import sys
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QFrame, QLabel

app = QApplication(sys.argv)

window = QWidget()
window.resize(400, 300)

main_layout = QVBoxLayout()

# Header
header = QFrame()
header.setStyleSheet("background-color: lightblue;")
header_layout = QVBoxLayout(header)
header_layout.addWidget(QLabel("Header"))

# Content
content = QFrame()
content.setStyleSheet("background-color: lightyellow;")
content_layout = QVBoxLayout(content)
content_layout.addWidget(QLabel("Content Area"))

# Footer
footer = QFrame()
footer.setStyleSheet("background-color: lightgreen;")
footer_layout = QVBoxLayout(footer)
footer_layout.addWidget(QLabel("Footer"))

main_layout.addWidget(header)
main_layout.addWidget(content)
main_layout.addWidget(footer)

window.setLayout(main_layout)

window.show()
sys.exit(app.exec_())



