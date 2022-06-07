import pygame


class Settings:
    def __init__(self):
        self._screen_res = (1280, 720)
        self._fps = 60

    def get_res(self):
        return self._screen_res

    def get_fps(self):
        return self._fps


settings = Settings()
