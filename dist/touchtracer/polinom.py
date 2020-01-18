
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.config import Config
from kivy.uix.widget import Widget
from kivy.graphics import (Color, Ellipse, Rectangle, Line)
import re


Config.set('graphics', 'resizable', 0)
Config.set('graphics', 'width', 480)
Config.set('graphics', 'height', 360)

from kivy.core.window import Window
Window.clearcolor = (1, 1, 1, 1)

class PainterWidget(Widget):
    def __init__(self, **kwargs):
        super(PainterWidget, self).__init__(**kwargs)
        
        with self.canvas:
            Color(0,1,0,1)
            Ellipse(pos = (100,100), size = (50,50)) #Элипс по позиции и с размером


class Polinom(App):
    polinom1 = []
    polinom2 = []
    polinom3 = []
    polinom4 = []

    def build(self):
            
        bl = BoxLayout(orientation = 'vertical', padding = 20, spacing = 20)
        blb = BoxLayout(spacing = 10, size_hint = (1,.1))

        self.lbl1 = TextInput(text = 'Введите полином в формате ( x^2+3x^3+(-5x^4)+x^8 )', font_size = 14, size_hint = (1,.2), background_color = [.85,.85,.85,1])
        self.lbl2 = TextInput(text = 'Введите полином в формате ( x^2+3x^3+(-5x^4)+x^8 )', font_size = 14, size_hint = (1,.2), background_color = [.85,.85,.85,1])
        self.lbl = Label(text = 'Результат: ', font_size = 16, size_hint = (1,.2), text_size = (480-40, 60), halign = 'left', valign = 'top', color = [0,0,0,1])

        blb.add_widget(Button(text = '+', on_press = self.start, background_color = [.78,.36,.05,1], background_normal = '' ))
        blb.add_widget(Button(text = '-', on_press = self.start, background_color = [.78,.36,.05,1], background_normal = ''))
        blb.add_widget(Button(text = '*', on_press = self.start, background_color = [.78,.36,.05,1], background_normal = ''))
        blb.add_widget(Button(text = '/', on_press = self.start, background_color = [.78,.36,.05,1], background_normal = ''))
        blb.add_widget(Button(text = 'CLS', on_press = self.cl, background_color = [.78,.36,.05,1], background_normal = ''))

        bl.add_widget(self.lbl1)
        bl.add_widget(self.lbl2)
        bl.add_widget(self.lbl)
        bl.add_widget(blb)
        
        return bl
    
    def cl(self, instance):
         self.lbl.text = 'Результат: '
         self.lbl1.text = 'Введите полином: '
         self.lbl2.text = 'Введите полином: '
         self.polinom3 = []
         self.polinom4 = []
         self.polinom1 = []
         self.polinom2 = []


    def start(self, instance):
        self.flag1 = False
        self.flag2 = False
        self.a, self.b = '', ''
        self.char = '0123456789()^+-x'
        for i in self.lbl1.text.strip():
            if i in self.char:
                self.flag1 = True
            else:
                self.flag1 = False
                self.lbl1.text = 'Неверный ввод'
                break

        for i in self.lbl2.text.strip():
            if i in self.char:
                self.flag2 = True
            else:
                self.flag2 = False
                self.lbl2.text = 'Неверный ввод'
                break
        
        if self.flag1 and self.flag2:
            self.a, self.b = self.lbl1.text.strip(), self.lbl2.text.strip()
            self.polinom3 = re.split(r'[+()]+', self.a)
            self.polinom4 = re.split(r'[+()]+', self.b)
        else:
            self.a, self.b = '', ''
        self.polinomCreate()
        self.polinomAdd()

        if instance.text == '+':
            self.summa()
        
        if instance.text == '-':
            self.sub()

        if instance.text == '*':
            self.mul()

        if instance.text == '/':
            self.div()

    
    def Input(self, polinom):
        self.string = ''
        for i in range(len(polinom)):
            if polinom[i] == 0:
                continue
            elif polinom[i] == 1:
                self.string += '(' + 'x^' + str(i)+ ')' + ' + '
            elif polinom[i] == -1:
                self.string += '(' + '-x^' + str(i)+ ')' + ' + '
            else:
                self.string += '(' + str(round(polinom[i],2)) + 'x^' + str(i)+ ')' + ' + '
        self.lbl.text = 'Результат: ' + self.string[0:len(self.string)-3:1]
        

    def polinomCreate(self):
        for i in range(100):
            self.polinom1.append(0)
        for i in range(100):
            self.polinom2.append(0)
    

    def polinomAdd(self):
        for i in range(len(self.polinom3)):
            x = re.findall(r'\d+$', self.polinom3[i])
            if (x == []):
                x = ['1']
            x = int(x.pop())
            if re.split(r'x', self.polinom3[i])[0] == '':
                self.polinom1[x] = 1
            elif re.split(r'x', self.polinom3[i])[0] == '-':
                self.polinom1[x] = -1
            else:
                self.polinom1[x] = int(re.split(r'x', self.polinom3[i])[0])
            
        for i in range(len(self.polinom4)):
            x = re.findall(r'\d+$', self.polinom4[i])
            if (x == []):
                x = ['1']
            x = int(x.pop())
            if re.split(r'x', self.polinom4[i])[0] == '':
                self.polinom2[x] = 1
            elif re.split(r'x', self.polinom4[i])[0] == '-':
                self.polinom2[x] = -1
            else:
                self.polinom2[x] = int(re.split(r'x', self.polinom4[i])[0])
        

    def summa(self):
        self.a = self.polinom1
        self.b = self.polinom2

        self.string = []
        for i in range(len(self.a)):
            self.string.append(self.a[i]+self.b[i]) 

        self.Input(self.string)
    

    def sub(self):
        self.a = self.polinom1
        self.b = self.polinom2

        self.string = []
        for i in range(len(self.a)):
            self.string.append(self.a[i]-self.b[i]) 

        self.Input(self.string) 
    
    
    def mul(self):
        self.a = self.polinom1
        self.b = self.polinom2

        self.string = [0 for i in range(len(self.a) + len(self.b))]
        for i in range(len(self.a)):
            for j in range(len(self.b)):
                x = self.a[i] * self.b[j]
                k = i + j
                self.string[k] = self.string[k] + x

        self.Input(self.string)
    

    def div(self): # первый больше степени второго, можно делить
        self.d = []
        self.a = self.polinom1
        self.b = self.polinom2
        self.summa1 = []
        self.y = 0
        self.x = 0
    #_____________________________________________________
    
        while self.x >= self.y:
            for i in range(len(self.a)):
                if self.a[i] != 0:
                    self.x = i
                    self.n = self.a[i]
            for i in range(len(self.b)):
                if self.b[i] != 0:
                    self.y = i
                    self.k = self.b[i]
            if self.x < self.y:
                break
        #__________________________________________________
        
            self.c = [0 for i in range(abs(self.x-self.y))]

            if (self.n < 0 and self.k < 0) or (self.n > 0 and self.k > 0):
                self.c.append(self.n/self.k)
            else:
                self.c.append(self.n/self.k)
        
            self.mull = [0 for i in range(len(self.c) + len(self.b))] # Умножение 
            for i in range(len(self.c)):
                for j in range(len(self.b)):
                    z = self.c[i] * self.b[j]
                    k = i + j
                    self.mull[k] = self.mull[k] + z
        #_________________________________________________
                
            if len(self.a) > len(self.mull): #a - mul
                k = len(self.a) - len(self.mull)
                for i in range(k):
                    self.mull.append(0)
            else:
                k = len(self.mull) - len(self.a)
                for i in range(k):
                    self.a.append(0)
        
            self.string = []      
            for i in range(len(self.a)):
                self.string.append(self.a[i]-self.mull[i])

            if len(self.string) == self.string.count(0):
                if len(self.d) > len(self.c): #a - mul
                    k = len(self.d) - len(self.c)
                    for i in range(k):
                        self.c.append(0)
                else:
                    k = len(self.c) - len(self.d)
                    for i in range(k):
                        self.d.append(0)

                for i in range(len(self.d)):
                    self.d[i] += self.c[i]

                self.Input(self.d)
                break
            
            else:
                self.a = self.string
        #__________________________________________________
                
                if len(self.d) > len(self.c): #a - mul
                    k = len(self.d) - len(self.c)
                    for i in range(k):
                        self.c.append(0)
                else:
                    k = len(self.c) - len(self.d)
                    for i in range(k):
                        self.d.append(0)

                for i in range(len(self.d)):
                    self.d[i] += self.c[i]
        #__________________________________________________
                    
        self.Input(self.d)

    
if __name__ == '__main__':
    Polinom().run()
