import pyautogui
from time import sleep
from button_positions import HOME_PLAY_BUTTON, MAP_DIFFICULTYS, DIFFICULTYS, MODES, OVERWRITE_SAVE
from logger import Logger
from monkeys import monkeys, upgrades
from threading import Thread


Logger = Logger()

class Map():
    def __init__(self, map_name, map_difficulty, map_site, map_place, difficulty, mode):
        self.map_name = map_name
        self.map_difficulty = map_difficulty
        self.map_site = map_site
        self.map_place = map_place
        self.difficulty = difficulty
        self.mode = mode

    def select(self):
        time_to_home = 5
        Logger.log(f"Open home screen - {time_to_home} sec", "YELLOW")
        sleep(time_to_home)

        x, y = HOME_PLAY_BUTTON
        pyautogui.click(x, y)

        delay = 0.3
        for x in range(self.map_site):
            sleep(delay)
            x, y = self.map_difficulty
            pyautogui.click(x, y)
        
        sleep(delay)
        pyautogui.click(self.map_place)

        sleep(delay)
        pyautogui.click(self.difficulty)

        sleep(delay)
        pyautogui.click(self.mode)
        
        sleep(delay)
        pyautogui.click(OVERWRITE_SAVE)

    

    def place_monkey(self, key:str, pos:tuple, time_between:int=0.2):
        pyautogui.press(key)
        pyautogui.moveTo(pos[0], pos[1])
        sleep(time_between)
        pyautogui.click()

    def upgrade_monkey(self, pos:tuple, path):
        pyautogui.moveTo(pos[0], pos[1])
        pyautogui.click()
        pyautogui.press(upgrades[path])
        pyautogui.press("ESC")

    def play(self, game_plan):
        data = []
        for r in game_plan:
            data.append(r.split())
        
        
        for r in data:
            key = r[0].upper()
            if key == "PAUSE":
                Logger.log(f"Waiting for {r[1]} seconds", "GREEN")
                sleep(float(r[1]))

            elif key == "UPGRADE":
                self.upgrade_monkey((int(r[1]), int(r[2])), r[3])
                Logger.log(f"Upgraded monkey at x:{r[1]} y:{r[2]} with path:{r[3]}", "GREEN")

            elif key == "SPACE":
                pyautogui.press("SPACE")
                Logger.log(f"Used space", "GREEN")

            elif key == "ABILITY":
                pyautogui.press(r[1])
                Logger.log(f"Used ability {r[1]}", "GREEN")

            else:
                self.place_monkey(monkeys[r[0].upper()],(int(r[1]),int(r[2])))
                Logger.log(f"Placed {r[0]} at position x:{r[1]} y:{r[2]}", "GREEN")