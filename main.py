import keyboard as kb
import pyperclip as pc
import pyautogui as pg

ENG_TO_UA = {"q": 'й', "w": 'ц', "e": 'у', "r": 'к', "t": 'е', "y": 'н', "u": 'г', "i": 'ш', "o": 'щ', "p": 'з',
                 "[": 'х',
                 "]": 'ї', "a": 'ф', "s": 'і', "d": 'в', "f": 'а', "g": 'п', "h": 'р', "j": 'о', "k": 'л',
                 "l": 'д', ";": 'ж', "\'": 'є', "z": 'я', "x": 'ч', "c": 'с', "v": 'м', "b": 'и', "n": 'т', "m": 'ь',
                 ",": 'б', ".": 'ю', "/": '.'}

def change(eng):
    uasp = []
    for x in range(len(eng)):
          try:
             uasp.append(ENG_TO_UA[eng[x]])
          except:
                uasp.append(eng[x])
    ua = ''.join(uasp)
    return ua

def main():
    #pg.hotkey('ctrl', 'c')
    eng = pc.paste()
    ua = change(eng)
    pc.copy(ua)

def add():
    kb.add_hotkey('alt+shift+z', main)