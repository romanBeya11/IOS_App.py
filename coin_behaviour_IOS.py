from scene import *
import sound
import random
import math
A = Action

class Coin_Behaviour (Scene):
	def setup(self):
		
		# Setting up the background
		self.screen_center_x = self.size.x / 2
		self.screen_center_y = self.size.y / 2
		# Setting up the background
		self.screen_center_x = self.size.x / 2
		self.screen_center_y = self.size.y / 2
		self.bg_pos = Vector2(self.screen_center_x, self.screen_center_y)
		background = SpriteNode(color = '#a5acf7', position = self.bg_pos, parent = self, size = self.size)
		
		# Boundary Detection
		# Setting the ground height
		self.height_of_ground = 35
		# Setting the top of screen boundary
		self.top_of_screen_boundary = 750
		# Left side of screen
		self.left_side_of_screen_boundary = self.screen_center_x - 480
		# Right side of screen
		self.right_side_of_screen_boundary = 980
		
		self.create_new_coin()
		
		# Creating player sprite
		self.player_position = Vector2()
		self.player_position.x = self.screen_center_x - 200
		self.player_position.y = self.screen_center_y - 200
		self.player = SpriteNode('plf:HudPlayer_pink', position = self.player_position, parent = self, size = self.size / 10)
		
		self.score_label = Vector2()
		self.score_label.x = 700
		self.score_label.y = 700
		self.score = LabelNode(text = "Score: 0", position = self.score_label, parent = self, font = ("Copperplate", 40))
		
		'''self.special_box_pos = Vector2()
		self.special_box_pos.x = random.randint(self.left_side_of_screen_boundary, self.right_side_of_screen_boundary)
		self.special_box_pos.y = random.randint(self.height_of_ground, self.score_label.y - 30)
		self.special_box = SpriteNode('plf:Tile_BoxItem_boxed', position = self.special_box_pos, parent = self, size = self.size / 15)'''
		self.special_boxes()
		self.show_hearts()
		self.create_new_enemy()
		
		# HIT COUNTER FOR COINS
		self.coin_intersect = 0
		
		# HIT COUNTER FOR ENEMIES
		self.enemy_cross_path = 0
		
	def did_change_size(self):
		pass
		
	def show_hearts(self):
		self.heart_sprite = Vector2()
		self.heart_sprite.x = 200
		self.heart_sprite.y = 700
		self.heart = SpriteNode('plf:HudHeart_full', position = self.heart_sprite, parent = self, size = self.size / 14)
		self.heart_sprite = Vector2()
		self.heart_sprite.x = 270
		self.heart_sprite.y = 700
		self.heart = SpriteNode('plf:HudHeart_full', position = self.heart_sprite, parent = self, size = self.size / 14)
		self.heart_sprite = Vector2()
		self.heart_sprite.x = 340
		self.heart_sprite.y = 700
		self.heart = SpriteNode('plf:HudHeart_full', position = self.heart_sprite, parent = self, size = self.size / 14)
		
	def create_new_enemy(self):
		self.enemy_pos = Vector2()
		#self.enemy_pos.x = random.randint(self.left_side_of_screen_boundary, self.right_side_of_screen_boundary)
		self.enemy_pos.x = random.randint(self.left_side_of_screen_boundary, self.right_side_of_screen_boundary)
		self.enemy_pos.y = random.randint(self.height_of_ground, self.top_of_screen_boundary)
		self.enemy = SpriteNode('plf:Enemy_Saw_move', position = self.enemy_pos, parent = self, size = self.size / 8) 
		#self.enemy.run_action(Action.move_by(self.enemy_pos.x, self.enemy_pos.y, 20))
		#if self.enemy_pos >= self.right_side_of_screen_boundary:
			#self.enemy.run_action(Action.move_by(-1*self.right_side_of_screen_boundary, self.screen_center_y, 5))
			#self.enemy.run_action(Action.move_by(self.enemy_pos.x, self.enemy_pos.y, 20))
		#elif self.enemy_pos <= self.left_side_of_screen_boundary:
			#self.enemy.run_action(Action.move_by(self.enemy_pos.x, self.enemy_pos.y, 20))
		
	def special_boxes(self):
		self.special_box_pos = Vector2()
		self.special_box_pos.x = random.randint(self.left_side_of_screen_boundary, self.right_side_of_screen_boundary)
		self.special_box_pos.y = random.randint(self.height_of_ground, self.score_label.y - 30)
		self.special_box = SpriteNode('plf:Tile_BoxItem_boxed', position = self.special_box_pos, parent = self, size = self.size / 15, alpha = 0)
		#self.special_box_intersection()
		
	def create_new_heart(self, x, y):	
		self.heart_sprite = Vector2()
		self.heart_sprite.x = x
		self.heart_sprite.y = y
		self.heart = SpriteNode('plf:HudHeart_full', position = self.heart_sprite, parent = self, size = self.size / 14)
		
	def special_box_intersection(self):
		if self.player.frame.intersects(self.special_box.frame):
			self.create_new_heart(self.special_box_pos.x, self.special_box_pos.y)
			self.special_box.run_action(Action.fade_to(1, 2))
			
	def enemy_intersect(self):
		if self.player.frame.intersects(self.enemy.frame):
			self.enemy_cross_path = self.enemy_cross_path + 1
			#self.enemy.remove_from_parent()
			#self.create_new_enemy()
			self.heart.remove_from_parent()
			if self.enemy_cross_path == 1:
				self.special_box_intersection()
				self.heart_sprite1 = Vector2()
				self.heart_sprite1.x = 340
				self.heart_sprite1.y = 700
				self.heart1 = SpriteNode('plf:HudHeart_half', position = self.heart_sprite, parent = self, size = self.size / 14)
			elif self.enemy_cross_path == 2:
				self.heart1.remove_from_parent()
				self.heart_sprite2 = Vector2()
				self.heart_sprite2.x = 340
				self.heart_sprite2.y = 700
				self.heart2 = SpriteNode('plf:HudHeart_empty', position = self.heart_sprite, parent = self, size = self.size / 14)
			elif self.enemy_cross_path == 3:
				self.heart2.remove_from_parent()
			elif self.enemy_cross_path == 4:
				self.heart_sprite4 = Vector2()
				self.heart_sprite4.x = 270
				self.heart_sprite4.y = 700
				self.heart4 = SpriteNode('plf:HudHeart_half', position = self.heart_sprite, parent = self, size = self.size / 14)
			elif self.enemy_cross_path == 5:
				self.heart4.remove_from_parent()
				self.heart_sprite5 = Vector2()
				self.heart_sprite5.x = 200
				self.heart_sprite5.y = 700
				self.heart5 = SpriteNode('plf:HudHeart_empty', position = self.heart_sprite, parent = self, size = self.size / 14)
			elif self.enemy_cross_path == 6:
				self.heart5.remove_from_parent()
				#self.special_box_intersection()
				
	def increment_score(self):
		self.coin_intersect = self.coin_intersect + 1
		self.score.text = "Score: " + str(self.coin_intersect)
			
	def intiate_gravity(self):
		# GRAVITY STARTS HERE!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
		if self.player_position.y == self.height_of_ground:
			self.player_position.y = self.height_of_ground
		else:
			if self.player_position.y >= self.top_of_screen_boundary:
				self.player_position.y = self.top_of_screen_boundary
			if self.player_position.x >= self.right_side_of_screen_boundary:
				self.player_position.x = self.right_side_of_screen_boundary
			if self.player_position.x <= self.left_side_of_screen_boundary:
				self.player_position.x = self.left_side_of_screen_boundary
			
			# Find the distance between the ground and the players current pos
			distance_to_grnd = self.player_position.y - self.height_of_ground
			if distance_to_grnd <= self.height_of_ground + 20:
				descend = self.player_position.y = self.player_position.y - 8
				action = Action.move_to(self.player_position.x, descend)
				self.player.run_action(action)
				if descend <= self.height_of_ground:
					#self.player_position.x = self.screen_center_x
					self.player_position.y = self.height_of_ground
					#print 'reset NOW'
			elif distance_to_grnd >= self.height_of_ground + 100:
				descend = self.player_position.y = self.player_position.y - 4
				action = Action.move_to(self.player_position.x, descend)
				self.player.run_action(action)
				if descend <= self.height_of_ground:
					#self.player_position.x = self.screen_center_x
					self.player_position.y = self.height_of_ground
					#print 'reset NOW'
			else:
				descend = self.player_position.y = self.player_position.y - 2
				action = Action.move_to(self.player_position.x, descend)
				self.player.run_action(action)
				if descend <= self.height_of_ground:
					#self.player_position.x = self.screen_center_x
					self.player_position.y = self.height_of_ground
							
	def coin_to_player_intersection(self):
		if self.player.frame.intersects(self.coin.frame):
			self.coin.remove_from_parent()
			self.create_new_coin()
			self.increment_score()
			
	def create_new_coin(self):
		# Creating random positions for the coins
		random_coin_coordinate_x = random.randint(self.left_side_of_screen_boundary, self.right_side_of_screen_boundary)
		random_coin_coordinate_y = random.randint(self.height_of_ground, self.top_of_screen_boundary)
		self.coin_position = Vector2()
		self.coin_position.x = random_coin_coordinate_x
		self.coin_position.y = random_coin_coordinate_y
		self.coin = SpriteNode('plf:Item_CoinGold', position = self.coin_position, parent = self, size = self.size / 9) #/15
					
	def update(self):
		self.coin_to_player_intersection()
		self.intiate_gravity()
		self.enemy_intersect()
		self.special_box_intersection()
	def touch_began(self, touch):
		pass
	
	def touch_moved(self, touch):
		pass
	
	def touch_ended(self, touch):
		x = self.player_position.x = touch.location.x
		y = self.player_position.y = touch.location.y
		self.player.run_action(Action.move_by(x, y, 0.5)) 

if __name__ == '__main__':
	run(Coin_Behaviour(), show_fps = True)
