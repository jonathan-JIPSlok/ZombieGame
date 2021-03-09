import pygame
import pygame_menu
from sys import exit
from random import randint

pygame.init()

Largura = 1280
Altura = 700
FPS = 30

#Drops
Municao_Drop = pygame.image.load('Img/DropMunicao.png')
Municao_Sound_1 = pygame.mixer.Sound('Sound/Municao1.ogg')
Municao_Sound_2 = pygame.mixer.Sound('Sound/Municao2.ogg')

#Skills
SkillImg_ThreeKill = pygame.image.load('Img/ThreeKillSkill.png')
SkillSound_ThreeKill = pygame.mixer.Sound('Sound/ThreeKillSkill.ogg')

SkillImg_Caboom = pygame.image.load('Img/CaboomSkill.png')
SkillSound_Caboom = pygame.mixer.Sound('Sound/CaboomSkill.ogg')

SkillImg_Life_1Porcent = pygame.image.load('Img/Life1PorcentSkill.png')
SkillSound_1Porcent = pygame.mixer.Sound('Sound/1PorcentSkill.ogg')

#Imagens zombie andando 
ImgZombie_Lado_Direito = pygame.image.load('Img/Zombie/Zombie_D.png')
ImgZombie_Lado_D_Passo1 = pygame.image.load('Img/Zombie/Zombie_D_Passo1.png')
ImgZombie_Lado_D_Passo2 = pygame.image.load('Img/Zombie/Zombie_D_Passo2.png')

ImgZombie_Lado_Esquerdo =  pygame.image.load('Img/Zombie/Zombie_E.png')
ImgZombie_Lado_E_Passo1 = pygame.image.load('Img/Zombie/Zombie_E_Passo1.png')
ImgZombie_Lado_E_Passo2 = pygame.image.load('Img/Zombie/Zombie_E_Passo2.png')

#Imagen da bala
ImgBala = pygame.image.load('Img/Bala.png')

#Imagens andando
Player_Lado_Direito = pygame.image.load('Img/Player/Player_D.png')
ImgPlayer_Lado_D_Passo1 = pygame.image.load('Img/Player/Player_D_Passo1.png')
ImgPlayer_Lado_D_Passo2 = pygame.image.load('Img/Player/Player_D_Passo2.png')

Player_Lado_Esquerdo = pygame.image.load('Img/Player/Player_E.png')
ImgPlayer_Lado_E_Passo1 = pygame.image.load('Img/Player/Player_E_Passo1.png')
ImgPlayer_Lado_E_Passo2 = pygame.image.load('Img/Player/Player_E_Passo2.png')

#Imagens dando Facada
ImgPlayer_Facada_D1 = pygame.image.load('Img/Player/Player_D_Facada1.png')
ImgPlayer_Facada_D2 = pygame.image.load('Img/Player/Player_D_Facada2.png')
ImgPlayer_Facada_D3 = pygame.image.load('Img/Player/Player_D_Facada3.png')
ImgPlayer_Facada_D4 = pygame.image.load('Img/Player/Player_D_Facada4.png')

ImgPlayer_Facada_E1 = pygame.image.load('Img/Player/Player_E_Facada1.png')
ImgPlayer_Facada_E2 = pygame.image.load('Img/Player/Player_E_Facada2.png')
ImgPlayer_Facada_E3 = pygame.image.load('Img/Player/Player_E_Facada3.png')
ImgPlayer_Facada_E4 = pygame.image.load('Img/Player/Player_E_Facada4.png')

#Imagens Zombie Atacando
ImgZombie_Atacando_E1 = pygame.image.load('Img/Zombie/Zombie_E_Atack1.png')
ImgZombie_Atacando_E2 = pygame.image.load('Img/Zombie/Zombie_E_Atack2.png')

ImgZombie_Atacando_D1 = pygame.image.load('Img/Zombie/Zombie_D_Atack1.png')
ImgZombie_Atacando_D2 = pygame.image.load('Img/Zombie/Zombie_D_Atack2.png')

