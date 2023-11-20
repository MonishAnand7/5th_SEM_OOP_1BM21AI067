class Songs:
    def __init__(self, lyrics):
        self.lyrics = lyrics

    def SingMeASong(self):
        for line in self.lyrics:
            print(line)

HappyBday = Songs([
    "May God Bless You,",
    "Have a sunshine on you,",
    "Happy Birthday to You."
])

HappyBday.SingMeASong()
