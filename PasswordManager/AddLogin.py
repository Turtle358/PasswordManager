from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
import sqlite3, EncryptDecrypt as ED
#Databases
# Create a database or connect to one
conn = sqlite3.connect("Logins.db")
# Create cursor
c = conn.cursor()

try:
    c.execute("""CREATE TABLE LoginPassword(
        Site VARCHAR(100),
        Username VARCHAR(30),
        Password VARCHAR(30)
        )""")
except:
    pass
c.close()


class LoginScreen(GridLayout):
    def __init__(self, **kwargs):
        super(LoginScreen, self).__init__(**kwargs)
        self.cols = 1
        self.top_grid = GridLayout()
        self.top_grid.cols = 2
        self.showinglogins = False
        self.top_grid.add_widget(Label(text='Site'))
        self.website = TextInput(multiline=False)
        self.top_grid.add_widget(self.website)
        self.top_grid.add_widget(Label(text='User Name'))
        self.username = TextInput(multiline=False)
        self.top_grid.add_widget(self.username)
        self.top_grid.add_widget(Label(text='Password'))
        self.password = TextInput(password=True, multiline=False)
        self.top_grid.add_widget(self.password)
        self.add_widget(self.top_grid)
        self.submit = Button(text="Submit")
        self.add_widget(self.submit)
        self.submit.bind(on_press=self.submit_pressed)

    def submit_pressed(self, btn):
        conn = sqlite3.connect("Logins.db")
        c = conn.cursor()
        c.execute("INSERT INTO LoginPassword VALUES(:Site, :Username, :Password)",
        {
            "Site": self.website.text,
            "Username": self.username.text,
            "Password": ED.encrypt(self.password.text)
        })
        conn.commit()
        c.close()
        self.website.text=""
        self.username.text=""
        self.password.text=""
    def ShowLogins(self, btn):
        if self.showinglogins:
            self.logins.text = ""
            self.showinglogins = False
        else:
            conn = sqlite3.connect("Logins.db")
            c = conn.cursor()
            c.execute("SELECT *,oid FROM LoginPassword")
            records = c.fetchall()
            c.close()
            print_records = ""
            for record in records:
                print_records += "Website: " + str(record[0]) + "\n Username:" + str(record[1]) + "\n Password:" + str(ED.decrypt(record[2])) + "\n\n"
            self.logins.text = print_records
            self.showinglogins = True





class MyApp(App):
    def build(self):
        return LoginScreen()


if __name__ == '__main__':
    MyApp().run()