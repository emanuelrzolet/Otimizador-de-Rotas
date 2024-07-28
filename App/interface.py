from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
    def build(self):
        self.input = TextInput(hint_text='Digite algo')
        self.label = Label(text='Saída:')
        layout = BoxLayout(orientation='vertical')
        layout.add_widget(self.input)
        layout.add_widget(self.label)
        self.input.bind(on_text_validate=self.on_enter)
        return layout

    def on_enter(self, instance):
        self.label.text = f'Saída: {self.input.text}'

if __name__ == '__main__':
    MyApp().run()
