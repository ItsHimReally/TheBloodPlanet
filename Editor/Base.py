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
    def __init__(self, vec_x=0.0, vec_y=0.0):
        self.x = vec_x
        self.y = vec_y


class Transform:
    def __init__(self, tr_position=Vector2(), tr_scale=Vector2(), tr_rotate=0, tr_velocity_x=0, tr_velocity_y=0):
        self.position = tr_position
        self.scale = tr_scale
        self.rotation = tr_rotate
        self.velocity_x = tr_velocity_x
        self.velocity_y = tr_velocity_y
        self.acceleration = 0
        self.rect = pygame.Rect(self.position.x, self.position.y, self.scale.x,
                                self.scale.y)
    '''
    Метод перемещения объекта
    
    :param shift_x: смещение по оси абсцисс
    :param shift_y: смещение по оси ординат
    
    '''

    def translate(self, shift_x=0.0, shift_y=0.0):
        self.position = Vector2(self.position.x + shift_x, self.position.y + shift_y)
        self.rect.move_ip(shift_x, shift_y)


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
        if not self.activeSelf:
            return


class GameObject(Object):
    def __init__(self, game_obj_name='Game Object', game_obj_parent=None, game_obj_tag='GameObject',
                 game_obj_transform=Transform()):
        self.transform = game_obj_transform

        super(GameObject, self).__init__(obj_name=game_obj_name, obj_parent=game_obj_parent, obj_tag=game_obj_tag)


class SpriteObject(GameObject):
    def __init__(self, sprite_obj_name='Game Object', sprite_obj_parent=None, sprite_obj_tag='Sprite',
                 sprite_obj_transform=Transform(), image_path=""):
        self.sprite = pygame.transform.scale(pygame.image.load(image_path).convert_alpha(), (
            sprite_obj_transform.scale.x, sprite_obj_transform.scale.y)) if image_path != "" else logging.info(
            f'Image path has not been defined!')

        super(SpriteObject, self).__init__(game_obj_name=sprite_obj_name, game_obj_parent=sprite_obj_parent,
                                           game_obj_tag=sprite_obj_tag, game_obj_transform=sprite_obj_transform)

    def paint(self, screen):
        super(SpriteObject, self).paint()

        screen.blit(self.sprite,
                    pygame.Rect(self.transform.position.x, self.transform.position.y, self.transform.scale.x,
                                self.transform.scale.y))


'''
Класс UI элементов
'''


class Button(SpriteObject):
    def __init__(self, button_on_clicked, ui_obj_name='Button Object', ui_obj_parent=None, ui_obj_tag='Button',
                 ui_obj_transform=Transform(), ui_image_path=""):
        self.clicked = button_on_clicked
        super(Button, self).__init__(sprite_obj_name=ui_obj_name, sprite_obj_parent=ui_obj_parent,
                                     sprite_obj_tag=ui_obj_tag, sprite_obj_transform=ui_obj_transform,
                                     image_path=ui_image_path)

    def on_click(self):
        if self.sprite.get_rect().collidepoint(pygame.mouse.get_pos()):
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
    def __init__(self, anim_obj_name='Game Object', anim_obj_parent=None, anim_obj_tag='Animation',
                 anim_obj_transform=Transform(), image_paths=None):
        self.frames = []
        self.animations = {}
        self.animations_fps = {}
        self.current_animation = []
        self.loop = True
        self.ended = False
        self.flipped = False
        self.animation_delay = 0
        self.last_frame_time = 0
        self.current_frame = 0
        if image_paths:
            self.add_animation('idle', image_paths, 100)
        else:
            logging.info(f'Idle animation paths has not been defined!')

        self.set_animation('idle')

        super(Animation, self).__init__(sprite_obj_name=anim_obj_name, sprite_obj_parent=anim_obj_parent,
                                        sprite_obj_tag=anim_obj_tag, sprite_obj_transform=anim_obj_transform)

    def paint(self, screen):
        self.sprite = self.current_animation[self.current_frame] if not self.flipped else pygame.transform.flip(
            self.current_animation[self.current_frame], True, False)

        current_time = pygame.time.get_ticks()
        if current_time - self.last_frame_time >= self.animation_delay:
            self.last_frame_time = current_time
            if self.loop:
                self.current_frame = self.current_frame + 1 if self.current_frame < len(self.current_animation) - 1 else 0
            else:
                self.current_frame = self.current_frame + 1 if self.current_frame < len(self.current_animation) - 1 else len(self.current_animation) - 1

        super(Animation, self).paint(screen)

    def add_animation(self, name, image_paths, animation_delay, x_scale=0, y_scale=0):
        self.frames = []
        if image_paths:
            for item in image_paths:
                self.frames.append(pygame.transform.scale(pygame.image.load(item).convert_alpha(),
                                                          (self.transform.scale.x if x_scale == 0 else x_scale,
                                                           self.transform.scale.y if y_scale == 0 else y_scale)))
            self.animations.update({name: self.frames})
            self.animations_fps.update({name: animation_delay})
        else:
            logging.info(f'Frames path has not been defined!')

    def set_animation(self, animation, loop=True):
        self.current_animation = self.animations[animation]
        self.current_frame = 0
        self.animation_delay = self.animations_fps[animation]
        self.loop = loop
        self.ended = False


