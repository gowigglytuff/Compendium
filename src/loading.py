

import pygame
from data import *
from features import *
from mapClasses import *
from tiler import *
from keyboards import *
from random import randrange

def init_game(gd, gc):
    '''
    :type gc: GameController
    :type gd: GameData
    :return:
    '''
    pygame.init()
    pygame.display.set_caption('NPC')


    # load all keyboard managers
    # TODO: add other possible Keyboard_managers
    gc.add_keyboard_manager(InGameKeyboardManager.ID, InGameKeyboardManager(gc, gd))
    gc.add_keyboard_manager(InMenuKeyboardManager.ID, InMenuKeyboardManager(gc, gd))
    gc.add_keyboard_manager(InPersonMenuKeyboardManager.ID, InMenuKeyboardManager(gc, gd))
    gc.add_keyboard_manager(InTextKeyboardManager.ID, InTextKeyboardManager(gc, gd))
    gc.set_keyboard_manager(InGameKeyboardManager.ID)

    #load menus
    gd.add_overlay("menu1", Overlay(gc, gd, "menu1", [], 700, 500, Spritesheet("assets/menu1/menu1.png", 200, 100)))
    gd.add_menu("menu1", Menu(gc, gd, "menu1", ["hi", "hello", "yo"], True, "hi", "menu1"))

    gd.add_overlay("menu2", Overlay(gc, gd, "menu2", [], 200, 500, Spritesheet("assets/menu1/menu1.png", 200, 100)))
    gd.add_menu("menu2", Menu(gc, gd, "menu2", ["Clayton", "Adam", "Jim"], True, "hi", "menu2"))

    gd.add_overlay("top_bar", Overlay(gc, gd, "top_bar", [], 100, 100, Spritesheet("assets/menu1/top_bar.png", 700, 100)))

    gd.add_overlay("text_box", Overlay(gc, gd, "text_box", [], 250, 550, Spritesheet("assets/menu1/text_box.png", 500, 150)))



    # add the player to the game
    gd.add_player("Player", Player(2, 3, 2, 3, 32, 40, Spritesheet("assets/player/player_sheet.png", 32, 40), "Bug", gc, gd))



    init_room_1(gc, gd)
    init_room_2(gc, gd)
    init_room_3(gc, gd)
    init_room_4(gc, gd)

def init_room_1(gc, gd):
    # room #1

    # add the room #1, generate the grid, and add the background and doors
    gd.add_room("room1", Room("room1", 1, 1, 6, 6, ["room1"]))
    gd.room_list["room1"].generate_room_grid()
    gd.room_list["room1"].add_room_BG("room1", BG(1, 0, "room1", [pygame.image.load("assets/backgrounds/Background2.png").convert_alpha()], gc, gd))

    #TODO: incorporate tile maps better
    # map = TileMap("assets/map/practise.csv")
    # gd.room["room1"].add_room_BG("room1_b", BG(1, 1, "room1_b", [map.return_map()], gc, gd))

    gd.room_list["room1"].add_room_door("room1_door1", Door("room1", "room2", 2, 1, 1, 14, "room1_door1"))
    gd.room_list["room1"].add_room_door("room1_door2", Door("room1", "room3", 5, 0, 2, 4, "room1_door2"))

    # add the NPC characters to the game
    gd.add_character("Walker", Walker(2, 3, 2, 3, 32, 40, Spritesheet("assets/testing/sprite_sheet.png", 32, 40), "Walker", gc, gd, "left"))

    gd.add_character("Pink_Walker", Walker(5, 5, 5, 5, 32, 40, Spritesheet("assets/testing/sprite_sheet.png", 32, 40), "Pink_Walker", gc, gd, "left"))

    #add props to the game
    gd.add_prop("Prop1", Prop(3, 3, 3, 3, 32, 40, Spritesheet("assets/prop1.png", 32, 40), "Prop1", gc, gd, 1, 1))
    gd.add_prop("lamp", Prop(2, 5, 2, 5, 32, 40, Spritesheet("assets/lamp.png", 32, 40), "lamp", gc, gd, 1, 1))

    #add all the features to the current room
    gd.room_list["room1"].add_room_character("Walker")
    gd.room_list["room1"].add_room_character("Pink_Walker")
    gd.room_list["room1"].add_room_prop("Prop1")
    gd.room_list["room1"].add_room_prop("lamp")

    # add position manager to it's room and make it tell the tile array what it's filled with
    gd.add_positioner("room1", Position_Manager("room1", gc, gd))
    gd.positioner["room1"].fill_tiles("room1")
    gd.positioner["room1"].fill_doors("room1")

    # activate the timers for animation and actions for the NPC Walker (make this apply to all that are in room)
    for character in gd.room_list["room1"].character_list:
        gd.character_list[character].activate_timers()

