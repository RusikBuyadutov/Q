from kivy.app import App
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
from kivy.uix.screenmanager import ShaderTransition
from kivy.uix.screenmanager import FadeTransition
from kivy.uix.screenmanager import FallOutTransition
from kivy.uix.screenmanager import RiseInTransition
from kivy.uix.textinput import TextInput
from kivy.graphics import Color
from  kivy.uix.popup import Popup
from  kivy.uix.label import Label
from kivy.uix.screenmanager import WipeTransition
from kivy.core.audio import SoundLoader
from kivy.uix.checkbox import CheckBox
from kivy.graphics import Line
from functools import partial
from  kivy.uix.gridlayout import GridLayout
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
class Igrok(Screen):
    pass
class Pravila2(Screen):
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
GUI=Builder.load_file("Main.kv")    
class MainApp(App):
    global sound_menu
    global igroki_4_10
    global prizz
    prizz=SoundLoader.load("п.wav")

    sound_menu=SoundLoader.load("ZVUK.wav")
    def build(self): 
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
        return GUI
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
        if  zvuk_knopka.source=="VonON.png":
           
            sound_menu.volume=".1"
            sound_menu.play()
            sound_menu.loop=True
        if zvuk_knopka.source=="VolOFF.png":
            sound_menu.stop()
    def change_screen(self,screen_name):
        screen_manager=self.root.ids["screen_manager"]
        if screen_manager.current == "menu_screen":screen_manager.transition=RiseInTransition()
        if screen_manager.current == "pravila_screen":screen_manager.transition=WipeTransition()
        else:screen_manager.transition=FallOutTransition()     
        screen_manager.current=screen_name
    
        pass
    def add_player(self):
        self.click+=1
        k=0
        d=0
        if self.click==4:
            self.chet.append(0)
            A=self.root.ids["igrok_screen"].ids["IGROKI"]
            A.add_widget(TextInput(font_size=20,halign="center",valign="center",hint_text="Введите имя 4-ого ",background_color=(24/255, 255/255, 255/255, 1),multiline=False,background_normal="C:\\Users\\--\\Desktop\\ПРИЛОЖЕНИЕ\\Knopka.png"
                    ,background_active="Knopka.png",hint_text_color=(1,1,1,1),on_text_validate=partial(self.proverka2, k)))

        if self.click==5:
            self.chet.append(0)
            A=self.root.ids["igrok_screen"].ids["IGROKI"]
            A.add_widget(TextInput(font_size=20,halign="center",valign="center",hint_text="Введите имя 5-ого ",background_color=(255/255, 111/255, 0/255, 1),multiline=False,background_normal="C:\\Users\\--\\Desktop\\ПРИЛОЖЕНИЕ\\Knopka.png"
                    ,background_active="Knopka.png",hint_text_color=(1,1,1,1),on_text_validate=partial(self.proverka2, k) ))
        if self.click==6:
            self.chet.append(0)
            A=self.root.ids["igrok_screen"].ids["IGROKI"]
            A.add_widget(TextInput(font_size=20,halign="center",valign="center",hint_text="Введите имя 6-ого",background_color=(255/255, 64/255, 129/255, 1),multiline=False,background_normal="C:\\Users\\--\\Desktop\\ПРИЛОЖЕНИЕ\\Knopka.png"
                    ,background_active="Knopka.png",hint_text_color=(1,1,1,1),on_text_validate=partial(self.proverka2, k) ))
        if self.click==7:
            self.chet.append(0)
            A=self.root.ids["igrok_screen"].ids["IGROKI"]
            A.add_widget(TextInput(font_size=20,halign="center",valign="center",hint_text="Введите имя 7-ого ",background_color=(255/255, 255/255, 0/255, 1),multiline=False,background_normal="C:\\Users\\--\\Desktop\\ПРИЛОЖЕНИЕ\\Knopka.png"
                    ,background_active="Knopka.png",hint_text_color=(0,0,0,.6),on_text_validate=partial(self.proverka2, k) ))
        if self.click==8:
            self.chet.append(0)
            A=self.root.ids["igrok_screen"].ids["IGROKI"]
            A.add_widget(TextInput(font_size=20,halign="center",valign="center",hint_text="Введите имя 8-ого ",background_color=(124/255, 67/255, 189/255, 1),multiline=False,background_normal="C:\\Users\\--\\Desktop\\ПРИЛОЖЕНИЕ\\Knopka.png"
                    ,background_active="Knopka.png",hint_text_color=(1,1,1,1),on_text_validate=partial(self.proverka2, k) ))
        if self.click==9:
            self.chet.append(0)
            A=self.root.ids["igrok_screen"].ids["IGROKI"]
            A.add_widget(TextInput(font_size=20,halign="center",valign="center",hint_text="Введите имя 9-ого ",background_color=(164/255, 164/255, 164/255, 1),multiline=False,background_normal="C:\\Users\\--\\Desktop\\ПРИЛОЖЕНИЕ\\Knopka.png"
                    ,background_active="Knopka.png",hint_text_color=(1,1,1,1),on_text_validate=partial(self.proverka2, k) ))
        if self.click==10:
            self.chet.append(0)
            A=self.root.ids["igrok_screen"].ids["IGROKI"]
            A.add_widget(TextInput(font_size=20,halign="center",valign="center",hint_text="Введите имя 10-ого ",background_color=(93/255, 64/255, 55/255, 1),multiline=False,background_normal="C:\\Users\\--\\Desktop\\ПРИЛОЖЕНИЕ\\Knopka.png"
                    ,background_active="Knopka.png",hint_text_color=(1,1,1,1),on_text_validate=partial(self.proverka2, k) ))
        
        if self.click>10:
            z=0
            self.vvedite_imya=self.root.ids["igrok_screen"].ids["igrokfloat"]
            self.vvedite_imya.add_widget(ImageButton(source="Vnimanie.png",size_hint=(1,1),pos_hint={"top":1,"right":1},
                        on_press=partial(self.Udalit_Vizov_Vvedite_Imya, z)))
    
    
    def pravila(self):
        pass
    
    def proverka2(self,name,id):
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
            self.vvedite_imya.add_widget(ImageButton(source="IMYA.png",size_hint=(1,1),pos_hint={"top":1,"right":1},
                        on_press=partial(self.Udalit_Vizov_Vvedite_Imya, m)))
        else:
            self.v+=1
        
    def proverka3(self):
        if self.v == self.click:
            app.change_screen("kategorii_screen")
        

    def proverka(self):
        r=0
        l=0
        for i in  range(self.click):
            if self.click<=3:    
                self.nomer+=1
                Imya=self.root.ids["igrok_screen"].ids["igrok"+str(self.nomer)]
                self.imena.append(Imya.text)
                

                if Imya.text=="":
                    
                    self.vvedite_imya=self.root.ids["igrok_screen"].ids["igrokfloat"]
                    self.vvedite_imya.add_widget(ImageButton(source="IMYA.png",size_hint=(1,1),pos_hint={"top":1,"right":1},
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
            self.kategor.append("Сзади\\S.png")
        if KatDobr.active==True:
            self.kategor.append("Сзади\\D.png")
        if KatPol.active==True:
            self.kategor.append("Сзади\\P.png")
        if KatVec.active==True:
            self.kategor.append("Сзади\\V.png")
        if KatMor.active==True:
            self.kategor.append("Сзади\\M.png")
        if Kat18.active==True:
            self.kategor.append("Сзади\\18.png")
        if self.kategor==[]:
            self.viberite_kategor=self.root.ids["kategorii_screen"].ids["kategor_float"]
            self.viberite_kategor.add_widget(ImageButton(source="k.png",size_hint=(1,1),pos_hint={"top":1,"right":1},
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
            if self.kakoy<4:
                self.te=self.root.ids["igrok_screen"].ids["igrok"+str(self.kakoy)]
                self.hodila=self.root.ids["sled_screen"].ids["teper_hodit"]
                self.hodila.text="Теперь ходит" +"    "  +  "\n"+ "      " + self.te.text
                app.change_screen("sled_screen")  
        
        if self.click<=10 and self.click>3 and self.skolko>3:
            if self.skolko-1==self.click:
                app.leader()
            else:
                self.hodila=self.root.ids["sled_screen"].ids["teper_hodit"]
                self.hodila.text="Теперь ходит" +"    " + "\n"+ "      " + self.igroki_4_10[self.lol].text
                app.change_screen("sled_screen")
    def leader(self):
        
        
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
                victor.text=self.imena[z] +" "+"!"
            z+=1
        self.board=self.root.ids["leader_screen"].ids["leaderboard"]
        
        for i in range(self.click):
            imeno=Label(text=str(self.imena[i]),font_size=20,bold=True,color=[0,0,0,1])
            kek=Label(text=str(self.chet[i]),font_size=20,bold=True,color=[0,0,0,1])
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
            if self.kakoy<4:
                self.te=self.root.ids["igrok_screen"].ids["igrok"+str(self.kakoy)]
                self.hodila=self.root.ids["sled_screen"].ids["teper_hodit"]
                self.hodila.text="Теперь ходит" +"    " + "\n"+ "      " +  self.te.text
                app.change_screen("sled_screen")  
        
        if self.click<=10 and self.click>3 and self.skolko>3:
            if self.skolko-1==self.click:
                app.leader()
            else:
                self.hodila=self.root.ids["sled_screen"].ids["teper_hodit"]
                self.hodila.text="Теперь ходит" +"    " + "\n"+ "      " + self.igroki_4_10[self.lol].text
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
       
        if karta1.source=="Сзади\\S.png":
            files = os.listdir("Вопросы\\Скелет")
            index = random.randrange(0, len(files))
            vopros.source="Вопросы\\Скелет" + "\\" + files[index]
           
        if karta1.source=="Сзади\\D.png":
            files = os.listdir("..\\Вопросы\\Добрые")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\Добрые" + "\\" + files[index]
            
        if karta1.source=="Сзади\\M.png":
            files = os.listdir("Вопросы\\Мораль")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\Мораль" + "\\" + files[index]
            
        if karta1.source=="Сзади\\P.png":
            files = os.listdir("Вопросы\\Политика")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\Политика" + "\\" + files[index]
            
        if karta1.source=="..\\Сзади\\V.png":
            files = os.listdir("Вопросы\\Вечеринка")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\Вечеринка" + "\\" + files[index]
            
        if karta1.source=="Сзади\\18.png":
            files = os.listdir("Вопросы\\18")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\18" + "\\" + files[index]
        app.change_screen("vopros_screen")
        
        
    def vopros2(self):       
        karta2=self.root.ids["vibor_screen"].ids["karta2"]                
        vopros=self.root.ids["vopros_screen"].ids["vopros"]
        if karta2.source=="Сзади\\S.png":
            files = os.listdir("..\\Вопросы\\Скелет")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\Скелет" + "\\" + files[index]
            
        if karta2.source=="Сзади\\D.png":
            files = os.listdir("Вопросы\\Добрые")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\Добрые" + "\\" + files[index]
            
        if karta2.source=="Сзади\\M.png":
            files = os.listdir("Вопросы\\Мораль")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\Мораль" + "\\" + files[index]
           
        if karta2.source=="Сзади\\P.png":
            files = os.listdir("Вопросы\\Политика")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\Политика" + "\\" + files[index]
            
        if karta2.source=="Сзади\\V.png":
            files = os.listdir("Вопросы\\Вечеринка")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\Вечеринка" + "\\" + files[index]
            
        if karta2.source=="Сзади\\18.png":
            files = os.listdir("Вопросы\\18")
            index = random.randrange(0, len(files))
            vopros.source="Вопросы\\18" + "\\" + files[index]
        app.change_screen("vopros_screen")
    def vopros3(self):       
        karta3=self.root.ids["vibor_screen"].ids["karta3"]                
        vopros=self.root.ids["vopros_screen"].ids["vopros"]
        if karta3.source=="Сзади\\S.png":
            files = os.listdir("Вопросы\\Скелет")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\Скелет" + "\\" + files[index]
            
        if karta3.source=="Сзади\\D.png":
            files = os.listdir("Вопросы\\Добрые")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\Добрые" + "\\" + files[index]
            
        if karta3.source=="Сзади\\M.png":
            files = os.listdir("Вопросы\\Мораль")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\Мораль" + "\\" + files[index]
            
        if karta3.source=="Сзади\\P.png":
            files = os.listdir("Вопросы\\Политика")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\Политика" + "\\" + files[index]
            
        if karta3.source=="Сзади\\V.png":
            files = os.listdir("Вопросы\\Вечеринка")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\Вечеринка" + "\\" + files[index]
            
        if karta3.source=="Сзади\\18.png":
            files = os.listdir("Вопросы\\18")
            index = random.randrange(0, len(files))
            
            vopros.source="Вопросы\\18" + "\\" + files[index]
        app.change_screen("vopros_screen")

app = MainApp()
app.run()