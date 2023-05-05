from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import sqlite3, EncryptDecrypt as ED
class ShowPasswords(GridLayout):
    def __init__(self, **kwargs):
        super(ShowPasswords, self).__init__(**kwargs)
        conn = sqlite3.connect("Logins.db")
        c = conn.cursor()
        c.execute("SELECT *,oid FROM LoginPassword")
        records = c.fetchall()
        c.close()
        print_records = ""
        for record in records:
            print_records += "Website: " + str(record[0]) + "\n Username:" + str(record[1]) + "\n Password:" + str(ED.decrypt(record[2])) + "\n\n"
        self.top_grid = GridLayout()
        self.top_grid.cols = 1
        self.top_grid.add_widget(Label(text=f'Username: {record[1]}'))
        self.username = TextInput(multiline=False)
        self.top_grid.add_widget(self.username)
        self.top_grid.add_widget(Label(text='Password'))
        self.cols = 1
        self.password = TextInput(password=True, multiline=False)
        self.top_grid.add_widget(self.password)
        self.add_widget(self.top_grid)
        self.submit = Button(text="Submit")
        self.add_widget(self.submit)
        self.submit.bind(on_press=self.submit_pressed)
    def submit_pressed(self):
        return


class MyApp(App):
    def build(self):
        return ShowPasswords()


if __name__ == '__main__':
    MyApp().run()