#Animacoes
Animacoes = [[ImgPlayer_Lado_D_Passo1,ImgPlayer_Lado_D_Passo2, ImgPlayer_Lado_D_Passo1, Player_Lado_Direito],\
 [ImgPlayer_Lado_E_Passo1, ImgPlayer_Lado_E_Passo2, Player_Lado_Esquerdo]]
 
Zombie_Animacoes = [[ImgZombie_Lado_D_Passo1, ImgZombie_Lado_D_Passo2, ImgZombie_Lado_Direito],\
 [ImgZombie_Lado_E_Passo1, ImgZombie_Lado_E_Passo2, ImgZombie_Lado_Esquerdo]]
 
Player_Facada = [[ImgPlayer_Facada_D1, ImgPlayer_Facada_D2, ImgPlayer_Facada_D3, ImgPlayer_Facada_D4, Player_Lado_Direito],
 [ImgPlayer_Facada_E1, ImgPlayer_Facada_E2, ImgPlayer_Facada_E3, ImgPlayer_Facada_E4, Player_Lado_Esquerdo]]
 
Zombie_Mordida = [[ImgZombie_Atacando_D1, ImgZombie_Atacando_D2, ImgZombie_Atacando_D1, ImgZombie_Lado_Direito],\
 [ImgZombie_Atacando_E1, ImgZombie_Atacando_E2, ImgZombie_Atacando_E1, ImgZombie_Lado_Esquerdo]]

Img_Background = pygame.image.load('Img/Background.png')

Tela = pygame.display.set_mode((Largura, Altura))
pygame.display.set_caption('ZombieGame')
pygame.display.set_icon(pygame.image.load('Img/GameIcon.ico'))
ImgBackground = Img_Background.convert()

class SpawnEnemyes():
	def __init__(self):
		pass
	
	def gerar(self, Round):
		self.ListaEnemyes = []
		Sortido = (randint(2, 5) * Round)
		cont = 0
		for x in range(0, (Sortido if Sortido <= 40 else 40)):
			if Sortido > 10 and Sortido < 30:
				self.ListaEnemyes.append(Zombie(randint(1300, 3700), randint(220, 500), Round))
			elif Sortido >= 30:
				self.ListaEnemyes.append(Zombie(randint(1300, 5700), randint(220, 500), Round))
			else:
				self.ListaEnemyes.append(Zombie(randint(1300, 1700), randint(220, 500), Round))
			if cont == 10:
				break
		return self.ListaEnemyes
			
class Zombie(pygame.sprite.Sprite):
	def __init__(self, posy, posx, round):
		pygame.sprite.Sprite.__init__(self)
		
		self.Img = ImgZombie_Lado_Direito.convert()
		self.rect = self.Img.get_rect()
		
		self.rect.left = posy
		self.rect.top = posx
		
		self.Velocidade = 1
		self.Vida = 10
		
		if round <= 5:
			self.Vida = 10
		elif round <= 10:
			self.Vida = 15
		elif round <= 20:
			self.Vida = 25
		elif round <= 40:
			self.Vida = 60
		elif round <= 100:
			self.Vida = 80
		else: self.Vida = 100
		
		self.Drop = False
		
		self.Move = 0
		self.Move_Atack = 0
		self.Atack = False
		
	def colocar(self, superficie):
		superficie.blit(self.Img, self.rect)
	def andar(self, Jogador):
		if self.Atack == False:
			if Jogador.rect.left > self.rect.left + 100:
				self.rect.left += self.Velocidade
				self.Img = Zombie_Animacoes[0][int(self.Move/10)]
				self.Move += 1
			elif Jogador.rect.left < self.rect.left -100:
				self.rect.left -= self.Velocidade
				self.Img = Zombie_Animacoes[1][int(self.Move/10)]
				self.Move -= 1
			if Jogador.rect.left + 120 >= self.rect.left and Jogador.rect.left - 120 <= self.rect.left:
				if Jogador.rect.top > self.rect.top:
					self.rect.top += self.Velocidade
					if Jogador.Lado_Player == 0:
						self.Img = Zombie_Animacoes[1][int(self.Move/10)]
						self.Move -= 1
					elif Jogador.Lado_Player == 1:
						self.Img = Zombie_Animacoes[0][int(self.Move/10)]
						self.Move += 1
				elif Jogador.rect.top < self.rect.top:
					self.rect.top -= self.Velocidade
					if Jogador.Lado_Player == 0:
						self.Img = Zombie_Animacoes[1][int(self.Move/10)]
						self.Move -= 1
					elif Jogador.Lado_Player == 1:
						self.Img = Zombie_Animacoes[0][int(self.Move/10)]
						self.Move += 1
				elif Jogador.rect.left < self.rect.left and Jogador.rect.top == self.rect.top:
					self.Img = Zombie_Animacoes[1][int(2)]
				elif Jogador.rect.left > self.rect.left and Jogador.rect.top == self.rect.top:
					self.Img = Zombie_Animacoes[0][int(2)]
	
	def AnimacaoAtack(self, Jogador):
		self.Atack = True
		self.Img = Zombie_Mordida[(0 if Jogador.rect.left > self.rect.left else 1)][int(self.Move_Atack / 10)]
		self.Move_Atack += (3 if FPS == 30 else 1)
				
