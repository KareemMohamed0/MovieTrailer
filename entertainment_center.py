# fresh tomatoes module
from fresh_tomatoes import open_movies_page
import media

""" root file that push all movies to open movie page function """

# Movies list

attacImage = '''https://wallpaperscraft.com/image/attack_on_titan_eren_
jaeger_shingeki_no_kyojin_104200_240x320.jpg'''

attackOnTitan = media.Movie('Attack on titan',
                            'Eu velit reprehenderit veniam',
                            attacImage,
                            'https://www.youtube.com/watch?v=DpEfsDmMyF4')

narutoImage = '''https://wallpaperscraft.com/image/naruto_naruto_shippuden
_sasuke_uchiha_112104_1024x768.jpg'''

naruto = media.Movie('Naruto',
                     'Qui et deserunt non adipisicing irure irure.',
                     narutoImage,
                     'https://www.youtube.com/watch?v=rEYhAKi-j6Y')


deathImage = '''https://wallpaperscraft.com/image/death_note_yagami_light_kira_l
_lawliet_amane_misa_shinigami_death_god_103304_1280x720.jpg'''
deathNote = media.Movie('Death note',
                        'Magna Lorem dolor deserunt laboris consequat',
                        deathImage,
                        'https://www.youtube.com/watch?v=tJZtOrm-WPk')

allMovies = [attackOnTitan, naruto, deathNote]
open_movies_page(allMovies)
