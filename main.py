import threading
from kivy.lang import Builder
from kivymd.app import MDApp
# To set the reference size to your display
# Used in the .kv file
from kivy.metrics import dp
from kivymd.icon_definitions import md_icons
from kivymd.uix.button import MDTextButton
# To set up for multiple windows
from kivymd.uix.screenmanager import ScreenManager
from kivy.uix.screenmanager import Screen, ScreenManager
from kivymd.uix.screenmanager import MDScreenManager
# To change the screen size
from kivy.core.window import Window
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.menu import MDDropdownMenu
from kivy.utils import platform
from kivy.uix.label import Label
from kivy.core.text import Label as CoreLabel
from threading import Thread , ThreadError
from kivymd.uix.snackbar import MDSnackbar
from kivymd.uix.label import MDLabel
from kivy.clock import mainthread
# from kivymd.uix.appbar import MDTopAppBarLeadingButtonContainer
import requests
import ast
from datetime import datetime

#ghghgh
print(platform)
# Getting ip information

ip_information  =  open(self.user_data_dir + "server info.zyon", "r")
read_ip_information = ip_information.readlines()

light_url = "http://" + str(read_ip_information[0].strip()) + ":" + str(read_ip_information[1].strip())
sensor_url = "http://" + str(read_ip_information[0].strip()) + ":" + str(read_ip_information[2].strip())
sending_url = "http://" + str(read_ip_information[0].strip()) + ":" + str(read_ip_information[4].strip())
prefrences_url = "http://" + str(read_ip_information[0].strip()) + ":" + str(read_ip_information[3].strip())
ip_information.close()

print(light_url)
print(sensor_url)
# # url for light server
# light_url = "http://74.105.96.160:2222"
# # url for sensor server
# sensor_url = "http://74.105.96.160:3333"

#from kivymd.uix.behaviors import LongPressBehavior

class MainWindow(Screen):
    pass
class WIfiWindow(Screen):
    pass
class ChandelierWindow(Screen):
    pass
class LibraryWindow(Screen):
    pass
class SconeWindow(Screen):
    pass
class MapWindow(Screen):
    pass
class Welcome(Screen):
    pass
class AccountInfoWindow(Screen):
    pass
class BackgroundThemeWindow(Screen):
    pass
class ServerConnectionWindow(Screen):
    pass
class AboutWindow(Screen):
    pass
class ContactUsWindow(Screen):
    pass
class SecretWindow(Screen):
    pass
class WindowManager(ScreenManager):
    pass
class Zyon(MDApp):
    rel_x1 = 61 / 651
    rel_y1 = 998 / 1013
    rel_x2 = 101 / 651
    rel_y2 = 998 / 1013

    current_theme = open(self.user_data_dir + "theme_pack.zyon", "r")
    current_read_theme = current_theme.readlines()
    primary_color = ast.literal_eval(current_read_theme[0])
    secondary_color = ast.literal_eval(current_read_theme[1])
    background_primary_color = ast.literal_eval(current_read_theme[2])
    text_color_primaryy = str(current_read_theme[3]).strip("\n")
    text_color_secondary = str(current_read_theme[4]).strip("\n")
    # icon_color = ast.literal_eval(current_read_theme[4])
    # secondary_text_color = ast.literal_eval(current_read_theme[5])
    # background_secondary_color = ast.literal_eval(current_read_theme[3])
    print(primary_color)
    # 82/255, 208/255, 236/255, 1 this is the color of the blue active lights
    # 6/255, 18/255, 59/255, 1 basic background color

    # backgroundcolour = ast.literal_eval(current_read_theme[0])
    # primary_color = 6/255, 18/255, 59/255, 1
    def on_start(self):
        # backgroundcolour = [0, 0, 1, 1]

        self.iphonemapscreen = "Map View"
        self.mainscreen = "Main Window"
        self.accountscreen = "Account Info Screen"
        self.start_server_thread()

        self.set_account_settings()
        self.set_server_settings()

        try:
            open(self.user_data_dir + "settings.txt", "r")
        except:
            open(self.user_data_dir +"settings.txt", "w").write("True")
