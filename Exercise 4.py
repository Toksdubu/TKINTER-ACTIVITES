import tkinter as tk
def draw_shape(event):
    x = event.x
    y = event.y

    if current_shape == 'square':
        size = 50  
        if current_fill == 'filled':
            canvas.create_rectangle(x, y, x + size, y + size, fill=current_color)
        else:
            canvas.create_rectangle(x, y, x + size, y + size, outline=current_color)
    elif current_shape == 'circle':
        radius = 25  
        if current_fill == 'filled':
            canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill=current_color)
        else:
            canvas.create_oval(x - radius, y - radius, x + radius, y + radius, outline=current_color)
def handle_key(event):
    global current_shape, current_color, current_fill

    key = event.char.lower()

    if key == 's':
        current_shape = 'square'
    elif key == 'c':
        current_shape = 'circle'
    elif key == 'f':
        current_fill = 'filled'
    elif key == 'u':
        current_fill = 'unfilled'
    elif key == 'y':
        current_color = 'yellow'
    elif key == 'r':
        current_color = 'red'
    

root = tk.Tk()
root.title("Drawing Shapes")

current_shape = 'square'
current_color = 'red'
current_fill = 'filled'

canvas = tk.Canvas(root, width=400, height=400, bg='blue')
canvas.pack()


canvas.bind('<Button-1>', draw_shape)
root.bind('<KeyPress>', handle_key)

menu_bar = tk.Menu(root)
root.config(menu=menu_bar)

# Create a "Shapes" menu
shapes_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Shapes", menu=shapes_menu)

# Add shape options to the "Shapes" menu
shapes_menu.add_command(label="Square", command=lambda: set_shape('square'))
shapes_menu.add_command(label="Circle", command=lambda: set_shape('circle'))

# Create a "Fill" menu
fill_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Fill", menu=fill_menu)

# Add fill options to the "Fill" menu
fill_menu.add_command(label="Filled", command=lambda: set_fill('filled'))
fill_menu.add_command(label="Unfilled", command=lambda: set_fill('unfilled'))

# Create a "Color" menu
color_menu = tk.Menu(menu_bar, tearoff=False)
menu_bar.add_cascade(label="Color", menu=color_menu)

# Add color options to the "Color" menu
color_menu.add_command(label="Yellow", command=lambda: set_color('yellow'))
color_menu.add_command(label="Red", command=lambda: set_color('red'))

def set_shape(shape):
    global current_shape
    current_shape = shape

def set_fill(fill):
    global current_fill
    current_fill = fill

def set_color(color):
    global current_color
    current_color = color



root.mainloop()