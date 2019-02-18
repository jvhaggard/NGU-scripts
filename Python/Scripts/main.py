"""3-minute rebirth script"""

# Challenges
from challenges.basic import Basic
from challenges.level import Level

# Helper classes
from classes.challenge import Challenge
from classes.features import Features
from classes.alt_features import AltFeatures
from classes.inputs import Inputs
from classes.alt_inputs import AltInputs
from classes.navigation import Navigation
from classes.stats import Stats, EstimateRate, Tracker
from classes.upgrade import Upgrade
from classes.window import Window
from classes.discord import Discord
import usersettings as userset

import ngucon as ncon
import time

def advanced_run(f, af, i):
    i.send_string("r")
    time.sleep(.5)
    i.send_string("t")
    time.sleep(.5)
    f.time_machine(5e8, 5e8)
    f.augments({"EB": 0.7, "CS": 0.3}, 2e9)
    f.blood_magic(8)
    f.advanced_training(9e9)
    af.boost_cube()
    f.gold_diggers([2, 4, 5, 6, 7, 8, 9, 11, 12])

def speedrun(duration, f, af, i):
    """Start a speedrun.

    Keyword arguments
    duration -- duration in minutes to run
    f -- feature object
    """
    adv_done = False
    f.do_rebirth()
    start = time.time()
    end = time.time() + (duration * 60) + 1
    f.nuke(125) #Stops right after BAE
    # f.loadout(1)  # Gold drop equipment
    f.adventure(highest=True)
    time.sleep(4)
    # f.loadout(2)  # Bar/power equimpent
    f.adventure(itopod=True, itopodauto=True)
    f.time_machine(1e9, 1e9)
    f.augments({"EB": 0.7, "CS": 0.3}, 2e9)
    # f.augments({"SM": 0.7, "AA": 0.3}, 2e9)
    # f.augments({"AE": 0.8, "ES": 0.2}, 5e9)
    f.blood_magic(8)
    f.gold_diggers([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    feature.bb_ngu(4e9, [1, 2, 3, 4, 5, 6], 1.05)
    feature.bb_ngu(6e9, [1, 2, 3, 4], 1.05, magic=True)
    while time.time() < end - 20:
        f.wandoos(True)
        if time.time () > start + 40 and time.time () < start + 1150:
            try:
                NGU_energy = f.get_idle_cap()
                feature.assign_ngu(NGU_energy, [7, 8, 9])
                NGU_magic = f.get_idle_cap(magic=True)
                feature.assign_ngu(NGU_magic, [5, 6, 7], magic=True)
            except ValueError:
                print("couldn't assign e/m to NGUs")
            time.sleep(0.5)
        if (time.time () > start + 780) and adv_done == False:
            advanced_run(f, af, i)
            adv_done = True
            f.nuke()
        if (time.time () > start + 1200):
                af.boost_cube()
                f.gold_diggers([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
                time.sleep(180)
    f.nuke()
    time.sleep(2)
    f.fight()
    af.boost_cube()
    if af.quest_complete(): #and quest_done == False:
        Discord.send_message(('Quest Completed!'), Discord.ERROR)
        af.quest_finished()
        # quest_done  = True 
        af.quest_finished() #Click to start new quest
        af.quest_subcontract() #click to start subcontract
    f.pit()
    f.spin()
    f.save_check()
    tracker.progress()
    # f.ygg(rebirth=True) # Harvest for one hour + shorter runs outside of 24
    # u.em()
    # tracker.adjustxp()
    # f.speedrun_bloodpill()
    while time.time() < end:
        time.sleep(0.1)

    return

def check_challenge(self):
    """Check if a challenge is active."""
    self.rebirth()
    self.click(ncon.CHALLENGEBUTTONX, ncon.CHALLENGEBUTTONY)
    time.sleep(userset.LONG_SLEEP)
    color = self.get_pixel_color(ncon.CHALLENGEACTIVEX,
                                    ncon.CHALLENGEACTIVEY)

    return True if color == ncon.CHALLENGEACTIVECOLOR else False

def challenger():
    """Defeat target boss."""
    for x in range(3):
        speedrun(3, feature, alt_features, i)
        if not alt_features.check_challenge():
            return
    for x in range(3):
        speedrun(5, feature, alt_features, i)
        if not alt_features.check_challenge():
            return
    for x in range(4):
        speedrun(15, feature, alt_features, i)
        if not alt_features.check_challenge():
            return
    for x in range(4):
        speedrun(30, feature, alt_features, i)
        if not alt_features.check_challenge():
            return
    return

w = Window()
i = Inputs()
nav = Navigation()
feature = Features()
alt_features = AltFeatures()
ai = AltInputs()

Window.x, Window.y = i.pixel_search(ncon.TOP_LEFT_COLOR, 0, 0, 400, 600)
nav.menu("inventory")

u = Upgrade(37500, 37500, 1, 1, 3)

print(w.x, w.y)
tracker = Tracker(3)
c = Challenge()
# print(c.check_challenge())
count = 0


#feature.speedrun_bloodpill()
while True:  # main loop
# while count <= 1: # Adjust # for how many runs you want to do during testing minus 1
    # count += 1
    #feature.boost_equipment()
    #feature.ygg()
    #feature.snipe(0, 120, bosses=False)

    #time.sleep(120)
    # c.start_challenge(3)
    # print(count)
    speedrun(3, feature, alt_features, i)
    # challenger()
Discord.send_message(('Run done, check if challenge complete!'), Discord.ERROR)
