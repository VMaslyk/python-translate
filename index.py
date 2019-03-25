from appJar import gui
def press(button):
    if button == "Cancel":
        app.stop()
    else:
        usr = app.getEntry("Username")
        pwd = app.getEntry("Password")
        print("User:", usr, "Pass:", pwd)
app = gui("Login Window", "400x200")
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
