from appJar import gui
def press(button):
    if button == "Cancel":
        print("Close")
        app.stop()
    else:
        button == "Sumbit"
        print("Sumbit")

app = gui("Translete", "1400x800")
app.setBg("orange")
app.setFont(18)
app.addLabel("title", "Welcome to our site")
app.setLabelBg("title", "blue")
app.setLabelFg("title", "orange")

app.addLabelEntry("Username")
app.addLabelSecretEntry("Password")
app.addButtons(["Submit", "Cancel"], press)

app.setFocus("Username")

app.go()