class Bala(pygame.sprite.Sprite):
	def __init__(self, posx, posy):
		pygame.sprite.Sprite.__init__(self)
		
		self.ImgBala = ImgBala.convert()
		self.rect = self.ImgBala.get_rect()
		
		self.rect.top = posy
		self.rect.left = posx
		
		self.Velocidade = 90
		
	def colocar(self, superficie):
		superficie.blit(self.ImgBala, self.rect)
	def Trajetoria(self, lado):
		if lado == 0:
			self.rect.left += self.Velocidade
		elif lado == 1:
			self.rect.left -= self.Velocidade


class Player(pygame.sprite.Sprite):
	def __init__(self, posx, posy):
		pygame.sprite.Sprite.__init__(self)
		
		self.Lado_Player = 0
		
		self.Img = self.PlayerLado(0)
		self.rect = self.Img.get_rect()
		
		self.TiroSound = pygame.mixer.Sound('Sound/Tiro_1.wav')
		self.RecarregarSound = pygame.mixer.Sound('Sound/Recarregar_3.wav')
		
		self.rect.top = posy
		self.rect.left = posx
		
		self.Municao = 30
		self.Municao_Pente = 10
		self.Lista_BalasDisparadas = []
		
		self.MoveFacada = 0
		self.Facada = False
		
		self.Cont_Kill = 0
		
		(self.Sound_SkillThreeKill, self.Sound_SkillCaboom, self.Sound_Skill1Porcent) = (True, True, True)
		(self.Skill_ThreeKill_select, self.Skill_Caboom_select, self.Skill_Life1Porcent_select) = (False, False, False)
		(self.Skill_ThreeKill, self.Skill_Caboom, self.Skill_Life1Porcent) = (False, False, False)
		
		self.Vida = 100
		
		self.Velocidade = (3 if FPS == 30 else 1)
		
	def colocar(self,superficie):
		superficie.blit(self.Img, self.rect)
	
	def PlayerLado(self, move):
		move = int(move/10)
		
		try:
			return Animacoes[self.Lado_Player][move]
		except:
			return Animacoes[0][3]
	def Disparar(self):
		if self.Municao_Pente > 0:
			self.Municao_Pente -= 1
			if self.Lado_Player == 0:
				self.Lista_BalasDisparadas.append((Bala(self.rect.left + 100, self.rect.top + 65), self.TiroSound.play()))
			elif self.Lado_Player == 1:
				self.Lista_BalasDisparadas.append((Bala(self.rect.left -8, self.rect.top + 65), self.TiroSound.play()))
	
	def Animacao_Facada(self):
		self.MoveFacada += (5 if FPS == 30 else 1)
		self.Img = Player_Facada[self.Lado_Player][int(self.MoveFacada / 10)]
		if self.MoveFacada / 10 >= 3.9:
			return True
		else: return False
		
	def EfetuarFacada(self, enemie):
		
		Inimigo_Y = enemie.rect.left
		Jogador_Y = self.rect.left
		Distancia = Jogador_Y - Inimigo_Y
		
		if self.Lado_Player == 0:
			if Distancia <= 0 and Distancia >= -120 and self.rect.top == enemie.rect.top:
				enemie.Vida -= 4
	
		elif self.Lado_Player == 1:
			if Distancia >= 20 and Distancia <= 130 and self.rect.top == enemie.rect.top:
				enemie.Vida -= 4
				
	def Recarregar(self):
		if self.Municao_Pente < 10 and self.Municao > 0:
			for x in range(0, 10):
				if self.Municao > 0:
					self.Municao_Pente += 1
					self.Municao -= 1
				if self.Municao_Pente == 10:
					break
			self.RecarregarSound.play()
			
