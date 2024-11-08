import hashlib
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = self.hashed_password(password)
        self.age = age

    def hashed_password(self, password):
        return hashlib.sha256(password.encode()).hexdigest()

    def __eq__(self, other):
        return self.nickname == other.nickname

    def __str__(self):
        return f'{self.nickname}'

class Video:

    def __init__(self, title, duration, time_now = 0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __eq__(self, other):
        return self.title.lower() == other.title.lower()

    def __str__(self):
        return f"Video(title='{self.title}', duration= '{self.duration}', adult_mode= '{self.adult_mode}')"

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        for user in self.users:
            if user.nickname == nickname and user.password == hashed_password:
                self.current_user = user
                print(f'Пользователь {nickname} вошел в систему')
                return True
            else:
                print ('Ошибка входа: неверный логин или пароль')
                return False

    def register(self, nickname, password, age):
        new_user = User(nickname, password, age)
        if new_user in self.users:
            print(f'Пользователь {nickname} уже существует')
        else:
            self.users.append(new_user)
            self.current_user = new_user

    def log_out(self):
        if self.current_user:
            self.current_user = None


    def add(self, *videos):
        for video in videos:
            if video not in self.videos:
                self.videos.append(video)

    def get_video(self, search_word):
        search_word_lower = search_word.lower()
        return [video.title for video in self.videos if search_word_lower in video.title.lower()]

    def watch_video(self, title):
        if not self.current_user:
            print('Войдите в систему, чтобы просмотреть видео')
            return

        for video in self.videos:
            if video.title == title:
                if video.adult_mode and self.current_user.age < 18:
                    print('вам нет 18 лет, пожалуйста, покиньте страницу')
                    return
                else:
                    for second in range(video.time_now + 1, video.duration + 1):
                        print(second, end = '', flush = True)
                        time.sleep(1)
                    print('Конец видео')
                    video.time_now = 0
                    return


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1,v2)

print(ur.get_video('Лучший'))
print(ur.get_video('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin','lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')