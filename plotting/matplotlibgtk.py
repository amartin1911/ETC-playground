# https://matplotlib.org/gallery/user_interfaces/embedding_in_gtk3_sgskip.html
# Though a FigureCanvasGTK3Agg is used, the default renderer is still TkAgg
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

import matplotlib as mpl
mpl.use('GTK3Agg')
print(mpl.rcParams['backend'])
from matplotlib.backends.backend_gtk3agg import (
    FigureCanvasGTK3Agg as FigureCanvas)
from matplotlib.figure import Figure
import numpy as np

win = Gtk.Window()
win.connect("delete-event", Gtk.main_quit)
win.set_default_size(400, 300)
win.set_title("Embedding in GTK")

f = Figure(figsize=(5, 4), dpi=100)
a = f.add_subplot(111)
t = np.arange(0.0, 3.0, 0.01)
s = np.sin(2*np.pi*t)
a.plot(t, s)

sw = Gtk.ScrolledWindow()
win.add(sw)
# A scrolled window border goes outside the scrollbars and viewport
sw.set_border_width(10)

canvas = FigureCanvas(f)  # a Gtk.DrawingArea
canvas.set_size_request(800, 600)
# win.add(canvas)
sw.add_with_viewport(canvas)

win.show_all()
Gtk.main()
