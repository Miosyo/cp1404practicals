"""
Dynamic labels app
Estimated Time: 10 minutes
Actual Time: 10 minutes
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.uix.label import Label


class SquareNumberApp(App):
    """Dynamically create labels from a list of names."""

    def __init__(self, **kwargs):
        """Initialise the array of names."""
        super().__init__(**kwargs)
        self.names = ["James", "Johnson", "Jerry", "Jacob", "Job"]

    def build(self):
        """ build the Kivy app from the kv file """
        Window.size = (400, 200)
        self.title = "Dynamic Labels"
        self.root = Builder.load_file('dynamic_labels.kv')
        self.create_widgets()
        return self.root

    def create_widgets(self):
        """Create labels from a list of names."""
        for name in self.names:
            temp_label = Label(text=name)
            self.root.ids.main.add_widget(temp_label)


SquareNumberApp().run()
