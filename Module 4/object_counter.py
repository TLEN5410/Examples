class Widget():
    counter = 0
    pouch = list()

    def __init__(self):
        Widget.counter += 1
        self.pouch.append('stuff')

widget1 = Widget()
widget2 = Widget()
widget3 = Widget()

print widget1.counter, widget2.counter, widget3.counter
print widget1.pouch, widget2.pouch
