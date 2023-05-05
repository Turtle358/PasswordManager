from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.scrollview import ScrollView
from kivy.core.window import Window
from kivy.app import App
import sqlite3, AddLogin as AL, EncryptDecrypt as ED

class ScrollUIApp(App):
    def build(self):
        layout1 = GridLayout(cols=2)
        #Add Button
        addbtn = Button(text="+", size_hint_y=None, height=40)
        layout1.add_widget(addbtn)

        layout2 = GridLayout(cols=1, spacing=10, size_hint_y=None)
        # Make sure the height is such that there is something to scroll.
        layout2.bind(minimum_height=layout2.setter('height'))
        #Collect Data For Passwords
        conn = sqlite3.connect("Logins.db")
        c = conn.cursor()
        c.execute("SELECT *,oid FROM LoginPassword")
        records = c.fetchall()
        c.close()
        for record in records:
            print_records = "Website: " + str(record[0]) + "\nUsername:" + str(record[1])
            btn = Button(text=str(print_records), size_hint_y=None, height=40)
            layout2.add_widget(btn)
        root = ScrollView(size_hint=(1, None), size=(Window.width, Window.height))
        root.add_widget(layout1, layout2)
        return root
main = ScrollUIApp()
main.run()