# fresh tomatoes module
from fresh_tomatoes import open_movies_page
import media
# Movies list
attackOnTitan = media.Movie(
'Attack on titan',
'Eu velit reprehenderit veniam ipsum consequat nulla officia do.',
'https://wallpaperscraft.com/image/attack_on_titan_eren_jaeger_shingeki_no_kyojin_104200_240x320.jpg',
'https://www.youtube.com/watch?v=DpEfsDmMyF4'
)
naruto = media.Movie(
'Naruto',
'Qui et deserunt non adipisicing irure irure.',
'https://wallpaperscraft.com/image/naruto_naruto_shippuden_sasuke_uchiha_112104_1024x768.jpg',
'https://www.youtube.com/watch?v=rEYhAKi-j6Y'
)
deathNote = media.Movie(
'Death note',
'Magna Lorem dolor deserunt laboris consequat laborum.',
'https://wallpaperscraft.com/image/death_note_yagami_light_kira_l_lawliet_amane_misa_shinigami_death_god_103304_1280x720.jpg',
'https://www.youtube.com/watch?v=tJZtOrm-WPk'
)

allMovies = [attackOnTitan, naruto , deathNote]
open_movies_page(allMovies)