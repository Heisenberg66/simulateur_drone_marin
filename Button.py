import pygame

class Button(object):
	def __init__(self, txt):
		self._text = txt
		self.default_color = (0,255,0)
		self.font_color = (0,0,0)
		self.is_start = False
		self.obj = None

	def change_started_bool(self):
		if self.is_start:
			self.is_start=False
		else:
			self.is_start=True

	def check_is_started(self):
		return self.is_start

	def change_font_color(self,clr):
		self.font_color=clr

	def _set_text(self,txt):
		self._text=txt

	def _get_text(self):
		return self._text

	def change_appearance(self):
		if self.is_start:
			self.default_color=(255,0,0)
			self._text="STOP"
		else:
			self.default_color = (0,255,0)
			self._text="START"

	def change_default_color(self,clr):
		self.default_color=clr
	
	def label(self,size):
   		font = pygame.font.Font(None, size)
   		return font.render(self._text, 1, self.font_color)

	def draw(self, screen, rectcoord, labelcoord,size):
		self.obj  = pygame.draw.rect(screen, self.default_color, rectcoord)
		pygame.draw.rect(screen,(0,0,0),rectcoord,3)
		margin =0
		screen.blit(self.label(size), labelcoord)


	text=property(_get_text,_set_text)

