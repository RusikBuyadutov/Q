from kivy.app import App
import webbrowser
from kivy.uix.image import Image
from kivy.uix.button import Button  
from kivy.uix.widget import Widget
from kivy.uix.relativelayout import RelativeLayout 
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import ButtonBehavior
from kivy.uix.boxlayout import BoxLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.button import ButtonBehavior
from kivy.uix.screenmanager import NoTransition
from kivmob import KivMob, TestIds,RewardedListenerInterface
from kivy.uix.screenmanager import FallOutTransition
from kivy.uix.screenmanager import RiseInTransition
from kivy.uix.textinput import TextInput
from kivy.graphics import Color
from kivy.uix.popup import Popup
from kivy.uix.label import Label
from kivy.uix.screenmanager import WipeTransition
from kivy.core.audio import SoundLoader
from kivy.uix.checkbox import CheckBox
from kivy.uix.scrollview import ScrollView
from functools import partial
from kivy.uix.gridlayout import GridLayout
import random
import os

class ImageButton(ButtonBehavior,Image):
    pass
class Menu(Screen):
   pass
class Kategorii(Screen):
    pass
class Pravila(Screen):
    pass
class Pravilakz(Screen):
    pass
class Igrok(Screen):
    pass
class Pravila2(Screen):
    pass
class Pravila3(Screen):
    pass
class Pravila4(Screen):
    pass
class Pravila5(Screen):
    pass
class Pravila6(Screen):
    pass
class Pravila2kz(Screen):
    pass
class Pravila3kz(Screen):
    pass
class Pravila4kz(Screen):
    pass
class Pravila5kz(Screen):
    pass
class Pravila6kz(Screen):
    pass
class Pravila7kz(Screen):
    pass
class Vibor(Screen):
    pass
class Vopros(Screen):
    pass
class Sled(Screen):
    pass
class Leader(Screen):
    pass
class Final(Screen):
    pass
class Info(Screen):
    pass
class Pravila7(Screen):
    pass
class Infokz(Screen):
    pass
class Menudark(Screen):
    pass


