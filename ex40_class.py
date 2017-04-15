# final class preview

class Song(object):

    def __init__(self, lyrics):
        self.lyrics = lyrics

    def sing_a_song(self):
        for line in self.lyrics:
            print(line)

la_la_la = Song(["¡Hola!", """
La la la la la
La la la la la
La la la la la
La la la la la

¡Adentro!
(Leggo, leggo, leggo, leggo)

Toda mi vida fue así
tanto te busqué hasta que llegaste
con esa boca que Dios te ha dao'
Ni obliga' podría dejarte
Las ganas de ti me devoran
los segundos de todas las horas
Tus dos lucero son to' lo que quiero
Sin tus ojos azules me muero.

Ven y besame mucho el mundo no importa
la noche comienza, no, no, no pares ahora

La la la la la
La la la la la
La la la la la
La la la la la
Porque yo siempre te llevo
La la la la la
La la la la la
La la la la la
La la la la la
¡Adentro!""", """ Leggo, Leggo)"""])


hips_dont_lie = Song(["""Yo no sabia que ella bailaba así
aquella noche io me enloquecí
cómo se llama, bonita, mi casa, su casa

Tú sabes que palabaras hay
para hacerme suspirar
mantente atento
ya va llegando el momento

Será, será que lo que un dia fue
es porque fue para hacerce hoy
si sientes, yo siento
mira asi baby, asi es perfecto """, "can't stop the feeling in my body!"])


la_la_la.sing_a_song()
hips_dont_lie.sing_a_song()
