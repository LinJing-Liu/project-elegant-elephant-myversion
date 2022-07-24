class HobbyItem:
    def __init__(self, title, id, text, images):
        self.title = title
        self.id = id
        self.text = text
        self.images = images

hobby_text = 'My hobbies span a few areas, but overall, I am a quite indoor person. I like to read, watch movies and anime, listen to music (more on that in the music section), solve soduku puzzles and watch shows online (of course). I am also a foodie. I always have a genuine interest and curiosity for food that I have not tried before.'
music_text = 'My music taste changes quite a bit over years as well. Generally, I listen to pop music in both Chinese and English, and whatever kind of music I find online. In addition, I also really like kpop and track music from movies, shows and anime.'
travel_text = 'One memorable trip I had a few years ago is to the Niagara Falls. I will recommend it to anyone who is not boat-sick. The view is quite beautiful, as shown in the image below (from Creative Commons sadly).'

hobby_links = [
    'https://live.staticflickr.com/3919/14797066783_5d3cb41dc3_b.jpg',
    'https://live.staticflickr.com/5347/9703904811_082e58ec89_b.jpg',
    'https://live.staticflickr.com/5508/9703869609_37a8cd7e76_b.jpg'
]
music_links = [
    'https://live.staticflickr.com/6149/6199438609_14a5bcf91f_b.jpg',
    'https://upload.wikimedia.org/wikipedia/commons/1/15/Where_stray_kids_stay.jpg',
    'https://live.staticflickr.com/4074/5447199165_875c48f367_b.jpg'
]
travel_links = [
    'https://live.staticflickr.com/3761/9546866777_9719652eba_b.jpg',
    'https://live.staticflickr.com/7449/9550288456_0d9d62eb5f_b.jpg',
    'https://live.staticflickr.com/3176/2879148209_b10de83cc4_b.jpg'
]

hobby_info = [
    HobbyItem('Hobbies', 'food-carousel', hobby_text, hobby_links),
    HobbyItem('Music Taste', 'music-carousel', music_text, music_links),
    HobbyItem('Map of Travel', 'travel-carousel', travel_text, travel_links)
]