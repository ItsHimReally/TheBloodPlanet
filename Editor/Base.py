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
        self.velocity_x = 0
        self.velocity_y = 0
        self.acceleration = 0

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
                 game_obj_transform=Transform()):
        self.transform = game_obj_transform
        super(GameObject, self).__init__(obj_name=game_obj_name, obj_parent=game_obj_parent, obj_tag=game_obj_tag)


class SpriteObject(GameObject):
    def __init__(self, sprite_obj_name='Game Object', sprite_obj_parent=None, sprite_obj_tag='Object',
                 sprite_obj_transform=Transform(), image_path=""):
        self.sprite = pygame.image.load(image_path).convert_alpha() if image_path != "" else logging.info(f'Image path has not been defined!')
        self.animator = None
        super(SpriteObject, self).__init__(game_obj_name=sprite_obj_name, game_obj_parent=sprite_obj_parent,
                                         game_obj_tag=sprite_obj_tag, game_obj_transform=sprite_obj_transform)

    def paint(self, screen):
        super(SpriteObject, self).paint()
        screen.blit(self.sprite, pygame.Rect(self.transform.position.x, self.transform.position.y, self.transform.scale.x, self.transform.position.y))

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
        if self.sprite.get_rect().collidepoint(pygame.mouse.get_pos()):
            self.clicked()
        #self.clicked if self.clicked else logging.info(f'Clicked event has not been declared')


class AudioPlayer(Object):
    def __init__(self, audio_player_name='Game Object', audio_player_parent=None, audio_player_tag='Audio',
                 audio_path=''):
        self.sound = pygame.mixer.Sound(audio_path) if audio_path != '' else logging.info(f'Audio path has not been defined!')
        super(AudioPlayer, self).__init__(obj_name=audio_player_name, obj_parent=audio_player_parent,
                                     obj_tag=audio_player_tag)

    def play(self):
        self.sound.play()


# class Animation(SpriteObject):
#     def __init__(self, anim_obj_name='Game Object', anim_obj_parent=None, anim_obj_tag='Object',
#                  anim_obj_transform=Transform(), image_paths=None):
#         self.count = 0
#         self.frames = []
#         if image_paths:
#             for item in image_paths:
#                 self.frames.append(pygame.image.load(item).convert_alpha())
#         else:
#             logging.info(f'Frames path has not been defined!')
#
#         super(Animation, self).__init__(sprite_obj_name=anim_obj_name, sprite_obj_parent=anim_obj_parent,
#                                          sprite_obj_tag=anim_obj_tag, sprite_obj_transform=anim_obj_transform)
#
#     def paint(self, screen):
#         frame = ((pygame.time.get_ticks() // 100) % 2)
#         self.sprite = self.frames[frame]
#         # self.count = self.count + 1 if self.count < len(self.frames) - 1 else 0
#         super(Animation, self).paint(screen)

class Animation(SpriteObject):
    def __init__(self, anim_obj_name='Game Object', anim_obj_parent=None, anim_obj_tag='Object',
                 anim_obj_transform=Transform(), image_paths=None):
        self.frames = []
        self.animations = {}
        self.animations_fps = {}
        self.current_animation = []
        self.loop = True
        self.ended = False
        self.add_animation('idle', image_paths, 100)
        self.set_animation('idle')
        super(Animation, self).__init__(sprite_obj_name=anim_obj_name, sprite_obj_parent=anim_obj_parent,
                                         sprite_obj_tag=anim_obj_tag, sprite_obj_transform=anim_obj_transform)

    def paint(self, screen):
        if self.loop and not self.ended:
            if len(self.current_animation) > 1:
                frame = ((pygame.time.get_ticks() // self.animation_delay) % 2)
                if frame == len(self.current_animation) - 1:
                    self.ended = True
                self.sprite = self.current_animation[frame]
            else:
                self.sprite = self.current_animation[0]
        else:
            self.sprite = self.current_animation[len(self.current_animation) - 1]
        super(Animation, self).paint(screen)

    def add_animation(self, name, image_paths, animation_delay):
        self.frames = []
        if image_paths:
            for item in image_paths:
                self.frames.append(pygame.image.load(item).convert_alpha())
            self.animations.update({name: self.frames})
            self.animations_fps.update({name: animation_delay})
        else:
            logging.info(f'Frames path has not been defined!')
    def set_animation(self, animation, loop=True):
        self.current_animation = self.animations[animation]
        self.animation_delay = self.animations_fps[animation]
        self.loop = loop
        # self.frame = self.animations[animation][0]


class Movable(Animation):
    def __init__(self, movable_obj_name='Movable Object', movable_obj_parent=None, movable_obj_tag='Movable',
                 movable_obj_transform=Transform(), movable_image_paths=None, movable_obj_velocity_x=5, movable_obj_acceleration=1):
        self.transform = movable_obj_transform
        self.transform.velocity_x = movable_obj_velocity_x
        self.transform.acceleration = movable_obj_acceleration
        self.on_ground = True
        super(Movable, self).__init__(anim_obj_name=movable_obj_name, anim_obj_parent=movable_obj_parent,
                                         anim_obj_tag=movable_obj_tag, anim_obj_transform=movable_obj_transform, image_paths=movable_image_paths)


class Enemy(Movable):
    def __init__(self, enemy_obj_name='Enemy Object', enemy_obj_parent=None, enemy_obj_tag='Enemy',
                 enemy_obj_transform=Transform(), enemy_image_path=None, enemy_obj_velocity_x=5, enemy_obj_acceleration=1):
        super(Enemy, self).__init__(movable_obj_name=enemy_obj_name, movable_obj_parent=enemy_obj_parent,
                                         movable_obj_tag=enemy_obj_tag, movable_obj_transform=enemy_obj_transform,
                                            movable_image_paths=enemy_image_path, movable_obj_velocity_x=enemy_obj_velocity_x, movable_obj_acceleration=enemy_obj_acceleration)

class Player(Movable):
    def __init__(self, player_obj_name='Player Object', player_obj_parent=None, player_obj_tag='Player',
                 player_obj_transform=Transform(), player_image_path=None, player_obj_velocity_x=5, player_obj_acceleration=1):
        super(Player, self).__init__(movable_obj_name=player_obj_name, movable_obj_parent=player_obj_parent,
                                         movable_obj_tag=player_obj_tag, movable_obj_transform=player_obj_transform,
                                            movable_image_paths=player_image_path, movable_obj_velocity_x=player_obj_velocity_x, movable_obj_acceleration=player_obj_acceleration)
    def move(self, keys):
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.on_ground:
            self.on_ground = False
            self.transform.velocity_y = -20
        if keys[pygame.K_a]:
            self.transform.translate(-1 * self.transform.velocity_x)
        if keys[pygame.K_d]:
            self.transform.translate(self.transform.velocity_x)
        if not self.on_ground:
            self.fall()
    def fall(self):
        if self.transform.velocity_y >= 21:
            self.transform.velocity_y = 0
            self.on_ground = True
            return
        self.transform.translate(0, self.transform.velocity_y)
        self.transform.velocity_y += self.transform.acceleration
