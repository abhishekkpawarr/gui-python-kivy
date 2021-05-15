from kivy.app import App
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.widget import Widget


class WidgetsExample(GridLayout):
    count = 0
    count_enabled = BooleanProperty(False)
    # slider_value_txt = StringProperty("50")
    text_input_str = StringProperty("text")

    my_text = StringProperty(str(count))

    def on_button_click(self):
        print("Button Clicked!")
        if(self.count_enabled):
            self.count += 1
        self.my_text = str(self.count)

    def on_toggle_button(self, toggle_widget):
        print("toggle state: " + toggle_widget.state)
        if(toggle_widget.state=="normal"):
            toggle_widget.text = "OFF"
            self.count_enabled=False
        else:
            toggle_widget.text = "ON"
            self.count_enabled=True

    def on_switch_active(self, switch_active):
        print("Switch: " + str(switch_active.active))

    # def on_slider_value(self, slider_value):
        # print("Slider: " + str(int(slider_value.value)))
        # self.slider_value_txt = str(int(slider_value.value))
        # print(self.slider_value_txt)

    def on_text_validate(self, text_widget):
        self.text_input_str = text_widget.text


class BoxLayoutExample(BoxLayout):
    pass
    """
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        b1 = Button(text="A")
        b2 = Button(text="B")
        self.add_widget(b1)
        self.add_widget(b2)
    """


class MainWidget(Widget):
    pass


class App(App):
    pass


App().run()