class Movable(Animation):
    def __init__(self, movable_obj_name='Movable Object', movable_obj_parent=None, movable_obj_tag='Movable',
                 movable_obj_transform=Transform(), movable_image_paths=None, movable_obj_velocity_x=5,
                 movable_obj_velocity_y=5,
                 movable_obj_acceleration=1):

        self.transform = movable_obj_transform
        self.transform.velocity_x = movable_obj_velocity_x
        self.transform.velocity_y = movable_obj_velocity_y
        self.transform.acceleration = movable_obj_acceleration
        self.on_ground = True
        self.collisions = [False, False, False, False]  # collisions from left top right

        super(Movable, self).__init__(anim_obj_name=movable_obj_name, anim_obj_parent=movable_obj_parent,
                                      anim_obj_tag=movable_obj_tag, anim_obj_transform=movable_obj_transform,
                                      image_paths=movable_image_paths)

    def move(self, keys):
        # move left check collision
        if keys[pygame.K_a] and not self.collisions[0]:
            self.transform.translate(-1 * self.transform.velocity_x, 0)

        # move right check collision
        if keys[pygame.K_d] and not self.collisions[2]:
            self.transform.translate(self.transform.velocity_x, 0)

        if keys[pygame.K_r]:
            self.transform.translate(0, -100)

        # fall check collision
        if not self.collisions[3] and self.on_ground:
            self.transform.translate(0, 10)



    def check_collision(self, rect, marked_collisions):
        if self.transform.rect.colliderect(rect.transform.rect):

            if abs(self.transform.rect.left - rect.transform.rect.right) <= 10:
                marked_collisions[0] = True

            if abs(self.transform.rect.top - rect.transform.rect.bottom) <= 10:
                marked_collisions[1] = True

            if abs(self.transform.rect.right - rect.transform.rect.left) <= 10:
                marked_collisions[2] = True

            if abs(self.transform.rect.bottom - rect.transform.rect.top) <= 10:
                marked_collisions[3] = True

        return marked_collisions


'''
Классы для состояний врага
'''


class PatrolEnemyState:
    def __init__(self, next_pos=Vector2()):
        self.next_position = next_pos


class AttackEnemyState:
    def __init__(self, player_transform=Transform()):
        pass


'''
Класс врага
'''


class Enemy(Movable):
    def __init__(self, enemy_obj_name='Enemy Object', enemy_obj_parent=None, enemy_obj_tag='Enemy',
                 enemy_obj_transform=Transform(), enemy_image_path=None, enemy_obj_velocity_x=5, enemy_obj_velocity_y=5,
                 enemy_obj_acceleration=1, start_vector=Vector2(), finish_vector=Vector2()):

        self.dead = False
        self.start_pos = start_vector
        self.finish_pos = finish_vector
        self.infected = False

        self.state = PatrolEnemyState(finish_vector)

        transform = Transform(Vector2(start_vector.x, start_vector.y), enemy_obj_transform.scale)

        super(Enemy, self).__init__(movable_obj_name=enemy_obj_name, movable_obj_parent=enemy_obj_parent,
                                    movable_obj_tag=enemy_obj_tag, movable_obj_transform=transform,
                                    movable_image_paths=enemy_image_path, movable_obj_velocity_x=enemy_obj_velocity_x,
                                    movable_obj_velocity_y=enemy_obj_velocity_y,
                                    movable_obj_acceleration=enemy_obj_acceleration)

    def move(self, keys):
        if not self.dead and not self.infected:
            k = 1 if ((self.transform.position.x - self.state.next_position.x) * -1) >= 0 else -1

            if k == 1:
                if self.transform.position.x + self.transform.velocity_x >= self.state.next_position.x:
                    self.state = PatrolEnemyState(self.start_pos)
                    self.flipped = True

            elif k == -1:
                if self.transform.position.x - self.transform.velocity_x <= self.state.next_position.x:
                    self.state = PatrolEnemyState(self.finish_pos)
                    self.flipped = False
                    self.die()

            self.transform.translate(self.transform.velocity_x * k, 0)
        else:
            super().move(keys)

    def die(self):
        self.set_animation('Die', loop=False)
        self.dead = True


class Player(Movable):
    def __init__(self, player_obj_name='Player Object', player_obj_parent=None, player_obj_tag='Player',
                 player_obj_transform=Transform(), player_image_path=None, player_obj_velocity_x=5,
                 player_obj_acceleration=1):
        super(Player, self).__init__(movable_obj_name=player_obj_name, movable_obj_parent=player_obj_parent,
                                     movable_obj_tag=player_obj_tag, movable_obj_transform=player_obj_transform,
                                     movable_image_paths=player_image_path,
                                     movable_obj_velocity_x=player_obj_velocity_x,
                                     movable_obj_acceleration=player_obj_acceleration)

    def move(self, keys):
        if (keys[pygame.K_SPACE] or keys[pygame.K_w]) and self.collisions[3] and not self.collisions[1]:
            self.on_ground = False
            self.transform.velocity_y = -20
            self.set_animation('jump')
        super().move(keys)
        if not self.on_ground:
            self.jump()

    def jump(self):
        if self.transform.velocity_y >= 21:
            self.transform.velocity_y = 0
            self.on_ground = True
            self.set_animation('idle')
            return

        if self.collisions[1]:
            self.transform.velocity_y = 0

        self.transform.translate(0, self.transform.velocity_y)
        self.transform.velocity_y += self.transform.acceleration
