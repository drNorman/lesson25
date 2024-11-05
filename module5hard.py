from time import sleep


class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.h_password = hash(password)
        self.age = age

    def __str__(self):
        return self.nickname


class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    users = []
    videos = []
    current_user = None

    def __contains__(self, item):
        return item in self.current_user

    def log_in(self, nickname, password):
        for i in self.users:
            if nickname == i.nickname:
                if hash(password) == i.h_password:
                    self.current_user = i

    def register(self, nickname, password, age):
        for i in self.users:
            if nickname == i.nickname:
                print(f"Пользователь {nickname} уже существует")
                break
        else:
            self.users.append(User(nickname, password, age))
            self.log_in(nickname, password)

    def log_out(self):
        self.current_user = None

    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_videos(self, search_word):
        lower_search_word = search_word.lower()
        found_video = []
        for video in self.videos:
            if lower_search_word in video.title.lower():
                found_video.append(video.title)
        return found_video

    def watch_video(self, title):
        if self.current_user:
            for video in self.videos:
                if title == video.title:
                    if video.adult_mode:
                        if self.current_user.age >= 18:
                            for i in range(1, video.duration + 1):
                                print(i, end=' ')
                                sleep(1)
                            print("Конец видео")
                        else:
                            print("Вам нет 18 лет, пожалуйста покиньте страницу")
                    else:
                        for i in range(1, video.duration + 1):
                            print(i, end=' ')
                            sleep(1)
                        print("Конец видео")

        else:
            print("Войдите в аккаунт, чтобы смотреть видео")


if __name__ == '__main__':
    ur = UrTube()
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

    # Добавление видео
    ur.add(v1, v2)

    # Проверка поиска
    print(ur.get_videos('лучший'))
    print(ur.get_videos('ПРОГ'))

    # Проверка на вход пользователя и возрастное ограничение
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('vasya_pupkin', 'lolkekcheburek', 13)
    ur.watch_video('Для чего девушкам парень программист?')
    ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
    ur.watch_video('Для чего девушкам парень программист?')

    # Проверка входа в другой аккаунт
    ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
    print(ur.current_user)

    # Попытка воспроизведения несуществующего видео
    ur.watch_video('Лучший язык программирования 2024 года!')
