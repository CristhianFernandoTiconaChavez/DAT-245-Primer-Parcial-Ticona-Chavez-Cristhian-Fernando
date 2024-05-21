from kanren import Relation, facts, run, conde, var

padre = Relation()
madre = Relation()
abuelo = Relation()
abuela = Relation()

facts(padre, ('Carlos', 'Guillermo'),
              ('Carlos', 'Martha'),
              ('Carlos', 'Rosmery'),
              ('Carlos', 'Roxana'),
              ('Guillermo', 'Felipe'),
              ('Rolando', 'Uriel'),
              ('Rolando', 'Mayte'),
              ('Rolando', 'Valentina'),
              ('Daniel', 'Cristhian'),
              ('Daniel', 'Luna'),
              ('Daniel', 'Celeste'),
              ('Daniel', 'Gabriel'),
              ('Daniel', 'Jasiel'),
              ('Armando', 'Marco'),
              ('Armando', 'Gael'),
              ('Armando', 'Juan'))

facts(madre, ('Estefania', 'Guillermo'),
              ('Estefania', 'Martha'),
              ('Estefania', 'Rosmery'),
              ('Estefania', 'Roxana'),
              ('Betty', 'Felipe'),
              ('Martha', 'Uriel'),
              ('Martha', 'Mayte'),
              ('Martha', 'Valentina'),
              ('Rosmery', 'Cristhian'),
              ('Rosmery', 'Luna'),
              ('Rosmery', 'Celeste'),
              ('Rosmery', 'Gabriel'),
              ('Rosmery', 'Jasiel'),
              ('Roxana', 'Marco'),
              ('Roxana', 'Gael'),
              ('Roxana', 'Juan'))

facts(abuelo, ('Carlos', 'Felipe'),
              ('Carlos', 'Uriel'),
              ('Carlos', 'Mayte'),
              ('Carlos', 'Valentina'),
              ('Carlos', 'Cristhian'),
              ('Carlos', 'Luna'),
              ('Carlos', 'Celeste'),
              ('Carlos', 'Gabriel'),
              ('Carlos', 'Jasiel'),
              ('Carlos', 'Marco'),
              ('Carlos', 'Gael'),
              ('Carlos', 'Juan'))

facts(abuela, ('Estefania', 'Felipe'),
               ('Estefania', 'Uriel'),
               ('Estefania', 'Mayte'),
               ('Estefania', 'Valentina'),
               ('Estefania', 'Cristhian'),
               ('Estefania', 'Luna'),
               ('Estefania', 'Celeste'),
               ('Estefania', 'Gabriel'),
               ('Estefania', 'Jasiel'),
               ('Estefania', 'Marco'),
               ('Estefania', 'Gael'),
               ('Estefania', 'Juan'))

def abuelo(x, z):
    y = var()
    return conde((padre(x, y), padre(y, z)),
                 (madre(x, y), padre(y, z)),
                 (padre(x, y), madre(y, z)),
                 (madre(x, y), madre(y, z)))

def tio(x, z):
    y, y2 = var(), var()
    return conde(
        (padre(y, x), padre(y2, z), (padre(y, y2) or madre(y, y2))),
        (madre(y, x), madre(y2, z), (padre(y, y2) or madre(y, y2))),
        (padre(y, x), madre(y2, z), (padre(y, y2) or madre(y, y2))),
        (madre(y, x), padre(y2, z), (padre(y, y2) or madre(y, y2)))
    )



def primo(x, z):
    y1, y2, y3, y4 = var(), var(), var(), var()
    return conde(
        (padre(y1, x), padre(y2, z), (padre(y3, y1) or madre(y3, y1)), (padre(y4, y2) or madre(y4, y2))),
        (madre(y1, x), padre(y2, z), (padre(y3, y1) or madre(y3, y1)), (padre(y4, y2) or madre(y4, y2))),
        (padre(y1, x), madre(y2, z), (padre(y3, y1) or madre(y3, y1)), (padre(y4, y2) or madre(y4, y2))),
        (madre(y1, x), madre(y2, z), (padre(y3, y1) or madre(y3, y1)), (padre(y4, y2) or madre(y4, y2))),

        (padre(y1, x), padre(y2, z), (padre(y3, y1) or madre(y3, y1)), padre(y4, y2)),
        (padre(y1, x), padre(y2, z), (padre(y3, y1) or madre(y3, y1)), madre(y4, y2)),
        (madre(y1, x), padre(y2, z), (padre(y3, y1) or madre(y3, y1)), padre(y4, y2)),
        (madre(y1, x), padre(y2, z), (padre(y3, y1) or madre(y3, y1)), madre(y4, y2)),

        (padre(y1, x), madre(y2, z), (padre(y3, y1) or madre(y3, y1)), padre(y4, y2)),
        (padre(y1, x), madre(y2, z), (padre(y3, y1) or madre(y3, y1)), madre(y4, y2)),
        (madre(y1, x), madre(y2, z), (padre(y3, y1) or madre(y3, y1)), padre(y4, y2)),
        (madre(y1, x), madre(y2, z), (padre(y3, y1) or madre(y3, y1)), madre(y4, y2))
    )


x = var()
print("Abuelos de Celeste:")
print(run(0, x, abuelo(x, "Celeste")))
print("Abuelos de Marco")
print(run(0, x, abuelo(x, "Marco")))

print("Tíos de Felipe:")
print(run(0, x, tio(x, "Felipe")))

print("Primos de Marco:")
print(run(0, x, primo(x, "Marco")))
