# !/usr/bin/env python
# -*- coding: utf-8 -*-
"""
class Gun:
属性:
self.type   # 型号
self.damage   # 伤害
self.bullet_count   # 子弹数量
方法:
add_bullet(self.count)    # 添加子弹
shoot(self.enemy)
"""


class Gun:
    def __init__(self, type, damage, bullet_count):
        self.type = type
        self.damage = damage
        self.bullet_count = bullet_count
        self.gun = None

    def add_bullet(self, count):
        self.bullet_count += count

    def shoot(self, enemy):
        if self.bullet_count:
            self.bullet_count -= 1
            # TODO 敌方受伤
            enemy.hurt(self)
        else:
            self.bullet_count(20)

    def __str__(self):
        return "%s枪支的伤害为:%d,子弹数量为:%d" % (self.type, self.damage, self.bullet_count)



"""
class person:
属性:
self.role    # 类型
self.hp      # 血量
self.state   # 状态
self.gun     # 拥有枪支类型
方法:
fire(self,enemy)   # 开火
hurt(self.enemy_gun)   # 受伤
"""


class Person:
    def __init__(self, role, gun):
        self.role = role
        self.gun = gun
        self.hp = 100
        self.state = "活的"

    def fire(self, enemy):
        if self.gun is None:
            print("请添加枪支")
        else:
            self.gun.shoot(enemy)

    def hurt(self, enemy_gun):
        self.hp -= enemy_gun.damage
        if self.hp <= 0:
            self.hp = 0
            self.state = "死亡"
            print("%s玩家已经死亡" % self.role)
        else:
            print("%s玩家受伤" % self.role)

    def __str__(self):
        return "%s玩家的血量为:%d,状态:%s,枪支:%s" % (self.role, self.hp, self.state, self.gun)


ak47 = Gun("ak47", 40, 20)
ak48 = Gun("ak48", 80, 18)
badman = Person("坏人", ak47)
police = Person("警察", ak48)

badman.fire(police)
police.fire(badman)
badman.fire(police)
police.fire(badman)
print(badman)
print(police)
