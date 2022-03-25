import sys
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.image import Image
from kivy.uix.gridlayout import GridLayout
from matplotlib.widgets import Widget
from mylib.ImageScan import ImageScan

# TODO: GUIに作成や捜査等に関するライブラリの作成を行うと後々開発が楽になりそう
# 可変長引数を受け取ってまとめてlayoutに要素を追加する様な関数が欲しい
class HelloWorldApp(App):
    
    def getDupulicatedImagePathList(self, dirpath):
        iScan = ImageScan()
        return iScan.ScanImageGrayScale(dirpath)
    
    def build(self):
        args = sys.argv
        
        if len(args) == 1:
            sys.exit("prease args filepath")
        
        dirpath = args[1]
        
        filelist = self.getDupulicatedImagePathList(dirpath)
        wimgs = []
        
        for file in filelist:
            wimgs.append(Image(source = file))
        
        return Util.BuildGridLayout(2, wimgs)

class TextInputWidget(Widget):
    textinput = TextInput()
    button = Button(text = "submit")

class Util:
    @classmethod
    def BuildBoxLayout(cls, option, *widgetList):
        layout = BoxLayout(orientation = option)
        for widgets in widgetList:
            for widget in widgets:
                layout.add_widget(widget)
                
        return layout
    
    @classmethod
    def BuildGridLayout(cls, colsnum, *widgetList):
        layout = GridLayout(cols = colsnum)
        for widgets in widgetList:
            for widget in widgets:
                layout.add_widget(widget)
            
        return layout

if __name__ == '__main__':
    HelloWorldApp().run()