# coding: utf-8

"""
Prick - räkna prickarna
Version 0.1
Av: Jesper Svensson @jesperpsvensson

-----------------------

Spel för de mindre barnen som lär sig siffor
Räkna prickarna och välj motsvarande siffra
"""


import ui
import random
import sound
import time

starsdic = []
button_titles = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
tries = []
points = []

def check(sender):
	if str(sender.title) == str(len(starsdic)):
		sound.play_effect('game:Ding_3')
		add_points()
		del starsdic[:]
		set_stars()
		set_buttons() 
	else:
		sound.play_effect('Jump_5')
		decrease_life()
		
def restart_game(sender):
	if len(sender.superview['lifeLabel'].text) > 0:
		pass
	else:
		main()
		sender.superview['pointLabel'].text = '0'
		sender.title = ''
		
v = ui.load_view()

def set_stars():
	stars = ""
	stars_count = random.randrange(1, 11)
	stars_added = 0
	while stars_added < stars_count:
		stars += "•"
		stars_added += 1
		starsdic.append('1')
	v['astericsLabel'].text = stars

def set_lives():
	v['lifeLabel'].text = '❤️❤️❤️'
	
def decrease_life():
	if len(v['lifeLabel'].text) == 6:
		v['lifeLabel'].text = '❤️❤️'
	elif len(v['lifeLabel'].text) == 4:
		v['lifeLabel'].text = '❤️'
	else:
		v['lifeLabel'].text = ''
		v['astericsLabel'].text = 'Game Over'
		time.sleep(0.5)
		sound.play_effect('Piano_A3#')
		time.sleep(0.15)
 		sound.play_effect('Piano_A3')
 		time.sleep(0.15)
 		sound.play_effect('Piano_G3#')
 		time.sleep(0.2)
 		sound.play_effect('Piano_G3')
 		time.sleep(0.25)
 		sound.play_effect('Piano_F3#')
 		time.sleep(0.3)
 		sound.play_effect('Piano_F3')
 		time.sleep(0.35)
 		sound.play_effect('Piano_E3')
 		time.sleep(0.6)
 		sound.play_effect('Explosion_4')
 		v['replay'].title = 'Tryck här för att spela igen...'
 		del starsdic[:]
 		del points[:]
 	
def add_points():
	if len(v['lifeLabel'].text) == 6: 
		points.append(10)
		v['pointLabel'].text = str(sum(points))
	elif len(v['lifeLabel'].text) == 4:
		points.append(5)
		v['pointLabel'].text = str(sum(points))
	elif len(v['lifeLabel'].text) == 2:
		points.append(1)
		v['pointLabel'].text = str(sum(points))
	else:
		pass
	
def set_buttons():
	random.shuffle(button_titles)
	v['button1'].title = str(button_titles[0])
	v['button2'].title = str(button_titles[1])
	v['button3'].title = str(button_titles[2])
	v['button4'].title = str(button_titles[3])
	v['button5'].title = str(button_titles[4])
	v['button6'].title = str(button_titles[5])
	v['button7'].title = str(button_titles[6])
	v['button8'].title = str(button_titles[7])
	v['button9'].title = str(button_titles[8])
	v['button10'].title = str(button_titles[9])

def main():
	set_stars()
	set_lives()
	set_buttons()

main()
v.present('full_screen', hide_title_bar = True, orientations='portrait')
