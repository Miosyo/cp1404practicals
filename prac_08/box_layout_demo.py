"""
Box layout demo
"""

from kivy.app import App
from kivy.lang import Builder


class BoxLayoutDemo(App):
    """Box layout demo."""
    def build(self):
        """Build the ui from a kv file."""
        self.title = "Box Layout Demo"
        self.root = Builder.load_file('box_layout.kv')
        return self.root

    def handle_clear(self):
        """Clear the input and output labels."""
        self.root.ids.output_label.text = ''
        self.root.ids.input_name.text = ''

    def handle_greet(self):
        """Set the output label text"""
        self.root.ids.output_label.text = f"Hello {self.root.ids.input_name.text}"


BoxLayoutDemo().run()
