class YouTubeChannel:
    def __init__(self, name):
        self.name = name
        self.subscribers = []
        self.videos = []
    
    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)
    
    def unsubscribe(self, subscriber):
        self.subscribers.remove(subscriber)
    
    def upload_video(self, video_title):
        self.videos.append(video_title)
        self._notify_subscribers(video_title)
    
    def _notify_subscribers(self, video_title):
        for subscriber in self.subscribers:
            subscriber.update(self.name, video_title)

class Subscriber:
    def __init__(self, name):
        self.name = name
    
    def update(self, channel_name, video_title):
        print(f"{self.name}: Новое видео на канале '{channel_name}' - '{video_title}'")

# Использование
# Создаем канал
channel = YouTubeChannel("TechReviews")

# Создаем подписчиков
alice = Subscriber("Алиса")
bob = Subscriber("Боб")
charlie = Subscriber("Чарли")

# Подписываемся
channel.subscribe(alice)
channel.subscribe(bob)
channel.subscribe(charlie)

# Загружаем видео
print("Канал загружает видео:")
channel.upload_video("Обзор нового iPhone")

# Отписываемся
channel.unsubscribe(bob)

print("\nБоб отписался, загружаем еще видео:")
channel.upload_video("Лучшие ноутбуки 2024")