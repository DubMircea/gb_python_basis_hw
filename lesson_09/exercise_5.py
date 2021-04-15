class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print('«Запуск отрисовки»')


class Pen(Stationery):
    def __init__(self, *args):
        super(Pen, self).__init__(*args)

    def draw(self):
        print(f'«Запуск отрисовки» {self.title}')


class Pencil(Stationery):
    def __init__(self, *args):
        super(Pencil, self).__init__(*args)

    def draw(self):
        print(f'«Запуск отрисовки» {self.title}')


class Handle(Stationery):
    def __init__(self, *args):
        super(Handle, self).__init__(*args)

    def draw(self):
        print(f'«Запуск отрисовки» {self.title}')


st = Stationery('Stationery')
st.draw()

pen = Pen('pen')
pen.draw()

pencil = Pencil('pencil')
pencil.draw()

handle = Handle('handle')
handle.draw()
