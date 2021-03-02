class HashMap:

    # Definisco la hash MAP come un dizionario con associazione key : list
    def __init__(self, m):
        self.map = {}
        self.lenght = int(m)
        self.collisions = 0
        for i in range(m):
            self.map.update({i: []})

    # Calcolo tramite il metodo delle divisioni
    def division_method(self, key):
        return key % self.lenght

    def chain_insert(self, value):
        key = self.division_method(value)
        if self.map[key]:
            self.collisions += 1
        self.map[key].insert(0, value)

    def chain_delete(self, value):
        key = self.division_method(value)
        self.map[key].remove(value)

    def chain_search(self, value):
        key = self.division_method(value)
        i = 0
        for i in self.map[key]:
            if i == value:
                return 'è presente'
        return 'NON è presente'

    # METODI PER OPEN ADDRESSING
    # Ispezione lineare che richiama semplicemente il metodo delle divisioni
    def linear_probing(self, i):
        return self.division_method(i)
    # Inserimento
    def op_insert(self, value):
        i = 0
        while i != self.lenght:
            key = self.linear_probing(value + i)

            if self.map[key] == [] or self.map[key] == ['DELETED']:
                if self.map[key] == ['DELETED']:
                    self.map[key].clear()

                self.map[key].append(value)
                break
            else:
                i += 1
                self.collisions += 1

        if i == self.lenght:
            print(f'Valore: {value}, non può essere inserito per Overflow')

    # Rimozione Element (DELETED)
    def op_remove(self, value):
        i = 0
        while i != self.lenght:
            key = self.linear_probing(value + i)

            if self.map[key] == [value]:
                self.map[key].pop()
                self.map[key].append('DELETED')
                break
            else:
                i += 1

        if self.map[key] != [value] and i == self.lenght:
            print(f'{value} non presente nella Tabella')

    def op_search(self, value):
        i = 0
        while i != self.lenght:
            key = self.linear_probing(value + i)

            if self.map[key] == [value]:
                print(f'Elemento {value}, è Presente')
                break
            else:
                i += 1
        if self.map[key] != [value] and i == self.lenght:
            print(f'{value} non presente nella Tabella')

    # Ritorna il numero di collisioni totali
    def collision_checker(self):
        return self.collisions

    def print_table(self):
        for i in self.map.values():
            print(i)
