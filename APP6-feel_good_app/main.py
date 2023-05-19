from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import json, glob, random
from hoverable import HoverBehavior
from kivy.uix.image import Image
from kivy.uix.behaviors import ButtonBehavior
from datetime import datetime
from pathlib import Path

Builder.load_file("design.kv")         # connecting main python file and kivy file

class LoginScreen(Screen):              #class for LoginScreen(name of class and name in kivy should be same for all)
    def sign_up(self):                  #name of function should also match with that written in kivy
        self.manager.current = "signup_screen"          #switching screens

    def login(self, u, p):
        with open('users.json') as file:
            users = json.load(file)             # users is a dictionary
            
        if u in users and users[u]['password'] == p:
            self.manager.current = "login_success_screen"
        else:
            self.ids.wrong_login.text = "Incorrect username or password"        #accessing text of label

    def forget(self, u):
        with open("users.json") as file:
            users = json.load(file)
        
        if u in users:
            self.ids.wrong_login.text = "Password is "+users[u]["password"]
        else:
            self.ids.wrong_login.text = "enter valid username"


class RootWidget(ScreenManager):           #class for Rootwidget
    pass

class SignUpScreen(Screen):
    def add_user(self, u, p, cp):
        with open('users.json') as file:
            users = json.load(file)                #load json data as a dictionary called users in python
        
        if(p == cp):
            users[u] = {"username":u, "password":p, 
            "created": datetime.now().strftime(
            "%Y-%m-%d %H-%M-%S") } 

            with open('users.json','w') as file1:
                json.dump(users, file1)                 #dump will append the json file
            self.manager.current = "signup_success_screen"
        
        else:
            self.ids.la.text = "Password not matching!"

        

    def back(self):
        self.manager.transition.direction = 'right'
        self.manager.current = 'login_screen'

class SignUpSuccessScreen(Screen):
    def switch(self):
        self.manager.transition.direction = 'right'
        self.manager.current = "login_screen"

class LoginSuccessScreen(Screen):
    def logout(self):
        self.manager.current = "login_screen"

    def get_quote(self, feel):
        feel = feel.lower()
        available_fings = glob.glob('quotes\*txt')

        available_fings = [Path(filename).stem for filename in available_fings]      
        if feel in available_fings:
            with open(f"quotes/{feel}.txt", encoding='utf-8') as file:
                quotes = file.readlines()
            self.ids.dis_quote.text = random.choice(quotes)
        else:
            self.ids.dis_quote.text = "Enter another feeling"

class LogoutButton(ButtonBehavior, HoverBehavior, Image):       #ButtonBehaviour should be written first, as otherwise its characterstics may get hidden
    pass

class MainApp(App):                     #class for MainApp, highest in herierchy
    def build(self):                    #build is a method under App class
        return RootWidget()

if __name__ == "__main__":              #true only when run as standalone and not imported
    MainApp().run()                     #run is a method under App class