class Menu():
	def __init__(self):
		(self.Skill_1, self.Skill_2, self.Skill_3) = (1, 2, 3)
		
		menu = pygame_menu.Menu(Altura, Largura, "ZombieGame", theme=pygame_menu.themes.THEME_DARK)
		
		menu.add_button('Play', self.Main).set_background_color((155, 255, 190), (20, 10))
		menu.add_button('Skills', self.Skills_Select)
		menu.add_button('Opcoes', self.Opcoes)
		menu.add_button('Quit', exit)
		menu.add_label('')
		menu.add_label('Criado por JIPSlok (Created By JIPSlok) Versão: 0.5.0')
		
		menu.mainloop(Tela)
	
	def Skills_Select(self):
		menu = pygame_menu.Menu(Altura, Largura, "Skills", theme=pygame_menu.themes.THEME_DARK)
		
		menu.add_label('Skills são abilidades adiquiridas ao matar uma certa quantidade de inimigos')
		menu.add_label('')
		self.Skill_1 = menu.add_selector('Skill 1: ', [('ThreeKill', 1), ('Caboom', 2), ('Life 1%', 3)]).set_background_color((255, 000, 00))
		self.Skill_2 = menu.add_selector('Skill 2: ', [('Caboom', 2), ('ThreeKill', 1), ('Life 1%', 3)]).set_background_color((255, 0, 00))
		self.Skill_3 = menu.add_selector('Skill 3: ', [('Life 1%', 3), ('ThreeKill', 1), ('Caboom', 2)]).set_background_color((255, 0, 00))
		menu.add_label('')
		menu.add_label('ThreeKill = Mata 3 inimigos no round liberado apos 5 kills')
		menu.add_label('Caboom = Mata todos os inimigos no round liberado apos 40 kills')
		menu.add_label('Life 1% = deixa todos os inimigos no round com 1 de vida liberado apos 30 kills')
		
		menu.add_button('Voltar', menu.disable).set_background_color((100, 255, 100))
		
		menu.mainloop(Tela)
	
	def Main(self):
		
		Jogador = Player(0, 500)
		
		try:
			FPS = int(self.Player_FPS.get_value()[0])
		except:
			FPS = 30
		try:
			if self.Skill_1.get_value()[1] == 1 or self.Skill_2.get_value()[1] == 1 or self.Skill_3.get_value()[1] == 1:
				Jogador.Skill_ThreeKill_select = True
				print('skillThree ok')
			if self.Skill_1.get_value()[1] == 2 or self.Skill_2.get_value()[1] == 2 or self.Skill_3.get_value()[1] == 2:
				Jogador.Skill_Caboom_select = True
				print('Skill cabom ok')
			if self.Skill_1.get_value()[1] == 3 or self.Skill_2.get_value()[1] == 3 or self.Skill_3.get_value()[1] == 3:
				Jogador.Skill_Life1Porcent_select = True
				print('Skill 1% ok')
			
		except:
			if self.Skill_1 == 1 or self.Skill_2 == 1 or self.Skill_3 == 1:
				Jogador.Skill_ThreeKill_select = True
				print('skillThree ok')
			if self.Skill_1 == 2 or self.Skill_2 == 2 or self.Skill_3 == 2:
				Jogador.Skill_Caboom_select = True
				print('Skill cabom ok')
			if self.Skill_1 == 3 or self.Skill_2 == 3 or self.Skill_3 == 3:
				Jogador.Skill_Life1Porcent_select = True
				print('Skill 1% ok')
		
		move = 0
		
		(self.Andar_D, self.Andar_E, self.Andar_C, self.Andar_B, self.Atirar, self.Facada) = (False, False, False, False, False, False)
		
		self.Pause = False
		TempoDescansso_round = 0
		Tempo_Facada = 3
		
		Round = 1
		Primary_round = False
		
		pygame.font.init()
		font = pygame.font.get_default_font()
		font_Rounds = pygame.font.SysFont(font, 30)
		
		Enemyes = SpawnEnemyes()
		ListaEnemyes = []
		Lista_DropMunicao = []
		
		Timer = pygame.time.Clock()
		
		Tempo = 0
		
		while True:
			try:
				FPS = int(self.Player_FPS.get_value()[0])
			except:
				FPS = 30
			if self.Pause == False:
				(Posicao_AnteriorY, Posicao_AnteriorX) = (Jogador.rect.left, Jogador.rect.top)
				
				for event in pygame.event.get():
					if event.type == pygame.QUIT:
						pygame.quit()
						exit()
					if event.type == pygame.KEYDOWN:
						if event.key == pygame.K_r:
							Jogador.Recarregar()
							Tempo = 0
						if event.key == pygame.K_v:
							self.Atirar = True
						if event.key == pygame.K_d:
							self.Andar_D = True
						if event.key == pygame.K_a:
							self.Andar_E = True
						if event.key == pygame.K_w:
							self.Andar_C = True
						if event.key == pygame.K_s:
							self.Andar_B = True
						if event.key == pygame.K_e and Jogador.Vida > 0 and (Tempo_Facada == 10 if FPS == 30 else Tempo_Facada == 8*3) and self.Atirar == False:
							self.Facada = True
						if event.key == pygame.K_ESCAPE and Jogador.Vida > 0:
							self.Menu_Pause()
						if event.key == pygame.K_q:
							
							if len(ListaEnemyes) >= 3 and Jogador.Skill_ThreeKill == True:
								cont = 0
								numbers = [0, 1, 2]
								for x in ListaEnemyes:
									if cont in numbers:
										ListaEnemyes.remove(x)
									cont += 1
								Jogador.Skill_ThreeKill = False
								Jogador.Cont_Kill -= 5
								Jogador.Sound_SkillThreeKill = True
							
							if len(ListaEnemyes) >= 1 and Jogador.Skill_Life1Porcent == True:
								for x in ListaEnemyes:
									x.Vida = 1
								Jogador.Skill_Life1Porcent = False
								Jogador.Cont_Kill -= 30
								Jogador.Sound_Skill1Porcent = True
								
							if len(ListaEnemyes) >= 1 and Jogador.Skill_Caboom == True:
								for x in ListaEnemyes:
									ListaEnemyes = []
								Jogador.Skill_Caboom = False
								Jogador.Cont_Kill -= 40
								Jogador.Sound_SkillCaboom = True
							
							
					if event.type == pygame.KEYUP:
						if event.key == pygame.K_v:
							self.Atirar = False
						if event.key == pygame.K_d:
							self.Andar_D = False
							Jogador.Img = Jogador.PlayerLado(30)
						if event.key == pygame.K_a:
							self.Andar_E = False
							Jogador.Img = Jogador.PlayerLado(20)
						if event.key == pygame.K_w:
							self.Andar_C = False
						if event.key == pygame.K_s:
							self.Andar_B = False
							
				if self.Atirar == True and Tempo == (10 if FPS == 30 else 8*3) and Jogador.Vida > 0 and Jogador.Municao_Pente > 0:
					Jogador.Disparar()
				elif self.Atirar == True and Tempo == (10 if FPS == 30 else 8*3) and Jogador.Vida > 0:
					Jogador.Recarregar()
				if self.Andar_D == True and Jogador.Vida > 0 and self.Andar_E == False:
					Jogador.rect.left += Jogador.Velocidade
					Jogador.Lado_Player = 0
					move += 1
					Jogador.Img = Jogador.PlayerLado(move)
				if self.Andar_E == True and Jogador.Vida > 0 and self.Andar_D == False:
					Jogador.rect.left -= Jogador.Velocidade
					Jogador.Lado_Player = 1
					Jogador.Img = Jogador.PlayerLado(move)
					move -= 1
				if self.Andar_C == True and Jogador.Vida > 0:
					Jogador.rect.top -= Jogador.Velocidade
					move = 10
				if self.Andar_B == True and Jogador.Vida > 0:
					Jogador.rect.top += Jogador.Velocidade
					move = 0
				if self.Facada == True and Jogador.Vida > 0:
					if len(Enemyes.ListaEnemyes) > 0:
						Jogador.Facada = True
						Facada_Resultado = Jogador.Animacao_Facada()
						
						if Facada_Resultado:
							for Inimigo in Enemyes.ListaEnemyes:
								self.Facada = Jogador.EfetuarFacada(Inimigo)
								Tempo_Facada = 0
								if Inimigo.Vida <= 0:
									Random_Bala = randint(1, 6)
									if Random_Bala == 3:
										Inimigo.rect.top += 100
										Inimigo.Img = Municao_Drop.convert()
										Lista_DropMunicao.append(Inimigo)
									Enemyes.ListaEnemyes.remove(Inimigo)
									Jogador.Cont_Kill += 1
									
							self.Facada == False
							Facada_Resultado = Jogador.Animacao_Facada()
				
				if move > 19:
					move = 0
				if move < 0:
					move = 19
				
				if Jogador.MoveFacada / 10 >= 4.0:
					Jogador.MoveFacada = 0

				
				Round_Enemyes_Text = font_Rounds.render(f'Round: {Round}    Enemyes: {len(ListaEnemyes)}', 1, (0, 0, 255))
				Player_Vida_Text = font_Rounds.render(f'Fps: {int(Timer.get_fps())}', 1, (0, 0, 0))
				Player_Municao_Text = font_Rounds.render(f'Munição: {Jogador.Municao}    Pente: {Jogador.Municao_Pente}', 1, (0, 0, 255))
				Player_Derrota_Text = font_Rounds.render(f'Você Perdeu!', 1, (255, 0, 0))
				PlayerVida_text = font_Rounds.render(f'Vida: {Jogador.Vida}', 1, (255, 0, 0))
				
				Tela.blit(ImgBackground, (0, 0))
				Tela.blit(Round_Enemyes_Text, (0, 0))
				Tela.blit(Player_Vida_Text, (800, 0))
				Tela.blit(Player_Municao_Text, (500, 0))
				Tela.blit(PlayerVida_text, (Jogador.rect.left + 10, Jogador.rect.top - 20))
				
				if Jogador.rect.top <= 240:
					(Jogador.rect.left, Jogador.rect.top) = (Posicao_AnteriorY, Posicao_AnteriorX)
				elif Jogador.rect.top >= Altura - 90:
					(Jogador.rect.left, Jogador.rect.top) = (Posicao_AnteriorY, Posicao_AnteriorX)
				elif Jogador.rect.left >= Largura - 90:
					(Jogador.rect.left, Jogador.rect.top) = (Posicao_AnteriorY, Posicao_AnteriorX)
				elif Jogador.rect.left <= 0:
					(Jogador.rect.left, Jogador.rect.top) = (Posicao_AnteriorY, Posicao_AnteriorX)
				
				if Jogador.Vida > 0:
					Jogador.colocar(Tela)
				else:
					Jogador.Vida = 0
				
				if len(ListaEnemyes) > 0:
					for inimigo in ListaEnemyes:
						if inimigo.Drop == False:
							if inimigo.Move > 19:
								inimigo.Move = 0
							if inimigo.Move < 0:
								inimigo.Move = 19
							inimigo.colocar(Tela)
							inimigo.andar(Jogador)
							ZombieMove = inimigo.Move
				
				for Municao in Lista_DropMunicao:
					if Jogador.rect.colliderect(Municao):
						Lista_DropMunicao.remove(Municao)
						(Municao_Sound_1.play() if randint(0, 10) % 2 == 0 else Municao_Sound_2.play())
							
						Jogador.Municao += 10
					Municao.colocar(Tela)
				
				if len(Jogador.Lista_BalasDisparadas) > 0:
					for bala in Jogador.Lista_BalasDisparadas:
						bala[0].colocar(Tela)
						bala[0].Trajetoria(Jogador.Lado_Player)
						bala[1]
						if len(ListaEnemyes) > 0:
							for inimigo in ListaEnemyes:
								if bala[0].rect.colliderect(inimigo.rect) and bala in Jogador.Lista_BalasDisparadas:
									Forca_Bala = [3, 5, 3, 3, 3, 3, 3, 3, 3, 5 ,3 ,3 ,5, 5, 100]
									inimigo.Vida -= Forca_Bala[randint(0, 14)]
									Jogador.Lista_BalasDisparadas.remove(bala)
									if inimigo.Vida <= 0:
										Random_Bala = randint(1, 6)
										if Random_Bala == 3:
											inimigo.rect.top += 100
											inimigo.Img = Municao_Drop.convert()
											Lista_DropMunicao.append(inimigo)
											
										ListaEnemyes.remove(inimigo)
										Jogador.Cont_Kill += 1
							
							if bala[0].rect.left > 1280 and bala in Jogador.Lista_BalasDisparadas: Jogador.Lista_BalasDisparadas.remove(bala)
							if bala[0].rect.left < 0 and bala in Jogador.Lista_BalasDisparadas: Jogador.Lista_BalasDisparadas.remove(bala)
						
				if len(ListaEnemyes) > 0:
					cont_Lista_1 = 0
					cont_Lista_2 = 0
					for Enemye in ListaEnemyes:
						EnemyVida = font_Rounds.render(f'Vida: {Enemye.Vida}', 1, (255, 0, 0))
						Tela.blit(EnemyVida, (Enemye.rect.left + 30, Enemye.rect.top-20))
						
						if Enemye.Move_Atack / 10 > 3.9:
							Enemye.Move_Atack = 0
						
						if Jogador.rect.left <= Enemye.rect.left + 100 and Jogador.rect.left + 100 > Enemye.rect.left and Jogador.Vida > 0:
							if (Jogador.rect.top - Enemye.rect.top) < 50 and (Jogador.rect.top - Enemye.rect.top) > -50:
								Enemye.AnimacaoAtack(Jogador)
								if Enemye.Move_Atack / 10 >= 3.9 and Enemye.Move_Atack / 10 <= 4.0:
									Jogador.Vida -= 1
									Enemye.Atack = False
							else:
								Enemye.Atack = False
						elif Jogador.rect.left >= Enemye.rect.left - 100 and Jogador.rect.left - 100 < Enemye.rect.left and Jogador.Vida > 0:
							if (Jogador.rect.top - Enemye.rect.top) < 50 and (Jogador.rect.top - Enemye.rect.top) > -50:
								Enemye.AnimacaoAtack(Jogador)
								if Enemye.Move_Atack / 10 >= 3.9 and Enemye.Move_Atack / 10 <= 4.0:
									Jogador.Vida -= 1
									Enemye.Atack = False
							else: Enemye.Atack = False
						elif (Jogador.rect.left - Enemye.rect.left) > 100 or (Jogador.rect.left - Enemye.rect.left) < -100:
							Enemye.Atack = False
							Enemye.Move_Atack = 0
									
						for Enemye2 in ListaEnemyes:
							if cont_Lista_2 == cont_Lista_1:
								pass
							else:
								if Enemye.rect.colliderect(Enemye2.rect):
									Enemye.rect.top -= (2 if FPS == 30 else 2/2)
									Enemye2.rect.top += (2 if FPS == 30 else 2/2)
									if Enemye.rect.top <= 240:
										Enemye.rect.top += (1 if FPS == 30 else 1/3)
										Enemye.rect.left += (1 if FPS == 30 else 1/3)
									
							cont_Lista_2 += 1
						cont_Lista_2 = 0
						cont_Lista_1 += 1
				
				#Sound Skill
				if Jogador.Cont_Kill == 5 and Jogador.Skill_ThreeKill_select == True and Jogador.Sound_SkillThreeKill == True:
					SkillSound_ThreeKill.play()
					Jogador.Sound_SkillThreeKill = False
				if Jogador.Cont_Kill == 30 and Jogador.Skill_Life1Porcent_select == True and Jogador.Sound_Skill1Porcent == True:
					SkillSound_1Porcent.play()
					Jogador.Sound_Skill1Porcent = False
				if Jogador.Cont_Kill == 40 and Jogador.Skill_Caboom_select == True and Jogador.Sound_SkillCaboom == True:
					SkillSound_Caboom.play()
					Jogador.Sound_SkillCaboom = False
				#Skill
				if Jogador.Cont_Kill >= 5 and Jogador.Skill_ThreeKill_select == True:
					Jogador.Skill_ThreeKill = (True if Jogador.Cont_Kill < 30 else False)
					Tela.blit(SkillImg_ThreeKill, (620, 670))
					
				if Jogador.Cont_Kill >= 30 and Jogador.Skill_Life1Porcent_select == True:
					Jogador.Skill_Life1Porcent = (True if Jogador.Cont_Kill < 40 else False)
					Tela.blit(SkillImg_Life_1Porcent, (620, 670))
					
				if Jogador.Cont_Kill >= 40 and Jogador.Skill_Caboom_select == True:
					Jogador.Skill_Caboom = True
					Tela.blit(SkillImg_Caboom, (620, 670))
					
				if Round == 1 and Primary_round == False:
					ListaEnemyes = Enemyes.gerar(Round)
					Primary_round = True
				elif len(ListaEnemyes) == 0:
					if TempoDescansso_round < 100:
						TempoDescansso_round += 1
					else:
						Round += 1
						ListaEnemyes = Enemyes.gerar(Round)
						TempoDescansso_round = 0
						Jogador.Municao += 10
						
				if Tempo == (10 if FPS == 30 else 8*3):
					Tempo = 0
				else:
					Tempo += 1
				if Tempo_Facada < (10 if FPS == 30 else 8*3):
					Tempo_Facada += 1
					
				if Jogador.Vida == 0:
					Tela.blit(Player_Derrota_Text, (500, 450))
					
				pygame.display.flip()
				Timer.tick(FPS)
		
	def Menu_Pause(self):
		self.Pause = True
		(self.Andar_D, self.Andar_E, self.Andar_C, self.Andar_B, self.Atirar) = (False, False, False, False, False)
		self.menuPause = pygame_menu.Menu(Altura, Largura, "ZombieGame", theme=pygame_menu.themes.THEME_DARK)
		
		self.menuPause.add_button('Voltar', self.ContinuarGame)
		self.menuPause.add_button('Opcoes', self.Opcoes)
		self.menuPause.add_button('Reiniciar', self.Main)
		self.menuPause.add_button('Quit', exit)
		
		self.menuPause.mainloop(Tela)
	def ContinuarGame(self):
	
		self.Pause = False
		self.menuPause.disable()
		
	def Opcoes(self):
		opcoes = pygame_menu.Menu(Altura, Largura, "ZombieGame", theme=pygame_menu.themes.THEME_DARK)
		
		self.Player_FPS = opcoes.add_selector('FPS: ', [('30', 1), ('60', 2)])
		opcoes.add_button('Voltar', opcoes.disable)
		
		opcoes.mainloop(Tela)
Game = Menu()