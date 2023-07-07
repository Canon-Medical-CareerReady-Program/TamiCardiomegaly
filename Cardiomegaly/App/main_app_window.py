from numbers import Rational
from App.main_app_window_base import MainAppWindowBase
from Core import algorithm
from Core.core_types import Point

class MainAppWindow(MainAppWindowBase):


    def __init__(self, tk_root):
        super().__init__(tk_root)
        
        # Init variables
        self.start_point = None

    def getGeneralColor(self):
        """ Returns the color of the general measurement """
        return "yellow"
    def getHeartColor(self):
        """ Returns the color of the heart measurement """
        return "red"
    
    def getThoraxColor(self):
        """ Returns the color of the thorax measurement """
        return "#FF00FF"
    
    def getshadowcolor(self):
        return "#FF00FF"
    
    def on_mouse_click(self, event):
        """ Called when the user clicks or starts a drag on the canvas """
        self.start_point = Point(event.x, event.y)

    def on_mouse_drag(self, event):   
        """ Called continuously while the user is dragging the mouse on the canvas """
        if self.start_point:     
            self.update_current_line(self.start_point, Point(event.x, event.y), label=f"({event.x}, {event.y})")

    def on_mouse_release(self, event):
        """ Called when the user releases the mouse on the canvas """
        if self.start_point and self.current_line:
            line_length = algorithm.distance(self.start_point.x, self.start_point.y, event.x, event.y)
            self.update_current_measurement(line_length)
            print(f"Line length: {line_length}")
            # Rest the start point so that we can start a new line
            self.start_point = None
            # Detach the current line variable so that it continues to exist
            self.current_line = None

    def save_measurement(self):
        """ Called when the user clicks the save button """
        print("TODO: Save the measurement")
        print_text = " The heart measurement is " + str(self.last_full_measurement_heart_val) + " The thorax measurement is " + str(self.last_full_measurement_thorax_val)

        print(print_text)
        
        text =  "cardiomegaly ratio = " + str(self.last_full_measurement_heart_val / self.last_full_measurement_thorax_val ) + print_text
        file_path = "output.txt"  # Specify the file path and name

        with open(file_path, "w") as file:
            file .write(text)
        print("Text saved to", file_path)
        

    
from PIL import Image