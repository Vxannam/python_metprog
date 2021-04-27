import time

class CarData: # класс для автомабиля
    fio: str
    model: str
    date: int
    number: str
    color: str

    def __init__(self, line: str): # инициализируется класс и заполнябтся поля
        fio, model, date, number, color = line.split(' | ')
        self.fio = fio
        self.model = model
        self.date = int(date)
        self.number = number
        self.color = color

    def __gt__(self, other): # перегрузка оператора сравнения '>'
        if self.fio > other:
            return True
        else:
            return False

    def __lt__(self, other):  # перегрузка оператора сравнения '<'
        if self.fio < other.fio:
            return True
        elif self.fio == other.fio:
            if self.date < other.date:
                return True
            elif self.date == other.date:
                if self.model < other.model:
                    return True
                elif self.model == other.model:
                    if self.color < other.color:
                        return True
                    elif self.color == other.color:
                        if self.number < other.number:
                            return True
                        else:
                            return False
                    else:
                        return False
                else:
                    return False
            else:
                return False
        else:
            return False

    def __eq__(self, other):  # перегрузка оператора сравнения '=='
        if self.fio == other:
            return True
        else:
            return False

class MultiMap:
    tree = None

    def __init__(self):
        self.tree = Tree()

    def insert(self, key, obj):
        self.tree.insert_tree(key, obj)

    def find(self, key):
        return self.tree.search(key)

class Node(object):
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.left = []
        self.right = []

class Tree(object):
    def __init__(self):
        self.root = []

    def search(self, key):
        v = self.root
        while v:
            if v[0].key == key:
                time.sleep(0.01)
                return v
            elif key < v[0].key:
                v = v[0].left
            else:  # x > v.key:
                v = v[0].right
        time.sleep(0.01)
        return []

    def insert_tree(self, key, val):
        flag = 0
        parent = None
        if self.root:
            v = self.root
            if v[0].key == key:
                 flag = 1
        else:
            v = None
        while v and flag != 1:
            parent = v
            if isinstance(v, list):
                v = v[0]
            if key < v.key:
                v = v.left
            elif key > v.key:
                v = v.right
            else:
                flag = 2
                break

        w = Node(key, val)

        if parent is None or flag == 1:
            self.root.append(w)
        elif flag == 2:
            parent.append(w)
        elif key < parent[0].key:
            parent[0].left.append(w)
        elif key > parent[0].key:
            parent[0].right.append(w)