#self.user_data_dir
        setting = open(self.user_data_dir + "settings.txt", "r")
        statement = str(setting.readline())
        print(setting.readline())
        setting.close()
        if statement == "True":
            print("first time")
            self.root.current = "welcome_page"
            setting = open(self.user_data_dir + "settings.txt", "w")
            setting.write("False")
            setting.close()
            current_date = datetime.now()
            formatted_date = current_date.strftime('%B %d, %Y')

            file = open(self.user_data_dir + "installation date.zyon", "w")
            file.write(str(formatted_date))
            file.close()
        else:
            self.root.current = "Map View"
        #self.primary_color = 6/255, 18/255, 59/255, 1
    def change_background(self):

        open(self.user_data_dir + "theme_pack.zyon", "w").write("[0.3215686274509804, 0.8156862745098039, 0.9254901960784314, (1)]")
        self.root.get_screen("Background Page").ids.grid_layout_check.canvas.before.flag_update()

        print("asked for the update")
        # self.root.get_screen("Background Page").ids.color_setting.rgba = 0.5,1,1,1
    def switch_theme(self, option):
        file = open(self.user_data_dir + "theme_pack.zyon", "w")
        if option == "Default":
            file.write("[0.3215686274509804, 0.8156862745098039, 0.9254901960784314, 1]\n")
            file.write("[0.0627450980392157, 0.1137254901960784, 0.2549019607843137, 1]\n")
            file.write("[0.0235294117647059, 0.0705882352941176, 0.2313725490196078, 1]\n")
            file.write("black\n")
            file.write("white")
            file.close()
            print("Written")

        if option == "Midnight":
            file.write("[0.7843137254901961, 0.4509803921568627, 0.9176470588235294, 1]\n")
            file.write("[0.5137254901960784, 0.5686274509803922, 1, 1]\n")
            file.write("[0.203921568627451, 0.1725490196078431, 0.7176470588235294, 1]\n")
            file.write("black\n")
            file.write("white")
            file.close()
            print("Written")

        if option == "Sunset":
            file.write("[1.008888888888889, 0.2627450980392157, 0.5568627450980392, 1]\n")
            file.write("[1, 0.5568627450980392, 0.4862745098039216, 1]\n")
            file.write("[1, 0.4392156862745098, 0.4901960784313725, 1]\n")
            file.write("black\n")
            file.write("white")
            file.close()
            print("Written")

        if option == "Light Mode":
            file.write("[0.6549019607843137, 0.3568627450980392, 0.0941176470588235, 1]\n")
            file.write("[1, 0.6666666666666667, 0.0980392156862745, 1]\n")
            file.write("[1, 0.7882352941176471, 0.4627450980392157, 1]\n")
            file.write("white\n")
            file.write("black")
            file.close()
            print("Written")

        if option == "Sunny days":
            file.write("[0.4274509803921569, 0.3098039215686275, 0.5803921568627451, 1]\n")
            file.write("[0.4901960784313725, 0.4745098039215686, 0.5803921568627451, 1]\n")
            file.write("[0.0588235294117647, 0.0509803921568627, 0.2784313725490196, 1]\n")
            file.write("white\n")
            file.write("black")
            file.close()
            print("Written")

        if option == "Meadow":
            file.write("[0.48627450980392156, 0.7215686274509804, 0.7372549019607844, 1]\n")
            file.write("[0.7764705882352941, 0.7568627450980392, 0.3882352941176471, 1]\n")
            file.write("[0.33725490196078434, 0.4196078431372549, 0.14901960784313725, 1]\n")
            file.write("black\n")
            file.write("white")
            file.close()
            print("Written")

        if option == "Hogwarts":
            file.write("[0.4549019607843137, 0.4823529411764706, 0.4627450980392157, 1]\n")
            file.write("[0.42745098039215684, 0.30196078431372547, 0.0, 1]\n")
            file.write("[0.403921568627451, 0.11372549019607843, 0.11372549019607843, 1]\n")
            file.write("white\n")
            file.write("black")
            file.close()
            print("Written")

        if option == "Forest":
            file.write("[0.6196078431372549, 0.42745098039215684, 0.16470588235294117, 1]\n")
            file.write("[0.24313725490196078, 0.403921568627451, 0.23529411764705882, 1]\n")
            file.write("[0.3411764705882353, 0.5294117647058824, 0.4588235294117647, 1]\n")
            file.write("black\n")
            file.write("white")
            file.close()
            print("Written")

        if option == "Sea":
            file.write("[0.4901960784313725, 0.7215686274509804, 0.9568627450980393, 1]\n")
            file.write("[0.20392156862745098, 0.34509803921568627, 0.6, 1]\n")
            file.write("[0.2901960784313726, 0.6980392156862745, 0.792156862745098, 1]\n")
            file.write("black\n")
            file.write("white")
            file.close()
            print("Written")
    def set_account_settings(self):
        account_settings = open(self.user_data_dir +"account_settings.zyon", "r")
        readline_account_setting = account_settings.readlines()
        self.root.get_screen("Account Info Page").ids.name_input.text = readline_account_setting[0]
        self.root.get_screen("Account Info Page").ids.notification_switch.active = readline_account_setting[1]
        self.root.get_screen("Account Info Page").ids.phone_input.text = readline_account_setting[2]
        self.root.get_screen("Account Info Page").ids.rain_switch.active = readline_account_setting[3]
        self.root.get_screen("Account Info Page").ids.rain_menu_button.text = readline_account_setting[4]
        self.root.get_screen("Account Info Page").ids.light_switch.active = readline_account_setting[5]
        self.root.get_screen("Account Info Page").ids.light_menu_button.text = readline_account_setting[6]
        self.root.get_screen("Account Info Page").ids.door_switch.active = readline_account_setting[7]
        self.root.get_screen("Account Info Page").ids.door_menu_button.text = readline_account_setting[8]
        account_settings.close()
        file = open(self.user_data_dir +"installation date.zyon", "r")
        read_file = file.readlines()[0].strip()
        self.root.get_screen("Account Info Page").ids.app_installation_date.text = str(str(read_file) + "    ")
        file.close()
    def set_server_settings(self):
        intiial_file = (open(self.user_data_dir +"server info.zyon", "r"))
        file = intiial_file.readlines()
        self.root.get_screen("Server Connection Page").ids.server_ip_info.text = file[0].strip()
        self.root.get_screen("Server Connection Page").ids.light_port_info.text = file[1].strip()
        self.root.get_screen("Server Connection Page").ids.sensor_port_info.text = file[2].strip()
        self.root.get_screen("Server Connection Page").ids.preferences_port_info.text = file[3].strip()
        self.root.get_screen("Server Connection Page").ids.sending_port_info.text = file[4].strip()
        intiial_file.close()
    def save_switch_to_main_account(self):
        self.root.current = 'Main Window'

        name_info = self.root.get_screen("Account Info Page").ids.name_input.text
        notification_switch = self.root.get_screen("Account Info Page").ids.notification_switch.active
        phone_info = self.root.get_screen("Account Info Page").ids.phone_input.text
        rain_switch = self.root.get_screen("Account Info Page").ids.rain_switch.active
        rain_input = self.root.get_screen("Account Info Page").ids.rain_menu_button.text
        light_switch = self.root.get_screen("Account Info Page").ids.light_switch.active
        light_input = self.root.get_screen("Account Info Page").ids.light_menu_button.text
        door_switch = self.root.get_screen("Account Info Page").ids.door_switch.active
        door_input = self.root.get_screen("Account Info Page").ids.door_menu_button.text

        account_settings = open(self.user_data_dir +"account_settings.zyon", "w")
        account_settings.write(str(name_info).strip() + "\n")
        account_settings.write(str(notification_switch).strip() + "\n")
        account_settings.write(str(phone_info).strip() + "\n")
        account_settings.write(str(rain_switch).strip() + "\n")
        account_settings.write(str(rain_input).strip() + "\n")
        account_settings.write(str(light_switch).strip() + "\n")
        account_settings.write(str(light_input).strip() + "\n")
        account_settings.write(str(door_switch).strip() + "\n")
        account_settings.write(str(door_input).strip())
        account_settings.close()

        #TODO: make sure to make it so it will send the file to the server for processing
    def save_switch_to_main_secret(self):
        self.root.current = 'Main Window'
    def save_switch_to_main_theme(self):
        self.root.current = 'Main Window'
    def save_switch_to_main_server(self):
        self.root.current = 'Main Window'
        file = open(self.user_data_dir +"server info.zyon", "w")
        file.write(str(self.root.get_screen("Server Connection Page").ids.server_ip_info.text).strip() + "\n")
        file.write(str(self.root.get_screen("Server Connection Page").ids.light_port_info.text).strip() + "\n")
        file.write(str(self.root.get_screen("Server Connection Page").ids.sensor_port_info.text).strip() + "\n")
        file.write(str(self.root.get_screen("Server Connection Page").ids.preferences_port_info.text).strip() + "\n")
        file.write(str(self.root.get_screen("Server Connection Page").ids.sending_port_info.text).strip())
        file.close()
    def save_switch_to_main_about(self):
        self.root.current = 'Main Window'
    def save_switch_to_main_contact(self):
        self.root.current = 'Main Window'
    def start_server_thread(self):
        threading.Thread(target= self.light_server).start()
        threading.Thread(target=self.sensor_server).start()
    def light_server(self):
        print("Starting Server For Lights")
        while True:
            try:
                lights_data = requests.get(light_url)
                l_data = lights_data
                self.set_light(l_data)

            except:
                print("g")
                self.send_error(code = "1404")
    def sensor_server(self):
        print("Starting Server For Sensors")
        while True:
            try:

                sensor_data = requests.get(sensor_url)
                s_data = sensor_data
                self.set_sensor(s_data)
                print("worked")
            except:
                print("y")
                self.send_error(code = "1408")
    def build(self):
        Window.size = (393,852) # regular
        # Window.size = (430, 932) # pro max
        return Builder.load_file("main.kv")
        #self.primary_color = 6 / 255, 18 / 255, 59 / 255, 1
        menu_items = [
            {
                "text": f"{i}",
                "on_release": lambda x=f"Item {i}": self.menu_callback(x),
            } for i in range(5)
        ]
        self.rain_dropdown1 = MDDropdownMenu(items=menu_items, width_multi=4, caller=self.root.get_screen(self.accountscreen).ids.rain_menu_button)
    @mainthread
    def send_error(self, code):
        MDSnackbar(
            MDLabel(text="Please Contact Support With Error Code: " + str(code))
        ).open()
        print(str(code))
    @mainthread
    def set_sensor(self, p_data):
        try:

            fpw = str(p_data.text).split("\n")[0]
            brw = str(p_data.text).split("\n")[1]
            gw = str(p_data.text).split("\n")[2]
            bw = str(p_data.text).split("\n")[3]
            sw = str(p_data.text).split("\n")[4]
            kw = str(p_data.text).split("\n")[5]
            lw = str(p_data.text).split("\n")[6]
            gd = str(p_data.text).split("\n")[7]
            sd = str(p_data.text).split("\n")[8]
            ld = str(p_data.text).split("\n")[9]
            boned = str(p_data.text).split("\n")[10]
            btwod = str(p_data.text).split("\n")[11]
            kd = str(p_data.text).split("\n")[13]
            guestw = str(p_data.text).split("\n")[14]

            print()

            try:
                if "fpw" in fpw:
                    if "0" in fpw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.fpw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.fpw = (1, 0, 0, 1)

                if "brw" in brw:
                    if "0" in brw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.brw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.brw = (1, 0, 0, 1)

                if "gw" in gw:
                    if "0" in gw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.gw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.gw = (1, 0, 0, 1)

                if "bw" in bw:
                    if "0" in bw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.bw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.bw = (1, 0, 0, 1)

                if "sw" in sw:
                    if "0" in sw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.sw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.sw = (1, 0, 0, 1)

                if "kw" in kw:
                    if "0" in kw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.kw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.kw = (1, 0, 0, 1)

                if "lw" in lw:
                    if "0" in lw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.lw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.lw = (1, 0, 0, 1)

                if "gd" in gd:
                    if "0" in gd:
                         self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.gd = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.gd = (1, 0, 0, 1)

                if "sd" in sd:
                    if "0" in sd:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.sd = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.sd = (1, 0, 0, 1)

                if "ld" in ld:
                    if "0" in ld:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.ld = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.ld = (1, 0, 0, 1)

                if "boned" in boned:
                    if "0" in boned:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.boned = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.boned = (1, 0, 0, 1)

                if "btwod" in btwod:
                    if "0" in btwod:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.btwod = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.btwod = (1, 0, 0, 1)

                if "kd" in kd:
                    if "0" in kd:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.kd = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.kd = (1, 0, 0, 1)

                if "guestw" in guestw:
                    if "0" in guestw:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.guestw = (0, 1, 0, 1)
                    else:
                        self.root.get_screen(self.iphonemapscreen).ids.main_floor_marking.guestw = (1, 0, 0, 1)

            except:
                pass

        except:
            pass
    @mainthread
    def set_light(self, s_light):
        try:
            drivway_light_sts = str(s_light.text).split("\n")[0]
            outside_sts = str(s_light.text).split("\n")[1]
            front_round_sts = str(s_light.text).split("\n")[2]
            front_flood_sts = str(s_light.text).split("\n")[3]
            game_room_sts = str(s_light.text).split("\n")[4]
            garage_door_carrage_sts = str(s_light.text).split("\n")[5]
            front_scone_sts = str(s_light.text).split("\n")[6]
            chandelier_sts = str(s_light.text).split("\n")[7]
            chandelier_dim_val = str(s_light.text).split("\n")[8]
            scone_sts = str(s_light.text).split("\n")[9]
            scone_dim_val = str(s_light.text).split("\n")[10]
            bookshelf_sts = str(s_light.text).split("\n")[11]
            round_room_sts = str(s_light.text).split("\n")[12]
            round_room_dim_val = str(s_light.text).split("\n")[13]
            baxkyard_sts = str(s_light.text).split("\n")[14]
            print(front_round_sts)

            try:
                #TODO: add main screen buttons
                if "0" in front_round_sts:

                    self.root.get_screen(self.iphonemapscreen).ids.front_round_room_lights.md_bg_color = (0.827, 0.827, 0.827, 0.5)

                else:

                    self.root.get_screen(self.iphonemapscreen).ids.front_round_room_lights.md_bg_color = (1, 0.85, 0.31, 1)


                if  "0" in round_room_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.library_light_button.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.library_light_button.md_bg_color = (1, 0.85, 0.31, 1)

                if  "0" in baxkyard_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.backyard_flood_button.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                    self.root.get_screen(self.iphonemapscreen).ids.backyard_flood_light_button_2.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.backyard_flood_button.md_bg_color = (1, 0.85, 0.31, 1)
                    self.root.get_screen(self.iphonemapscreen).ids.backyard_flood_light_button_2.md_bg_color = (1, 0.85, 0.31, 1)

                if  "0" in chandelier_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.chandelier_button.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                    self.root.get_screen(self.mainscreen).ids.chandelier_button.md_bg_color = (16/255, 29/255, 65/255, 1)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.chandelier_button.md_bg_color = (1, 0.85, 0.31, 1)
                    self.root.get_screen(self.mainscreen).ids.chandelier_button.md_bg_color = (16 / 255, 29 / 255, 65 / 255, 1)
                if "0" in front_scone_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.front_door_button.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.front_door_button.md_bg_color = (1, 0.85, 0.31, 1)

                if  "0" in front_flood_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.front_flood_button.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.front_flood_button.md_bg_color = (1, 0.85, 0.31, 1)

                if  "0" in game_room_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.slope_light_button.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.slope_light_button.md_bg_color = (1, 0.85, 0.31, 1)

                if  "0" in outside_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.outside_kitchen_button.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.outside_kitchen_button.md_bg_color = (1, 0.85, 0.31, 1)

                if  "0" in scone_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.scone_button_r.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.scone_button_r.md_bg_color = (1, 0.85, 0.31, 1)

                if  "0" in garage_door_carrage_sts:
                    self.root.get_screen(self.iphonemapscreen).ids.garage_carrage_light_button_1.md_bg_color = (0.827, 0.827, 0.827, 0.5)
                else:
                    self.root.get_screen(self.iphonemapscreen).ids.garage_carrage_light_button_1.md_bg_color = (1, 0.85, 0.31, 1)

            except:
                pass

        except:
            self.send_error(code="1409")
    def open_screen(self, x):
        self.root.current = x
    # TODO: remove test
    def test(self):
        print("worked ya")
    def set_device(self, x):
        try:
            open(self.user_data_dir +"modeltype.txt", "r")
        except:
            model = open(self.user_data_dir + "modeltype.zyon", "w")
            model.write(x)
            model.close()
        else:
            model = open(self.user_data_dir + "modeltype.zyon", "w")
            model.write(x)
            model.close()

        self.root.current = "Main Window"
        #getting the position of click
    def handle_click(self, touch_x, touch_y):
        print(f"Clicked at X: {touch_x}, Y: {touch_y}")
        # checking for double tap to open dimmer panel
        # TODO: ADD haptic touch or vibration when pressed
    def set_rain_timout(self, option):
        self.root.get_screen("Account Info Page").ids.rain_menu_button.text = str(option)
        self.rain_dropdown1.dismiss()
    def set_light_timeout(self, option):
        self.root.get_screen("Account Info Page").ids.light_menu_button.text = str(option)
        self.light_dropdown1.dismiss()
    def set_door_timout(self, option):
        self.root.get_screen("Account Info Page").ids.door_menu_button.text = str(option)
        self.door_dropdown1.dismiss()
    def open_rain_menu(self):
        menu_items = [
            {
                "text": '30 Min',
                "on_release": lambda: self.set_rain_timout("30 Min"),
                # "on_release" : self.root.get_screen("Account Info Page").ids.rain_menu_button.text == "30 Min",

            },
            {
                "text": '1 Hr',
                "on_release": lambda: self.set_rain_timout("1 Hr"),

            },
            {
                "text": '2 Hr',
                "on_release": lambda: self.set_rain_timout("2 Hr"),

            },
            {
                "text": '3 Hr',
                "on_release": lambda: self.set_rain_timout("3 Hr"),

            },

        ]


        self.rain_dropdown1 = MDDropdownMenu(items=menu_items, position = "bottom" ,width=dp(240),caller=self.root.get_screen("Account Info Page").ids.rain_menu_button)
        self.rain_dropdown1.open()
    def open_light_menu(self):
        menu_items = [
            {
                "text": '12 AM',
                "on_release": lambda: self.set_light_timeout("12 AM"),

            },
            {
                "text": '1 AM',
                "on_release": lambda: self.set_light_timeout("1 AM"),

            },
            {
                "text": '2 AM',
                "on_release": lambda: self.set_light_timeout("2 AM"),

            },
            {
                "text": '3 AM',
                "on_release": lambda: self.set_light_timeout("3 AM"),

            },

        ]


        self.light_dropdown1 = (MDDropdownMenu(items=menu_items, position = "bottom" ,width=dp(240),caller=self.root.get_screen("Account Info Page").ids.light_menu_button))
        self.light_dropdown1.open()
    def door_light_menu(self):
        menu_items = [
            {
                "text": '12 AM',
                "on_release": lambda: self.set_door_timout("12 AM"),

            },
            {
                "text": '1 AM',
                "on_release": lambda: self.set_door_timout("1 AM"),

            },
            {
                "text": '2 AM',
                "on_release": lambda: self.set_door_timout("2 AM"),

            },
            {
                "text": '3 AM',
                "on_release": lambda: self.set_door_timout("3 AM"),

            },

        ]


        self.door_dropdown1 = (MDDropdownMenu(items=menu_items, position = "bottom" ,width=dp(240),caller=self.root.get_screen("Account Info Page").ids.light_menu_button))
        self.door_dropdown1.open()
    def secret_menu(self):
        self.root.current = 'secret menu'
    def check_double_tap(self, card, touch):
        if touch.is_double_tap:
            print("Double-tap detected")
            self.root.current = "Chandelier Window"
    # TODO: ADD haptic touch or vibration when pressed
    # check for double tap then open special page for dimmer panel
    def check_double_tap_scone(self, card, touch):
        if touch.is_double_tap:
            print("Double-tap detected")
            self.root.current = "Scone Window"
    # TODO: ADD haptic touch or vibration when pressed
    # check for double tap then open special page for dimmer panel
    def check_double_tap_library(self, card, touch):
        if touch.is_double_tap:
            print("Double-tap detected")
            self.root.current = "Library Window"
    # initalisation of menu items
    def show_menu(self):
        menu_items = [
            {
                "text": "Home",
                "on_release": lambda x="Main Window": self.open_screen(x),
            },
            {
                "text": "Floor View",
                "on_release": lambda x="Map View": self.open_screen(x),
            }
        ]
        MDDropdownMenu(caller = self.root.get_screen("Main Window").ids.menu_caller, items = menu_items).open()
Zyon().run()
#TODO: create send commands

# TODO: button cammands