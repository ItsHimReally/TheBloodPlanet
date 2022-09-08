"""
Файл с основной структурой редактора, импортировать во всех рабочих python-файлах проекта
"""

# импорты основных библиотек
from abc import ABC
import logging
import pygame

# настройка логов
logging.basicConfig(filename="GameLogs.log", level=logging.INFO)

'''
Набор базовых классов редактора для более простой и удобной работы с модулем pygame
'''


class Vector2:
    def __init__(self, vec_x=0, vec_y=0):
        self.x = vec_x
        self.y = vec_y


class Transform:
    def __init__(self, tr_position=Vector2(), tr_scale=Vector2(), tr_rotate=0):
        self.position = tr_position
        self.scale = tr_scale
        self.rotation = tr_rotate

    '''
    Метод перемещения объекта

    :param shift_x: смещение по оси абсцисс
    :param shift_y: смещение по оси ординат

    '''

    def translate(self, shift_x=0, shift_y=0):
        self.position = Vector2(self.position.x + shift_x, self.position.y + shift_y)


'''
Базовые классы игровых объектов, содержащие в себе базовую информацию об объекте
'''


class Object(ABC):
    def __init__(self, obj_name='Game Object', obj_parent=None, obj_tag='Object'):
        self.activeSelf = True  # переменная, обозначающая включен объект или нет
        self.name = obj_name  # название объекта в сцене
        self.tag = obj_tag  # тэг объекта, поможет при поиске группы объектов с одинаковыми св-вами
        self.parent = obj_parent  # родительский объект в иерархии

        logging.info(f'Object [{self.name}] has been created!')

    def paint(self):
        if ~self.activeSelf:
            return


class GameObject(Object):
    def __init__(self, game_obj_name='Game Object', game_obj_parent=None, game_obj_tag='Object',
                 game_obj_transform=Transform(), game_obj_physics=False, game_obj_falling=False):
        self.transform = game_obj_transform
        self.physics = game_obj_physics
        self.falling = game_obj_falling
        super(GameObject, self).__init__(obj_name=game_obj_name, obj_parent=game_obj_parent, obj_tag=game_obj_tag)


class SpriteObject(GameObject):
    def __init__(self, sprite_obj_name='Game Object', sprite_obj_parent=None, sprite_obj_tag='Object',
                 sprite_obj_transform=Transform(), image_path=""):
        self.sprite = pygame.image.load(image_path) if image_path != "" else logging.info(
            f'Image path has not been defined!')

        super(SpriteObject, self).__init__(game_obj_name=sprite_obj_name, game_obj_parent=sprite_obj_parent,
                                           game_obj_tag=sprite_obj_tag, game_obj_transform=sprite_obj_transform,
                                           game_obj_physics=False, game_obj_falling=False)

    def paint(self, screen):
        super(SpriteObject, self).paint()
        screen.blit(self.sprite,
                    pygame.Rect(self.transform.position.x, self.transform.position.y, self.transform.scale.x,
                                self.transform.position.y))


'''
Класс UI элементов
'''


class Button(SpriteObject):
    def __init__(self, button_on_clicked, ui_obj_name='Button Object', ui_obj_parent=None, ui_obj_tag='button',
                 ui_obj_transform=Transform(), ui_image_path=""):
        self.clicked = button_on_clicked
        super(Button, self).__init__(sprite_obj_name=ui_obj_name, sprite_obj_parent=ui_obj_parent,
                                     sprite_obj_tag=ui_obj_tag, sprite_obj_transform=ui_obj_transform,
                                     image_path=ui_image_path)

    def on_click(self):
        self.clicked if self.clicked else logging.info(f'Clicked event has not been declared')


class AudioPlayer(Object):
    def __init__(self, audio_player_name='Game Object', audio_player_parent=None, audio_player_tag='Audio',
                 audio_path=''):
        self.sound = pygame.mixer.Sound(audio_path) if audio_path != '' else logging.info(
            f'Audio path has not been defined!')
        super(AudioPlayer, self).__init__(obj_name=audio_player_name, obj_parent=audio_player_parent,
                                          obj_tag=audio_player_tag)

    def play(self):
        self.sound.play()


class Animation(SpriteObject):
    def __init__(self, anim_obj_name='Game Object', anim_obj_parent=None, anim_obj_tag='Object',
                 anim_obj_transform=Transform(), image_paths=None):
        self.count = 0
        self.frames = []
        if image_paths:
            for item in image_paths:
                self.frames.append(pygame.image.load(item))
        else:
            logging.info(f'Frames path has not been defined!')

        super(Animation, self).__init__(sprite_obj_name=anim_obj_name, sprite_obj_parent=anim_obj_parent,
                                        sprite_obj_tag=anim_obj_tag, sprite_obj_transform=anim_obj_transform)

    def paint(self, screen):
        self.sprite = self.frames[self.count]
        self.count += 1
        super(Animation, self).paint(screen)
