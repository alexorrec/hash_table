# Vogliamo capire qual è il comportamento delle tabelle hash al crescere del fattore di caricamento α=n/m.
# Per fare questo scriveremo:
# Un programma che implementa le tabelle hash con gestione delle collisioni basate su concatenamento
# e su indirizzamento aperto (ispezione lineare).
# La funzione hash deve essere calcolata col metodo delle divisioni.
# Oltre al costruttore devono essere implementati inserimento,cancellazione e ricerca per i due metodi

# Un programma che conta quante collisioni si hanno eseguendo un numero variabile di inserimenti in una tabella hash
# Un programma che esegue gli esperimenti

# Alessandro Cerro  7012851  23/02

# PROGRAMMA DI TEST
#
#   TODO: come scelgo M?
#   TODO: scelta del valore da cercare

import hash_table as h
import random

# CONCATENAMENTO
m = 11

insert_lst = []
for i in range(m):
    n = random.randrange(0, 60)
    insert_lst.append(n)
print(f'La lista da inserire: {insert_lst}')
delete_list = random.sample(insert_lst, 4)
print(f'I valori da rimuovere: {delete_list}')

print('')
# Inserimento
print('C O N C A T E N A M E N T O')

T = h.HashMap(m)
for i in insert_lst:
    T.chain_insert(i)
T.print_table()
print('')
print(f'Il numero di collisioni avvenute nell\'inserimento è: {T.collision_checker()}')
x = insert_lst[random.randint(0, m)]
print(f'Il valore {x}, {T.chain_search(x)}')
print('Inizio rimozione...')

delete_list = random.sample(insert_lst, 4)
print(f'I valori da rimuovere: {delete_list}')
for i in delete_list:
    T.chain_delete(i)
T.print_table()
print('')
# OPEN ADDRESSING
print('O P E N  A D R E S S I N G')

B = h.HashMap(m)
for i in insert_lst:
    B.op_insert(i)
B.print_table()

print(f'Il numero di collisioni avvenute nell\'inserimento è: {B.collision_checker()}')
B.op_search(100)
print('Inizio rimozione...')

for i in delete_list:
    B.op_remove(i)
B.print_table()


