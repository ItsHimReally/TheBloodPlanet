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

    def Translate(self, shift_x=0, shift_y=0):
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
                 game_obj_transform=Transform()):
        self.transform = game_obj_transform
        super(GameObject, self).__init__(obj_name=game_obj_name, obj_parent=game_obj_parent, obj_tag=game_obj_tag)


class SpriteObject(GameObject):
    def __init__(self, sprite_obj_name='Game Object', sprite_obj_parent=None, sprite_obj_tag='Object',
                 sprite_obj_transform=Transform(), image_path=""):
        self.sprite = pygame.image.load(image_path) if image_path != "" else logging.info(f'Image path has not been defined!')
        super(GameObject, self).__init__(game_obj_name=sprite_obj_name, game_obj_parent=sprite_obj_parent,
                                         game_obj_tag=sprite_obj_tag, game_obj_transform=sprite_obj_transform)

    def paint(self, screen):
        super(SpriteObject, self).paint()
        screen.blit(self.sprite, pygame.Rect(self.transform.position, self.transform.scale))


class AudioPlayer(Object):
    def __init__(self, audio_player_name='Game Object', audio_player_parent=None, audio_player_tag='Object'):
        pass
