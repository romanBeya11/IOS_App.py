from scene import *
import sound
import random
import math
A = Action

class MyScene (Scene):
	def setup(self):
		self.show_hearts()
		self.enemy_cross_path = 0
	
	def did_change_size(self):
		pass
		
	def show_hearts(self):
		self.heart_sprite_1 = Vector2()
		self.heart_sprite_1.x = 200
		self.heart_sprite_1.y = 700
		self.heart_1 = SpriteNode('plf:HudHeart_full', position = self.heart_sprite_1, parent = self, size = self.size / 14)
		self.heart_sprite_2 = Vector2()
		self.heart_sprite_2.x = 270
		self.heart_sprite_2.y = 700
		self.heart_2 = SpriteNode('plf:HudHeart_full', position = self.heart_sprite_2, parent = self, size = self.size / 14)
		self.heart_sprite_3 = Vector2()
		self.heart_sprite_3.x = 340
		self.heart_sprite_3.y = 700
		self.heart_3 = SpriteNode('plf:HudHeart_full', position = self.heart_sprite_3, parent = self, size = self.size / 14)
		
	def heart(self):
		self.enemy_cross_path = self.enemy_cross_path + 1
		if self.enemy_cross_path == 1:
				self.heart_3.run_action(Action.fade_to(0, 1))
				self.heart_sprite_4 = Vector2()
				self.heart_sprite_4.x = 340
				self.heart_sprite_4.y = 700
				self.heart_4 = SpriteNode('plf:HudHeart_half', position = self.heart_sprite_4, parent = self, size = self.size / 14)
				sound.play_effect('rpg:Chop')
		elif self.enemy_cross_path == 2:
			#self.heart_2.run_action(Action.fade_to(0, 1))
			self.heart_4.run_action(Action.fade_to(0, 1))
			self.heart_sprite_5 = Vector2()
			self.heart_sprite_5.x = 340
			self.heart_sprite_5.y = 700
			self.heart_5 = SpriteNode('plf:HudHeart_empty', position = self.heart_sprite_5, parent = self, size = self.size / 14)
			sound.play_effect('rpg:Chop')
		elif self.enemy_cross_path == 3:
			self.heart_5.run_action(Action.fade_to(0, 1))
			sound.play_effect('rpg:Chop')
		elif self.enemy_cross_path == 4:
			self.heart_2.run_action(Action.fade_to(0, 1))
			self.heart_sprite_6 = Vector2()
			self.heart_sprite_6.x = 270
			self.heart_sprite_6.y = 700
			self.heart_6 = SpriteNode('plf:HudHeart_half', position = self.heart_sprite_6, parent = self, size = self.size / 14)
			sound.play_effect('rpg:Chop')
		elif self.enemy_cross_path == 5:
			self.heart_6.run_action(Action.fade_to(0, 1))
			self.heart_sprite_7 = Vector2()
			self.heart_sprite_7.x = 270
			self.heart_sprite_7.y = 700
			self.heart_7 = SpriteNode('plf:HudHeart_empty', position = self.heart_sprite_7, parent = self, size = self.size / 14)
		elif self.enemy_cross_path == 6:
			self.heart_7.run_action(Action.fade_to(0, 1))
		elif self.enemy_cross_path == 7:
			self.heart_1.run_action(Action.fade_to(0, 1))
			self.heart_sprite_8 = Vector2()
			self.heart_sprite_8.x = 200
			self.heart_sprite_8.y = 700
			self.heart_8 = SpriteNode('plf:HudHeart_half', position = self.heart_sprite_8, parent = self, size = self.size / 14)
		elif self.enemy_cross_path == 8:
			self.heart_8.run_action(Action.fade_to(0, 1))
			self.heart_sprite_9 = Vector2()
			self.heart_sprite_9.x = 200
			self.heart_sprite_9.y = 700
			self.heart_9 = SpriteNode('plf:HudHeart_empty', position = self.heart_sprite_9, parent = self, size = self.size / 14)
		elif self.enemy_cross_path == 9:
			self.heart_9.run_action(Action.fade_to(0, 1))
			
	def update(self):
		pass
	
	def touch_began(self, touch):
		self.heart()
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		pass

if __name__ == '__main__':
	run(MyScene(), show_fps=False)