GUI=Builder.load_file("Main.kv")    
class MainApp(App):
    global sound_menu
    global igroki_4_10
    global prizz
    global idiot
    global smehh
    smehh=SoundLoader.load("smeh.wav")
    prizz=SoundLoader.load("p.wav")
    idiot=SoundLoader.load("tupoy.wav")
    sound_menu=SoundLoader.load("ZVUK.wav")
    def build(self):
        self.iriska=0
        self.tq=0
        self.v=2
        self.lol=-3
        self.click=3
        self.nomer=0
        self.skolko=1
        self.za=0
        self.protiv=0
        self.kakoy=1
        self.igroki_4_10=[]
        self.skolko1=0
        self.chet=""
        self.rezultat=1
        self.resurs=0
        self.otveti=[]
        self.chet=[0,0,0]
        self.imena=[]
        self.kazak=False
        self.ads = KivMob(TestIds.APP)
        self.ads.new_banner(TestIds.BANNER, top_pos=False)
        self.ads.request_banner()
        self.ads.show_banner()
        self.ads = KivMob(TestIds.APP)
        self.ads.new_interstitial(TestIds.INTERSTITIAL)
        self.ads.request_interstitial()
        return GUI
    def call_rek(self):
        lambda a:self.ads.show_interstitial()
    def on_resume(self):
        self.ads.request_interstitial()
    def infoscr(self):
        if self.kazak==True:
            app.change_screen("infokz_screen")
        if self.kazak==False:
            app.change_screen("info_screen")

    def kazah(self):
        if self.kazak==False:
            self.kazak=True
        else:
            self.kazak=False
        
        
        kzigrat=self.root.ids["menu_screen"].ids["knopkaigrat"]
        kzpravila=self.root.ids["menu_screen"].ids["knopkapravila"]
        kzyazik=self.root.ids["menu_screen"].ids["knopkayazik"]
        kzigrokprodoljit=self.root.ids["igrok_screen"].ids["igrokprodoljit"]
        kzigrok1=self.root.ids["igrok_screen"].ids["igrok1"]
        kzigrok2=self.root.ids["igrok_screen"].ids["igrok2"]
        kzigrok3=self.root.ids["igrok_screen"].ids["igrok3"]
        kzstart=self.root.ids["kategorii_screen"].ids["knopkastart"]
        KzSkelet=self.root.ids["kategorii_screen"].ids["s"]
        KzDobr=self.root.ids["kategorii_screen"].ids["d"]
        KzPol=self.root.ids["kategorii_screen"].ids["p"]
        KzVec=self.root.ids["kategorii_screen"].ids["v"]
        KzMor=self.root.ids["kategorii_screen"].ids["m"]
        Kz18=self.root.ids["kategorii_screen"].ids["i"]
        kzviborvopros=self.root.ids["vibor_screen"].ids["viborvopros"]
        kzza=self.root.ids["vopros_screen"].ids["za"]
        kzprotiv=self.root.ids["vopros_screen"].ids["protiv"]
        kzsledvopros=self.root.ids["leader_screen"].ids["sledvopros"]
        if self.kazak==True:
            
            kzsledvopros.source="kz/nexthod.png"
            kzigrat.source="kz/play.png"
            kzprotiv.source="kz/versus.png"
            kzza.source="kz/za.png"
            kzpravila.source="kz/prav.png"
            kzyazik.source="kz/yaz.png"
            kzigrokprodoljit.source="kz/prodoljit.png"
            kzviborvopros.source="kz/chooseact.png"
            Kz18.source="kz/kat/intim.png"
            kzigrok1.hint_text="Біріншісінің атын енгізіңіз"
            KzMor.source="kz/kat/moral.png"
            kzstart.source="kz/start.png"
            KzVec.source="kz/kat/vech.png"
            kzigrok2.hint_text="Екіншісінің атын енгізіңіз"
            kzigrok3.hint_text="Үшіншісінің атын енгізіңіз"
            KzDobr.source="kz/kat/dobr.png"
            KzPol.source="kz/kat/pol.png"
            KzSkelet.source="kz/kat/skelet.png"
        if self.kazak==False:
            kzsledvopros.source="sled1.png"
            kzigrat.source="Igrat.png"
            kzprotiv.source="Protiv.png"
            kzza.source="Za.png"
            kzpravila.source="Pravila.png"
            kzyazik.source="Yazik.png"
            kzigrokprodoljit.source="Go.png"
            kzviborvopros.source="Vipiros.png"
            Kz18.source="kategory/18.png"
            kzigrok1.hint_text="Введите имя 1-ого"
            KzMor.source="kategory/Moral.png"
            kzstart.source="Start.png"
            KzVec.source="kategory/Vecherinka.png"
            kzigrok2.hint_text="Введите имя 2-ого"
            kzigrok3.hint_text="Введите имя 3-ого"
            KzDobr.source="kategory/Dobrye.png"
            KzPol.source="kategory/Politika.png"
            KzSkelet.source="kategory/Skelet.png"
    def smeh1(self):
        self.iriska+=1
        if self.iriska==5 or self.iriska==10:
            smehh.volume=".3"
            smehh.play()
    def Klik(self):
        sound_klik=SoundLoader.load("zvuk_klik.wav")
        sound_klik.volume=".2"
        sound_klik.play()   
    def priz(self):
        prizz.volume=".3"
        prizz.play()
    def notpriz(self):
        prizz.stop()
    def Zvuk(self):
        zvuk_knopka=self.root.ids["menu_screen"].ids["zvuk"]
        
        if zvuk_knopka.source =="VonOn.png":
            zvuk_knopka.source="VolOFF.png"
            
        else:
            zvuk_knopka.source ="VonOn.png"
            
        if  zvuk_knopka.source=="VonOn.png":
           
            sound_menu.volume=".1"
            sound_menu.play()
            sound_menu.loop=True
        if zvuk_knopka.source=="VolOFF.png":
            sound_menu.stop()
    def change_pravila(self,screen_name):
        
        screen_manager=self.root.ids["screen_manager"]
        screen_manager.transition=WipeTransition() 
        screen_manager.current=screen_name
        
    def change_screen(self,screen_name):
        screen_manager=self.root.ids["screen_manager"]
        
    
        if screen_manager.current == "menu_screen":screen_manager.transition=RiseInTransition()
        
        else:screen_manager.transition=FallOutTransition()     
        
        screen_manager.current=screen_name
    def pravilala(self):
        if self.kazak==True:
            app.change_screen("pravilakz_screen")
        if self.kazak==False:
            app.change_screen("pravila_screen")
        
    def add_player(self):
        if self.kazak==True:
            screen_manager=self.root.ids["screen_manager"]
            if screen_manager.current=="igrok_screen":
                self.click+=1
                k=0
                d=0
                if self.click==4:
                    self.chet.append(0)
                    A=self.root.ids["igrok_screen"].ids["IGROKI"]
                    A.add_widget(TextInput(font_size=40,halign="center",valign="center",hint_text="Төртінің атын енгізіңіз ",background_color=(255/255, 158/255, 128/255, 1),multiline=False,background_normal="Knopka.png"
                            ,background_active="Knopka.png",hint_text_color=(0,0,0,1),on_text_validate=partial(self.proverka2, k)))

                if self.click==5:
                    self.chet.append(0)
                    A=self.root.ids["igrok_screen"].ids["IGROKI"]
                    A.add_widget(TextInput(font_size=40,halign="center",valign="center",hint_text="Бесеуінің атын енгізіңіз ",background_color=(255/255, 158/255, 128/255, 1),multiline=False,background_normal="Knopka.png"
                            ,background_active="Knopka.png",hint_text_color=(0,0,0,1),on_text_validate=partial(self.proverka2, k) ))
                if self.click==6:
                    self.chet.append(0)
                    A=self.root.ids["igrok_screen"].ids["IGROKI"]
                    A.add_widget(TextInput(font_size=40,halign="center",valign="center",hint_text="Алтыншының атын енгізіңіз",background_color=(255/255, 158/255, 128/255, 1),multiline=False,background_normal="Knopka.png"
                            ,background_active="Knopka.png",hint_text_color=(0,0,0,1),on_text_validate=partial(self.proverka2, k) ))
                if self.click==7:
                    self.chet.append(0)
                    A=self.root.ids["igrok_screen"].ids["IGROKI"]
                    A.add_widget(TextInput(font_size=40,halign="center",valign="center",hint_text="Жетіншінің атын енгізіңіз ",background_color=(255/255, 158/255, 128/255, 1),multiline=False,background_normal="Knopka.png"
                            ,background_active="Knopka.png",hint_text_color=(0,0,0,1),on_text_validate=partial(self.proverka2, k) ))
                if self.click==8:
                    self.chet.append(0)
                    A=self.root.ids["igrok_screen"].ids["IGROKI"]
                    A.add_widget(TextInput(font_size=40,halign="center",valign="center",hint_text="Сегізінің атын енгізіңіз ",background_color=(255/255, 158/255, 128/255, 1),multiline=False,background_normal="Knopka.png"
                            ,background_active="Knopka.png",hint_text_color=(0,0,0,1),on_text_validate=partial(self.proverka2, k) ))
                if self.click==9:
                    self.chet.append(0)
                    A=self.root.ids["igrok_screen"].ids["IGROKI"]
                    A.add_widget(TextInput(font_size=40,halign="center",valign="center",hint_text="Тоғызыншының атын енгізіңіз ",background_color=(255/255, 158/255, 128/255, 1),multiline=False,background_normal="Knopka.png"
                            ,background_active="Knopka.png",hint_text_color=(0,0,0,1),on_text_validate=partial(self.proverka2, k) ))
                if self.click==10:
                    self.chet.append(0)
                    A=self.root.ids["igrok_screen"].ids["IGROKI"]
                    A.add_widget(TextInput(font_size=40,halign="center",valign="center",hint_text="Ондықтың атын енгізіңіз ",background_color=(255/255, 158/255, 128/255, 1),multiline=False,background_normal="Knopka.png"
                            ,background_active="Knopka.png",hint_text_color=(0,0,0,1),on_text_validate=partial(self.proverka2, k) ))
                
                if self.click>10:
                    z=0
                    self.vvedite_imya=self.root.ids["igrok_screen"].ids["igrokfloat"]
                    self.vvedite_imya.add_widget(ImageButton(source="kz/toomuch.png",size_hint=(.9,.9),pos_hint={"top":.95,"right":.95},allow_stretch=True,keep_ratio=False,
                                on_press=partial(self.Udalit_Vizov_Vvedite_Imya, z)))
        else:
            screen_manager=self.root.ids["screen_manager"]
            if screen_manager.current=="igrok_screen":
                self.click+=1
                k=0
                d=0
                
                if self.click==4:
                    self.chet.append(0)
                    A=self.root.ids["igrok_screen"].ids["IGROKI"]
                    A.add_widget(TextInput(font_size=40,halign="center",valign="center",hint_text="Введите имя 4-ого ",background_color=(255/255, 158/255, 128/255, 1),multiline=False,background_normal="Knopka.png"
                            ,background_active="Knopka.png",hint_text_color=(0,0,0,1),on_text_validate=partial(self.proverka2, k)))

                if self.click==5:
                    self.chet.append(0)
                    A=self.root.ids["igrok_screen"].ids["IGROKI"]
                    A.add_widget(TextInput(font_size=40,halign="center",valign="center",hint_text="Введите имя 5-ого ",background_color=(255/255, 158/255, 128/255, 1),multiline=False,background_normal="Knopka.png"
                            ,background_active="Knopka.png",hint_text_color=(0,0,0,1),on_text_validate=partial(self.proverka2, k) ))
                if self.click==6:
                    self.chet.append(0)
                    A=self.root.ids["igrok_screen"].ids["IGROKI"]
                    A.add_widget(TextInput(font_size=40,halign="center",valign="center",hint_text="Введите имя 6-ого",background_color=(255/255, 158/255, 128/255, 1),multiline=False,background_normal="Knopka.png"
                            ,background_active="Knopka.png",hint_text_color=(0,0,0,1),on_text_validate=partial(self.proverka2, k) ))
                if self.click==7:
                    self.chet.append(0)
                    A=self.root.ids["igrok_screen"].ids["IGROKI"]
                    A.add_widget(TextInput(font_size=40,halign="center",valign="center",hint_text="Введите имя 7-ого ",background_color=(255/255, 158/255, 128/255, 1),multiline=False,background_normal="Knopka.png"
                            ,background_active="Knopka.png",hint_text_color=(0,0,0,1),on_text_validate=partial(self.proverka2, k) ))
                if self.click==8:
                    self.chet.append(0)
                    A=self.root.ids["igrok_screen"].ids["IGROKI"]
                    A.add_widget(TextInput(font_size=40,halign="center",valign="center",hint_text="Введите имя 8-ого ",background_color=(255/255, 158/255, 128/255, 1),multiline=False,background_normal="Knopka.png"
                            ,background_active="Knopka.png",hint_text_color=(0,0,0,1),on_text_validate=partial(self.proverka2, k) ))
                if self.click==9:
                    self.chet.append(0)
                    A=self.root.ids["igrok_screen"].ids["IGROKI"]
                    A.add_widget(TextInput(font_size=40,halign="center",valign="center",hint_text="Введите имя 9-ого ",background_color=(255/255, 158/255, 128/255, 1),multiline=False,background_normal="Knopka.png"
                            ,background_active="Knopka.png",hint_text_color=(0,0,0,1),on_text_validate=partial(self.proverka2, k) ))
                if self.click==10:
                    self.chet.append(0)
                    A=self.root.ids["igrok_screen"].ids["IGROKI"]
                    A.add_widget(TextInput(font_size=40,halign="center",valign="center",hint_text="Введите имя 10-ого ",background_color=(255/255, 158/255, 128/255, 1),multiline=False,background_normal="Knopka.png"
                            ,background_active="Knopka.png",hint_text_color=(0,0,0,1),on_text_validate=partial(self.proverka2, k) ))
                
                if self.click>10 and self.tq<=3:
                    z=0
                    self.tq=self.tq+1
                    self.vvedite_imya=self.root.ids["igrok_screen"].ids["igrokfloat"]
                    self.vvedite_imya.add_widget(ImageButton(source="Vnimanie.png",size_hint=(.9,.9),pos_hint={"top":.95,"right":.95},allow_stretch=True,keep_ratio=False,
                                on_press=partial(self.Udalit_Vizov_Vvedite_Imya, z)))
                    self.click=10
                    
                if self.click>=10 and self.tq>=4:
                    tupp=0
                    self.vvedite_imya=self.root.ids["igrok_screen"].ids["igrokfloat"]
                    self.vvedite_imya.add_widget(ImageButton(source="idiot.png",size_hint=(.9,.9),pos_hint={"top":.95,"right":.95},allow_stretch=True,keep_ratio=False,
                                on_press=partial(self.Udalit_Vizov_Vvedite_Imya, tupp)))
                    self.click=10
                    idiot.volume=".4"
                    idiot.play()
        
    
    def inst1(self):
        webbrowser.open("https://www.instagram.com/rusyacapone/")
    def inst2(self):
        webbrowser.open("https://www.instagram.com/nexyeviy/")
    def pochta(self):
        webbrowser.open("mailto:LegerementStudio@gmail.com")
    def pravila(self):
        pass
    
    def proverka2(self,name,id):
        if self.kazak==True:
            if self.v==2:
                self.v+=1
            m=0
            pro=id
            for i in range (3):
                if len(self.imena)<=3:
                    Imya=self.root.ids["igrok_screen"].ids["igrok"+str(i+1)]
                    self.imena.append(Imya.text)
            self.igroki_4_10.append(id)
            self.imena.append(pro.text)
            
            if pro.text=="":
                self.vvedite_imya=self.root.ids["igrok_screen"].ids["igrokfloat"]
                self.vvedite_imya.add_widget(ImageButton(source="kz/insertname.png",size_hint=(.6,.6),pos_hint={"top":.8,"right":.8},
                            on_press=partial(self.Udalit_Vizov_Vvedite_Imya, m)))
            else:
                self.v+=1
        else:
            if self.v==2:
                self.v+=1
            m=0
            pro=id
            for i in range (3):
                if len(self.imena)<=3:
                    Imya=self.root.ids["igrok_screen"].ids["igrok"+str(i+1)]
                    self.imena.append(Imya.text)
            self.igroki_4_10.append(id)
            self.imena.append(pro.text)
            
            if pro.text=="":
                self.vvedite_imya=self.root.ids["igrok_screen"].ids["igrokfloat"]
                self.vvedite_imya.add_widget(ImageButton(source="IMYA.png",size_hint=(.6,.6),pos_hint={"top":.8,"right":.8},
                            on_press=partial(self.Udalit_Vizov_Vvedite_Imya, m)))
            else:
                self.v+=1
        
    def proverka3(self):
        m=0
        if self.v == self.click:
            app.change_screen("kategorii_screen")
        else:
            if self.click>3:
                self.vvedite_imya=self.root.ids["igrok_screen"].ids["igrokfloat"]
                self.vvedite_imya.add_widget(ImageButton(source="enter.png",size_hint=(.6,.6),pos_hint={"top":.8,"right":.8},
                                on_press=partial(self.Udalit_Vizov_Vvedite_Imya, m)))
        

    def proverka(self):
        if self.kazak==True:
            r=0
            l=0
            for i in  range(self.click):
                if self.click<=3:    
                    self.nomer+=1
                    Imya=self.root.ids["igrok_screen"].ids["igrok"+str(self.nomer)]
                    self.imena.append(Imya.text)
                    

                    if Imya.text=="":
                        
                        self.vvedite_imya=self.root.ids["igrok_screen"].ids["igrokfloat"]
                        self.vvedite_imya.add_widget(ImageButton(source="kz/insertname.png",size_hint=(.6,.6),pos_hint={"top":.8,"right":.8},allow_stretch=True,keep_ratio=False,
                            on_press=partial(self.Udalit_Vizov_Vvedite_Imya, l)))
                           
                        
                        break
                    else:
                        r+=1
            if r==3 and self.click==3:
                app.change_screen("kategorii_screen")   

                
            self.nomer=0 
        else:
            r=0
            l=0
            for i in  range(self.click):
                if self.click<=3:    
                    self.nomer+=1
                    Imya=self.root.ids["igrok_screen"].ids["igrok"+str(self.nomer)]
                    self.imena.append(Imya.text)
                    

                    if Imya.text=="":
                        
                        self.vvedite_imya=self.root.ids["igrok_screen"].ids["igrokfloat"]
                        self.vvedite_imya.add_widget(ImageButton(source="IMYA.png",size_hint=(.6,.6),pos_hint={"top":.8,"right":.8},allow_stretch=True,keep_ratio=False,
                            on_press=partial(self.Udalit_Vizov_Vvedite_Imya, l)))
                           
                        
                        break
                    else:
                        r+=1
            if r==3 and self.click==3:
                app.change_screen("kategorii_screen")   

                
            self.nomer=0 
    def Udalit_Vizov_Vvedite_Imya(self,img,widget_id):
        self.Udalit=widget_id

        self.maks=self.root.ids["igrok_screen"].ids["igrokfloat"]
        self.maks.remove_widget(self.Udalit)
    def Udalit_Vizov_Vvedite_Imya1(self,img,widget_id):
        self.Udalit1=widget_id

        self.vibo=self.root.ids["kategorii_screen"].ids["kategor_float"]
        self.vibo.remove_widget(self.Udalit1)
    def kat(self):
        l=0
        self.kategor=[]
        KatSkelet=self.root.ids["kategorii_screen"].ids["KatSkelet"]
        KatDobr=self.root.ids["kategorii_screen"].ids["KatDobr"]
        KatPol=self.root.ids["kategorii_screen"].ids["KatPol"]
        KatVec=self.root.ids["kategorii_screen"].ids["KatVec"]
        KatMor=self.root.ids["kategorii_screen"].ids["KatMor"]
        Kat18=self.root.ids["kategorii_screen"].ids["Kat18"]
        if KatSkelet.active==True:
            self.kategor.append("back/S.png")
        if KatDobr.active==True:
            self.kategor.append("back/D.png")
        if KatPol.active==True:
            self.kategor.append("back/P.png")
        if KatVec.active==True:
            self.kategor.append("back/V.png")
        if KatMor.active==True:
            self.kategor.append("back/M.png")
        if Kat18.active==True:
            self.kategor.append("back/18.png")
        if self.kategor==[] :
            if self.kazak==False:
                self.viberite_kategor=self.root.ids["kategorii_screen"].ids["kategor_float"]
                self.viberite_kategor.add_widget(ImageButton(source="k.png",size_hint=(.6,.6),pos_hint={"top":.8,"right":.8},
                    on_press=partial(self.Udalit_Vizov_Vvedite_Imya1, l)))
            else:
                self.viberite_kategor=self.root.ids["kategorii_screen"].ids["kategor_float"]
                self.viberite_kategor.add_widget(ImageButton(source="kz/choosekat.png",size_hint=(.6,.6),pos_hint={"top":.8,"right":.8},
                    on_press=partial(self.Udalit_Vizov_Vvedite_Imya1, l)))
        else:
             app.change_screen("vibor_screen")

        

        karta1=self.root.ids["vibor_screen"].ids["karta1"]
        karta2=self.root.ids["vibor_screen"].ids["karta2"]
        karta3=self.root.ids["vibor_screen"].ids["karta3"]
        if not self.kategor==[]:

            karta1.source=random.choice(self.kategor)
            karta2.source=random.choice(self.kategor)
            karta3.source=random.choice(self.kategor)
    def chetmin(self):

        self.resurs=self.root.ids["vopros_screen"].ids["chetchik"]
        if int(self.resurs.text)>0:
            self.rezultat=int(self.resurs.text) - 1
            self.resurs.text=str(self.rezultat)
        
    def chetplus(self):
        self.resurs=self.root.ids["vopros_screen"].ids["chetchik"]
        if int(self.resurs.text)<self.click:
            self.rezultat=int(self.resurs.text) + 1 
            self.resurs.text=str(self.rezultat)
    def za1(self):
        self.resurs=self.root.ids["vopros_screen"].ids["chetchik"]
        if self.resurs.text==str(1):
            self.otveti.append(1)
        else:
            self.otveti.append(self.rezultat)
        self.lol+=1
        self.za+=1
        self.kakoy+=1
        self.skolko1+=1
        self.skolko+=1
        
        self.resurs.text=str(1)
        
        if self.skolko1<=3:
           
            if self.skolko1==self.click:
                app.leader()
            if self.kakoy<4 and self.kazak==False:
                self.te=self.root.ids["igrok_screen"].ids["igrok"+str(self.kakoy)]
                self.hodila=self.root.ids["sled_screen"].ids["teper_hodit"]
                self.hodila.text="Теперь ходит" +"    "  +  "\n"+ "      " + self.te.text
                app.change_screen("sled_screen")  
            if self.kakoy<4 and self.kazak==True:
                self.te=self.root.ids["igrok_screen"].ids["igrok"+str(self.kakoy)]
                self.hodila=self.root.ids["sled_screen"].ids["teper_hodit"]
                self.hodila.text="Қазір серуендейді" +"    "  +  "\n"+ "      " + self.te.text
                app.change_screen("sled_screen")  
        
        if self.click<=10 and self.click>3 and self.skolko>3 and self.kazak==False:
            if self.skolko-1==self.click:
                app.leader()
            else:
                self.hodila=self.root.ids["sled_screen"].ids["teper_hodit"]
                self.hodila.text="Теперь ходит" +"    " + "\n"+ "      " + self.igroki_4_10[self.lol].text
                app.change_screen("sled_screen")
        if self.click<=10 and self.click>3 and self.skolko>3 and self.kazak==True:
            if self.skolko-1==self.click:
                app.leader()
            else:
                self.hodila=self.root.ids["sled_screen"].ids["teper_hodit"]
                self.hodila.text="Қазір серуендейді" +"    " + "\n"+ "      " + self.igroki_4_10[self.lol].text
                app.change_screen("sled_screen")
    def leader(self):
        
        if self.kazak==False:
            d=0
            z=0
            app.change_screen("leader_screen")
            self.rezultat=self.root.ids["leader_screen"].ids["skolkoza"]
            self.rezultat.text="Ответов ЗА:" +"   " + str(self.za)
            for i in self.otveti:
                
                if i==self.za:
                    k=self.chet[d]
                    self.chet.pop(d)
                    self.chet.insert(d,k+2)
                if i+1==self.za or i-1==self.za:
                    k=self.chet[d]
                    self.chet.pop(d)
                    self.chet.insert(d,k+1)
                d+=1
            for j in self.chet:

                if self.chet[z]==22 or self.chet[z]>22:
                    app.change_screen("final_screen")
                    app.priz()
                    victor=self.root.ids["final_screen"].ids["pobeda"]
                    victor.text=self.imena[z] 
                z+=1
            self.board=self.root.ids["leader_screen"].ids["leaderboard"]
            
            for i in range(self.click):
                imeno=Label(text=str(self.imena[i]),font_size=50,bold=True,color=[0,0,0,1])
                kek=Label(text=str(self.chet[i]),font_size=50,bold=True,color=[0,0,0,1])
                self.board.add_widget(imeno)
                self.board.add_widget(kek)
        if self.kazak==True:
            d=0
            z=0
            app.change_screen("leader_screen")
            self.rezultat=self.root.ids["leader_screen"].ids["skolkoza"]
            self.rezultat.text="Жауаптар үшін:" +"   " + str(self.za)
            for i in self.otveti:
                
                if i==self.za:
                    k=self.chet[d]
                    self.chet.pop(d)
                    self.chet.insert(d,k+2)
                if i+1==self.za or i-1==self.za:
                    k=self.chet[d]
                    self.chet.pop(d)
                    self.chet.insert(d,k+1)
                d+=1
            for j in self.chet:

                if self.chet[z]==22 or self.chet[z]>22:
                    app.change_screen("final_screen")
                    app.priz()
                    victor=self.root.ids["final_screen"].ids["pobeda"]
                    victor.text=self.imena[z] +" "+"!"
                z+=1
            self.board=self.root.ids["leader_screen"].ids["leaderboard"]
            
            for i in range(self.click):
                imeno=Label(text=str(self.imena[i]),font_size=50,bold=True,color=[0,0,0,1])
                kek=Label(text=str(self.chet[i]),font_size=50,bold=True,color=[0,0,0,1])
                self.board.add_widget(imeno)
                self.board.add_widget(kek)
            
        
            
        

    def protiv1(self):
        self.resurs=self.root.ids["vopros_screen"].ids["chetchik"]
        if self.resurs.text==str(1):
            self.otveti.append(1)
        else:
            self.otveti.append(self.rezultat)
        
        self.lol+=1
        self.protiv+=1
        self.kakoy+=1
        self.skolko1+=1
        self.skolko+=1
        
        self.resurs.text=str(1)
        if self.skolko1<=3:
           
            if self.skolko1==self.click:
                app.leader()
            if self.kakoy<4 and self.kazak==False:
                self.te=self.root.ids["igrok_screen"].ids["igrok"+str(self.kakoy)]
                self.hodila=self.root.ids["sled_screen"].ids["teper_hodit"]
                self.hodila.text="Теперь ходит" +"    " + "\n"+ "      " +  self.te.text
                app.change_screen("sled_screen")  
            if self.kakoy<4 and self.kazak==True:
                self.te=self.root.ids["igrok_screen"].ids["igrok"+str(self.kakoy)]
                self.hodila=self.root.ids["sled_screen"].ids["teper_hodit"]
                self.hodila.text="Қазір серуендейді" +"    " + "\n"+ "      " +  self.te.text
                app.change_screen("sled_screen")
        if self.click<=10 and self.click>3 and self.skolko>3 and self.kazak==False:
            if self.skolko-1==self.click:
                app.leader()
            else:
                self.hodila=self.root.ids["sled_screen"].ids["teper_hodit"]
                self.hodila.text="Теперь ходит" +"    " + "\n"+ "      " + self.igroki_4_10[self.lol].text
                app.change_screen("sled_screen")
        if self.click<=10 and self.click>3 and self.skolko>3 and self.kazak==True:
            if self.skolko-1==self.click:
                app.leader()
            else:
                self.hodila=self.root.ids["sled_screen"].ids["teper_hodit"]
                self.hodila.text="Қазір серуендейді" +"    " + "\n"+ "      " + self.igroki_4_10[self.lol].text
                app.change_screen("sled_screen")
    def nextquestion(self):
        self.board=self.root.ids["leader_screen"].ids["leaderboard"]
        self.board.clear_widgets()
        self.skolko1=0
        self.za=0
        self.protiv=0
        self.lol=-3
        self.skolko=1
        self.kakoy=1
        self.otveti.clear()
        
        self.rezultat=1
        karta1=self.root.ids["vibor_screen"].ids["karta1"]
        karta2=self.root.ids["vibor_screen"].ids["karta2"]
        karta3=self.root.ids["vibor_screen"].ids["karta3"]
        karta1.source=random.choice(self.kategor)
        karta2.source=random.choice(self.kategor)
        karta3.source=random.choice(self.kategor)
        app.change_screen("vibor_screen")
    def vopros1(self):
        
       
        karta1=self.root.ids["vibor_screen"].ids["karta1"]
       
        vopros=self.root.ids["vopros_screen"].ids["vopros"]
        if self.kazak==False:
            if karta1.source=="back/S.png":
                files = os.listdir("Vopros/S")
                index = random.randrange(0, len(files))
                vopros.source="Vopros/S" + "/" + files[index]
               
            if karta1.source=="back/D.png":
                files = os.listdir("Vopros/D")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/D" + "/" + files[index]
                
            if karta1.source=="back/M.png":
                files = os.listdir("Vopros/M")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/M" + "/" + files[index]
                
            if karta1.source=="back/P.png":
                files = os.listdir("Vopros/P")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/P" + "/" + files[index]
                
            if karta1.source=="back/V.png":
                files = os.listdir("Vopros/V")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/V" + "/" + files[index]
                
            if karta1.source=="back/18.png":
                files = os.listdir("Vopros/I")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/I" + "/" + files[index]
            app.change_screen("vopros_screen")
        else:
            if karta1.source=="back/S.png":
                files = os.listdir("kz/Vopros/S")
                index = random.randrange(0, len(files))
                vopros.source="kz/Vopros/S" + "/" + files[index]
               
            if karta1.source=="back/D.png":
                files = os.listdir("kz/Vopros/D")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/D" + "/" + files[index]
                
            if karta1.source=="back/M.png":
                files = os.listdir("kz/Vopros/M")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/M" + "/" + files[index]
                
            if karta1.source=="back/P.png":
                files = os.listdir("kz/Vopros/P")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/P" + "/" + files[index]
                
            if karta1.source=="back/V.png":
                files = os.listdir("kz/Vopros/V")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/V" + "/" + files[index]
                
            if karta1.source=="back/18.png":
                files = os.listdir("kz/Vopros/I")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/I" + "/" + files[index]
            app.change_screen("vopros_screen")
        
    def vopros2(self):       
        karta2=self.root.ids["vibor_screen"].ids["karta2"]                
        vopros=self.root.ids["vopros_screen"].ids["vopros"]
        if self.kazak==False:
            if karta2.source=="back/S.png":
                files = os.listdir("Vopros/S")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/S" + "/" + files[index]
                
            if karta2.source=="back/D.png":
                files = os.listdir("Vopros/D")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/D" + "/" + files[index]
                
            if karta2.source=="back/M.png":
                files = os.listdir("Vopros/M")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/M" + "/" + files[index]
               
            if karta2.source=="back/P.png":
                files = os.listdir("Vopros/P")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/P" + "/" + files[index]
                
            if karta2.source=="back/V.png":
                files = os.listdir("Vopros/V")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/V" + "/" + files[index]
                
            if karta2.source=="back/18.png":
                files = os.listdir("Vopros/I")
                index = random.randrange(0, len(files))
                vopros.source="Vopros/I" + "/" + files[index]
            app.change_screen("vopros_screen")
        else:
            if karta2.source=="back/S.png":
                files = os.listdir("kz/Vopros/S")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/S" + "/" + files[index]
                
            if karta2.source=="back/D.png":
                files = os.listdir("kz/Vopros/D")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/D" + "/" + files[index]
                
            if karta2.source=="back/M.png":
                files = os.listdir("kz/Vopros/M")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/M" + "/" + files[index]
               
            if karta2.source=="back/P.png":
                files = os.listdir("kz/Vopros/P")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/P" + "/" + files[index]
                
            if karta2.source=="back/V.png":
                files = os.listdir("kz/Vopros/V")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/V" + "/" + files[index]
                
            if karta2.source=="back/18.png":
                files = os.listdir("kz/Vopros/I")
                index = random.randrange(0, len(files))
                vopros.source="kz/Vopros/I" + "/" + files[index]
            app.change_screen("vopros_screen")
    def vopros3(self):       
        karta3=self.root.ids["vibor_screen"].ids["karta3"]                
        vopros=self.root.ids["vopros_screen"].ids["vopros"]
        if self.kazak==False:
            if karta3.source=="back/S.png":
                files = os.listdir("Vopros/S")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/S" + "/" + files[index]
                
            if karta3.source=="back/D.png":
                files = os.listdir("Vopros/D")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/D" + "/" + files[index]
                
            if karta3.source=="back/M.png":
                files = os.listdir("Vopros/M")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/M" + "/" + files[index]
                
            if karta3.source=="back/P.png":
                files = os.listdir("Vopros/P")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/P" + "/" + files[index]
                
            if karta3.source=="back/V.png":
                files = os.listdir("Vopros/V")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/V" + "/" + files[index]
                
            if karta3.source=="back/18.png":
                files = os.listdir("Vopros/I")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/I" + "/" + files[index]
            app.change_screen("vopros_screen")
        else:
            if karta3.source=="back/S.png":
                files = os.listdir("kz/Vopros/S")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/S" + "/" + files[index]
            
            if karta3.source=="back/D.png":
                files = os.listdir("kz/Vopros/D")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/D" + "/" + files[index]
                
            if karta3.source=="back/M.png":
                files = os.listdir("kz/Vopros/M")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/M" + "/" + files[index]
                
            if karta3.source=="back/P.png":
                files = os.listdir("kz/Vopros/P")
                index = random.randrange(0, len(files))
                
                vopros.source="Vopros/P" + "/" + files[index]
                
            if karta3.source=="back/V.png":
                files = os.listdir("kz/Vopros/V")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/V" + "/" + files[index]
                
            if karta3.source=="back/18.png":
                files = os.listdir("kz/Vopros/I")
                index = random.randrange(0, len(files))
                
                vopros.source="kz/Vopros/I" + "/" + files[index]
            app.change_screen("vopros_screen")

app = MainApp()
import bugs
bugs.fixBugs()
app.run()
