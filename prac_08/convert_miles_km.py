"""

"""

from kivy.app import App
from kivy.lang import Builder
from kivy.core.window import Window
from kivy.properties import StringProperty


class ConvertMilesKm(App):
    """Convert miles to km app."""
    MILES_TO_KM_FACTOR = 1.60934
    conversion_result = StringProperty()

    def build(self):
        """build the Kivy app from the kv file."""
        Window.size = (800, 400)
        self.title = "Convert Miles to Kilometres"
        self.root = Builder.load_file('convert_miles_km.kv')
        return self.root

    def handle_conversion(self):
        try:
            miles = float(self.root.ids.text_input.text)
            self.conversion_result = str(miles * self.MILES_TO_KM_FACTOR)
        except ValueError:
            self.conversion_result = '0.0'

    def handle_increment(self, amount):
        input_field_text = self.root.ids.text_input.text
        try:
            input_field_number = float(input_field_text)
            input_field_number += amount
        except ValueError:
            # Set value to a valid number
            input_field_number = amount
        self.root.ids.text_input.text = str(input_field_number)



ConvertMilesKm().run()
