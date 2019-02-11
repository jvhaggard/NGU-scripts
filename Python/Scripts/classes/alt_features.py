"""Feature class handles the alternative features in the game for Windows Server."""
from classes.inputs import Inputs
from classes.alt_inputs import AltInputs
from classes.features import Features
from classes.navigation import Navigation
from classes.window import Window
from collections import deque, namedtuple
from decimal import Decimal
import math
import ngucon as ncon
import re
import time
import win32con as wcon
import win32gui
import win32api
import usersettings as userset
from classes.window import Window as window
from classes.discord import Discord

class AltFeatures(Navigation, Inputs, AltInputs):
    """Handles the Windows 2018 different features in the game."""

    def get_inventory_slots(self, slots):
        """Get coords for inventory slots from 1 to slots."""
        point = namedtuple("p", ("x", "y"))
        i = 1
        row = 1
        x_pos = ncon.INVENTORY_SLOTS_X
        y_pos = ncon.INVENTORY_SLOTS_Y
        coords = []

        while i <= slots:
            x = x_pos + (i - (12 * (row - 1))) * 50
            y = y_pos + ((row - 1) * 50)
            coords.append(point(x, y))
            if i % 12 == 0:
                row += 1
            i += 1
        return coords

    def alt_merge_equipment(self):
        """Navigate to inventory and merge equipment."""
        self.menu("inventory")
        time.sleep(0.2)
        for slot in self.equipment:
            if (slot == "cube"):
                return
            self.d_click(self.equipment[slot]["x"], self.equipment[slot]["y"])

    def alt_boost_equipment(self):
        """Boost all equipment."""
        self.menu("inventory")
        time.sleep(0.2)
        for slot in self.equipment:
            if (slot == "cube"):
                return
            self.a_click(self.equipment[slot]["x"], self.equipment[slot]["y"])

    def alt_merge_inventory(self, slots):
        """Merge all inventory slots starting from 1 to slots.

        Keyword arguments:
        slots -- The amount of slots you wish to merge
        """
        self.menu("inventory")
        coords = self.get_inventory_slots(slots)
        for slot in coords:
            self.d_click(slot.x, slot.y)

    def alt_boost_inventory(self, slots):
        """Merge all inventory slots starting from 1 to slots.

        Keyword arguments:
        slots -- The amount of slots you wish to merge
        """
        self.menu("inventory")
        coords = self.get_inventory_slots(slots)
        for slot in coords:
            self.a_click(slot.x, slot.y)        
    def boost_cube(self):
        """Boost cube."""
        self.menu("inventory")
        self.click(self.equipment["cube"]["x"], self.equipment["cube"]["y"], "right")

    def click_quest(self):
        """Right click slot 1 and 2 for quests"""
        # This assumes you aren't getting any other drops, might need to put in a transform check or item OCR?
        self.menu("inventory")
        self.click(ncon.INVENTORY_SLOTS_X, ncon.INVENTORY_SLOTS_Y, "right")
        time.sleep(.5)
        self.click((ncon.INVENTORY_SLOT_2X), ncon.INVENTORY_SLOT_2Y, "right")

    def quest_finished(self):
        self.menu("quest")
        self.click(ncon.QUEST_ACTION_X, ncon.QUEST_ACTION_Y)

    def quest_subcontract(self):
        self.menu("quest")
        self.click(ncon.QUEST_SUBCONTRACT_X, ncon.QUEST_SUBCONTRACT_Y)

    def check_challenge(self):
        """Check if a challenge is active."""
        self.rebirth()
        self.click(ncon.CHALLENGEBUTTONX, ncon.CHALLENGEBUTTONY)
        time.sleep(userset.LONG_SLEEP)
        color = self.get_pixel_color(ncon.CHALLENGEACTIVEX,
                                        ncon.CHALLENGEACTIVEY)

        return True if color == ncon.CHALLENGEACTIVECOLOR else False
    

    #TODO: Why is this not importing from inputs and I had to put it here?
    def alt_ctrl_click(self, x, y):
        """Clicks at pixel x, y while simulating the CTRL button to be down."""
        x += window.x
        y += window.y
        lParam = win32api.MAKELONG(x, y)
        # MOUSEMOVE event is required for game to register clicks correctly
        win32gui.PostMessage(window.id, wcon.WM_MOUSEMOVE, 0, lParam)
        time.sleep(.7)
        #Ctrl then left click
        win32gui.PostMessage(window.id, wcon.WM_KEYDOWN, 0x11, 0)
        time.sleep(.2)   
        win32gui.PostMessage(window.id, wcon.WM_LBUTTONDOWN,
                                wcon.MK_LBUTTON, lParam)
        time.sleep(.2)
        print("Down")
        win32gui.PostMessage(window.id, wcon.WM_LBUTTONUP,
                                wcon.MK_LBUTTON, lParam)
        time.sleep(.2)
        win32gui.PostMessage(window.id, wcon.WM_KEYUP, 0x11, 0)
        time.sleep(0.5)

    def alt_transform_slot(self, slots, threshold=0.8, consume=False):
        """Check if slot is transformable and transform if it is.
        Be careful using this, make sure the item you want to transform is
        not protected, and that all other items are protected, this might
        delete items otherwise. Another note, consuming items will show
        a special tooltip that will block you from doing another check
        for a few seconds, keep this in mind if you're checking multiple
        slots in succession.
        Keyword arguments:
        slot -- The slot you wish to transform, if possible
        threshold -- The fuzziness in the image search, I recommend a value
                     between 0.7 - 0.95.
        consume -- Set to true if item is consumable instead.
        """

        self.menu("inventory")
        coords = self.get_inventory_slots(slots)
        print(coords)
        for slot in coords[::-1]:
            self.click(slot.x,slot.y)
            time.sleep(.2)
            if consume:
                coords = self.image_search(Window.x, Window.y, Window.x + 960, Window.y + 600, self.get_file_path("images", "consumable.png"), threshold)
            else:
                coords = self.image_search(Window.x, Window.y, Window.x + 960, Window.y + 600, self.get_file_path("images", "transformable.png"), threshold)

            if coords:
                self.ctrl_click([slot.x][-1], [slot.y][-1])
            time.sleep(5)
            break
    
    def clear_keypresses(self):
        #D key gets stuck down on d_click???
        win32gui.PostMessage(window.id, wcon.WM_KEYUP, 0x44, 1)
        #A key gets stuck down on a_click???
        win32gui.PostMessage(window.id, wcon.WM_KEYUP, 0x41, 1)