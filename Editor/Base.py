"""
Файл с основной структурой редактора, импортировать во всех рабочих python-файлах проекта
"""

# импорты основных библиотек
import pygame, logging
from abc import ABC

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

    def draw(self):
        if ~self.activeSelf:
            return


class GameObject(Object):
    def __init__(self, game_obj_name='Game Object', game_obj_parent=None, game_obj_tag='Object',
                 game_obj_transform=Transform()):
        self.transform = game_obj_transform
        super(GameObject, self).__init__(obj_name=game_obj_name, obj_parent=game_obj_parent, obj_tag=game_obj_tag)
