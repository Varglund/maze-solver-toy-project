from tkinter import Tk, BOTH, Canvas

class Window():
    def __init__(self, width:int, height:int):
        self.__width = width
        self.__height = height
        self.__root = Tk()
        self.__root.title = "root_widget"
        self.__canvas = Canvas(self.__root, bg="white", width=self.__width, height=self.__height)
        # pack the canvas so that it is ready to draw
        self.__canvas.pack(fill=BOTH, expand=1)
        # create a data member to represent that the window is "running" and set it to False
        self.__running = False
        self.__root.protocol("WM_DELETE_WINDOW", self.close)

    def redraw(self)->None:
        self.__root.update_idletasks()
        self.__root.update()

    def wait_for_close(self)->None:
        self.__running = True
        while self.__running:
            self.redraw()

    def close(self)->None:
        self.__running = False
