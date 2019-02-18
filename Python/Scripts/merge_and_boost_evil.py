"""
Merge and Boost script
No Transformation at this time.
"""

# Helper classes
from classes.features import Features
from classes.alt_features import AltFeatures
from classes.alt_inputs import AltInputs
from classes.inputs import Inputs
from classes.navigation import Navigation
from classes.stats import Stats, EstimateRate, Tracker
from classes.upgrade import Upgrade
from classes.window import Window
from classes.discord import Discord
from datetime import datetime
from pytz import timezone

import ngucon as ncon
import time

 
tz = timezone('EST')
w = Window()
i = Inputs()
nav = Navigation()
feature = Features()
alt_features = AltFeatures()

Window.x, Window.y = i.pixel_search(ncon.TOP_LEFT_COLOR, 0, 0, 400, 600)
nav.menu("inventory")

u = Upgrade(37500, 37500, 2, 2, 3)

print(w.x, w.y)
tracker = Tracker(3)

quest_done = False

while True:  # main loop to go foreverrrrr
    #Add Money Pit Check
    feature.pit()
    #Add Save Check
    feature.save_check()
    #Add Spin Check
    feature.spin()
    #Add Blood Magic Check
    # feature.speedrun_bloodpill()
    #Ygg
    feature.ygg()
    #Adjust Energy NGU and try to BB
    # feature.set_ngu([1,4,5,6])
    # feature.bb_ngu(4e9, [1,4,5,6], 1.05)
    #Adjust Magic NGU and try to BB
    # feature.set_ngu([2,3], magic=True)
    # feature.bb_ngu(1e9, [2, 3], 1.05, magic=True)
    #Gold diggers
    # feature.gold_diggers([1, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    # feature.wandoos(True)
    #Equip
    alt_features.alt_boost_equipment()
    alt_features.alt_merge_equipment()
    # alt_features.clear_keypresses()
    alt_features.alt_merge_inventory(7)
    alt_features.alt_boost_inventory(6)
    alt_features.boost_cube()
    # time.sleep(1)
    #It will ping you the quest is complete every 3 minutes or so
    #Make it only fire once with a variable
    # if alt_features.quest_complete(): #and quest_done == False:
    #     Discord.send_message(('Quest Completed!'), Discord.ERROR)
    #     alt_features.quest_finished()
    #     # quest_done  = True 
    #     alt_features.quest_finished() #Click to start new quest
    #     alt_features.quest_subcontract() #click to start subcontract
        # feature.adventure(itopod=True, itopodauto=True)
    # if not alt_features.quest_complete() and quest_done == False:
        # alt_features.click_quest() # Clicks first 2 spot for quest items to merge
    #Start new quest > make quest_done = false
    # alt_features.alt_transform_slot(4,threshold=.9,consume=True)
    # alt_feature.alt_transform_slot(5,threshold=.9,consume=True)
    # alt_feature.alt_transform_slot(6,threshold=.9,consume=True)
    #Sets you to your designed zone in case you get bumped out somehow
    # feature.adventure(zone=13, highest=False, itopod=False, itopodauto=False)
    # feature.snipe(0, 300, once=False, highest=True, bosses=False)
    #Sleep before trying again
    print(datetime.now(tz))
    print("===")
    print("Sleeping for 180 seconds")
    # print("ITOPOD / Snipe for 300 seconds")
    time.sleep(180)
    print("===")
    #
    tracker.progress()