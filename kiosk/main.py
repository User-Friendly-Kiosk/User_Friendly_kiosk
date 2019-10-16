from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from sympy.physics.quantum.tests.test_pauli import sm
from kivy.core.window import Window
from kivy.core.text import LabelBase

LabelBase.register(name="NanumMyeongjo", fn_regular="NanumMyeongjo.ttf")

from application.kiosk.database import DataBase

import application.age.demo

checking = False
age=0
gender = ""

'''Make full screen'''
'''Window.fullscreen=True'''
Window.fullscreen='auto'

'''
class CreateAccountWindow(Screen):
    namee = ObjectProperty(None)
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def submit(self):
        if self.namee.text != "" and self.email.text != "" and self.email.text.count("@") == 1 and self.email.text.count(".") > 0:
            if self.password != "":
                db.add_user(self.email.text, self.password.text, self.namee.text)

                self.reset()

                sm.current = "login"
            else:
                invalidForm()
        else:
            invalidForm()

    def login(self):
        self.reset()
        sm.current = "login"

    def reset(self):
        self.email.text = ""
        self.password.text = ""
        self.namee.text = ""


class LoginWindow(Screen):
    email = ObjectProperty(None)
    password = ObjectProperty(None)

    def loginBtn(self):
        if db.validate(self.email.text, self.password.text):
            MainWindow.current = self.email.text
            self.reset()
            sm.current = "main"
        else:
            invalidLogin()

    def createBtn(self):
        self.reset()
        sm.current = "create"

    def reset(self):
        self.email.text = ""
        self.password.text = ""


class MainWindow(Screen):
    n = ObjectProperty(None)
    created = ObjectProperty(None)
    email = ObjectProperty(None)
    current = ""

    def logOut(self):
        sm.current = "login"

    def on_enter(self, *args):
        password, name, created = db.get_user(self.current)
        self.n.text = "Account Name: " + name
        self.email.text = "Email: " + self.current
        self.created.text = "Created On: " + created


def invalidLogin():
    pop = Popup(title='Invalid Login',
                  content=Label(text='Invalid username or password.'),
                  size_hint=(None, None), size=(400, 400))
    pop.open()


def invalidForm():
    pop = Popup(title='Invalid Form',
                  content=Label(text='Please fill in all inputs with valid information.'),
                  size_hint=(None, None), size=(400, 400))

    pop.open()

'''

class First(Screen):
    def faceRecognition(self):
        sm.current = "Face"


class Face(Screen):

    def on_enter(self):

        '''나이, 성별을 측정한 후 다음 화면으로 전환 해줘야 함'''
        '''getAgeGender()'''

        checking = True
        if(checking==True):
            sm.current = "Select"

'''
def getAgeGender():
    label = application.age.demo.main()
    print(label)
'''

class Select(Screen):
    def showMenu(self):
        sm.current="ShowMenu"

    def backButton(self):
        sm.current = "First"

class ShowMenu(Screen):
    def payment(self):
        sm.current="Payment"

    def backButton(self):
        sm.current = "Select"

class Payment(Screen):
    def payment(self):
        sm.current="Payment"

    def backButton(self):
        sm.current = "ShowMenu"

    def finish(self):
        sm.current="Finish"

class Finish(Screen):
    def payment(self):
        sm.current="Finish"


class WindowManager(ScreenManager):
    pass


kv = Builder.load_file("my.kv")

sm = WindowManager()
db = DataBase("users.txt")


screens = [First(name="First"), Face(name="Face"), Select(name="Select"), ShowMenu(name="ShowMenu"), Payment(name="Payment"), Finish(name="Finish")]

for screen in screens:
    sm.add_widget(screen)

sm.current = "First"


class MyMainApp(App):
    def build(self):
        return sm


if __name__ == "__main__":
    MyMainApp().run()