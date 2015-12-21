#!/usr/bin/env python
import sys
sys.path.append('..')
from common import *
from itertools import combinations

class Eq(object):
    def __init__(self, name, cost, dmg, armor):
        self.name = name
        self.cost = cost
        self.dmg = dmg
        self.armor = armor

class Player(object):
    def __init__(self, name, health, damage, armor, equipment=[]):
        self.name = name
        self.health = health
        self.damage = damage + sum([eq.dmg for eq in equipment])
        self.armor = armor + sum([eq.armor for eq in equipment])
        self.equipment = equipment
    def attack(self, player):
        dmg = self.damage - player.armor
        if dmg < 1:
            dmg = 1
        player.health -= dmg
        #print '%s deals %d damage to %s; %s now has %d hp' % (self.name, dmg, player.name, player.name, player.health)
    def is_dead(self):
        return self.health <= 0

class DayProcessor(Processor):
    def before(self):
        self.weapons = [
                Eq('Dagger', 8, 4, 0),
                Eq('Shortsword', 10, 5, 0),
                Eq('Warhammer', 25, 6, 0),
                Eq('Longsword', 40, 7, 0),
                Eq('Greataxe', 74, 8, 0)
        ]
        self.armors = [
                Eq('None', 0, 0, 0),
                Eq('Leather', 13, 0, 1),
                Eq('Chainmail', 31, 0, 2),
                Eq('Splintmail', 53, 0, 3),
                Eq('Bandedmail', 75, 0, 4),
                Eq('Platemail', 102, 0, 5),
        ]
        self.rings = [
                Eq('None', 0, 0, 0),
                Eq('None', 0, 0, 0),
                Eq('Damage +1', 25, 1, 0),
                Eq('Damage +2', 50, 2, 0),
                Eq('Damage +3', 100, 3, 0),
                Eq('Defense +1', 20, 0, 1),
                Eq('Defense +2', 40, 0, 2),
                Eq('Defense +3', 80, 0, 3)
        ]
        pass
    def process_line(self, line):
        pass

    def run_scenario(self, eq):
        boss = Player('Boss', 100, 8, 2)
        player = Player('Player', 100, 0, 0, eq)
        while True:
            player.attack(boss)
            if boss.is_dead():
                #print 'Boss dies'
                return True
            boss.attack(player)
            if player.is_dead():
                #print 'Player dies'
                return False

    def test(self):
        for w in self.weapons:
            for a in self.armors:
                for (r1, r2) in combinations(self.rings, 2):
                    eq = [w, a, r1, r2]
                    if self.run_scenario(eq):
                        print sum([e.cost for e in eq]), ':', ' '.join([e.name for e in eq])

    def after(self):
        self.test()
        pass

DayProcessor().run()
