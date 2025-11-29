import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    win.set_title("Change Your System Volume in a Jiffy!")
    win.set_default_size(400, 300)
    
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=10)
    box.set_margin_start(20)
    box.set_margin_end(20)
    box.set_margin_top(20)
    box.set_margin_bottom(20)
    
    h_box = Gtk.Box(orientation=Gtk.Orientation.HORIZONTAL, spacing=10)

    label = Gtk.Label(label="Volume")
    label.set_xalign(0)

    slider = Gtk.Scale.new_with_range(Gtk.Orientation.HORIZONTAL, 0, 100, 1)
    slider.set_size_request(200, -1)
    slider.set_value(0)
    slider.set_draw_value(True)

    h_box.append(label)
    h_box.append(slider)

    box.append(h_box)
    box.append(label)
    
    win.set_child(box)
    win.present()

def on_switch_toggled(switch, state):
    if state:
        print("i guess this is just the easter egg")
    else:
        print("nevermind")
    return False
app = Gtk.Application(application_id='org.gtk.Example')
app.connect('activate', on_activate)
app.run(None)