def init_room_2(gc, gd):
    # room#2

    # add the room #2, generate the grid, and add the background and doors
    gd.add_room("room2", Room("room2", 1, 1, 15, 15, ["room2"]))
    gd.room_list["room2"].generate_room_grid()
    gd.room_list["room2"].add_room_BG("room2", BG(1, 1, "room2", [pygame.image.load("assets/backgrounds/Background1.png").convert_alpha()], gc, gd))
    gd.room_list["room2"].add_room_door("room2_door1", Door("room2", "room1", 1, 15, 2, 2, "room2_door1"))


    # add features for room 2
    gd.add_prop("lamp4", Prop(1, 1, 1, 1, 32, 40, Spritesheet("assets/lamp.png", 32, 40), "lamp4", gc, gd, 1, 1))
    gd.add_prop("lamp2", Prop(10, 5, 10, 5, 32, 40, Spritesheet("assets/lamp.png", 32, 40), "lamp2", gc, gd, 1, 1))
    gd.add_prop("lamp3", Prop(8, 7, 8, 7, 32, 40, Spritesheet("assets/lamp.png", 32, 40), "lamp3", gc, gd, 1, 1))

    gd.add_decoration("Grass1", Decoration(2, 13, 2, 13, 32, 32, Spritesheet("assets/grass.png", 32, 32), "Grass1", gc, gd, 1, 1, [[2, 13], [2, 14], [3, 13], [3, 14]]))

    # attach all features to room
    gd.room_list["room2"].add_room_prop("lamp2")
    gd.room_list["room2"].add_room_prop("lamp3")
    gd.room_list["room2"].add_room_prop("lamp4")
    gd.room_list["room2"].add_room_decoration("Grass1")

    # add position manager to it's room and make it tell the tile array what it's filled with, then populate doors
    gd.add_positioner("room2", Position_Manager("room2", gc, gd))
    gd.positioner["room2"].fill_tiles("room2")
    gd.positioner["room2"].fill_doors("room2")



def init_room_3(gc, gd):
    gd.add_room("room3", Room("room3", 1, 2, 3, 3, ["room3"]))
    gd.room_list["room3"].generate_room_grid()
    gd.room_list["room3"].add_room_BG("room3", BG(1, 1, "room3", [pygame.image.load("assets/backgrounds/Background3.png").convert_alpha()], gc, gd))
    gd.room_list["room3"].add_room_door("room3_door1", Door("room3", "room1", 2, 5, 5, 1, "room3_door1"))

    gd.add_character("Pixie", Pixie(2, 2, 2, 2, 32, 40, Spritesheet("assets/testing/sprite_sheet.png", 32, 40), "Pixie", gc, gd))

    gd.add_character("Pixie_b", Pixie(3, 4, 3, 4, 32, 40, Spritesheet("assets/testing/sprite2_sheet.png", 32, 40), "Pixie_b", gc, gd))

    gd.room_list["room3"].add_room_character("Pixie")
    gd.room_list["room3"].add_room_character("Pixie_b")


    gd.add_positioner("room3", Position_Manager("room3", gc, gd))
    gd.positioner["room3"].fill_tiles("room3")
    gd.positioner["room3"].fill_doors("room3")

    for character in gd.room_list["room3"].character_list:
        gd.character_list[character].activate_timers()


def init_room_4(gc, gd):

    gd.add_room("room4", Room("room4", 1, 1, 100, 50, ["room4"]))
    gd.room_list["room4"].generate_room_grid()

    big_map = TileMap("assets/map/big_map.csv", "grass", "water")
    gd.room_list["room4"].add_room_BG("room4", BG(1, 1, "room4", [big_map.return_map()], gc, gd))
    gd.room_list["room4"].add_room_BG("room4b", BG(51, 1, "room4b", [big_map.return_map()], gc, gd))



    for name in range(40):
        rand_x = randrange(1, 100)
        rand_y = randrange(1, 50)
        gd.add_character(("Pixie" + str(name)), Pixie(rand_x, rand_y, rand_x, rand_y, 32, 40, Spritesheet("assets/testing/sprite_sheet.png", 32, 40), ("Pixie" + str(name)), gc, gd))
        gd.room_list["room4"].add_room_character(("Pixie" + str(name)))

    gd.add_positioner("room4", Position_Manager("room4", gc, gd))
    gd.positioner["room4"].fill_tiles("room4")
    gd.positioner["room4"].fill_doors("room4")