import pygame


class UIManager():

    def __init__(self):
        self.font50 = pygame.font.Font('images/Oxanium-Bold.ttf', 50)
        self.font25 = pygame.font.Font('images/Oxanium-Bold.ttf', 25)
        self.font12 = pygame.font.Font('images/Oxanium-Bold.ttf', 12)

        self.score_string = 'Score:'
        self.lives_string = 'Lives:'

        self.score_text = None
        self.lives_text = None

        self.set_score()
        self.set_lives()

        self.border_distance = 30

    def set_score(self, score=0):
        self.score_text = self.font25.render(f'{self.score_string} {score}', True, 'gray')

    def set_lives(self, lives=0):
        self.lives_text = self.font25.render(f'{self.lives_string} {lives}', True, 'gray')

    def update_ui(self,score,lives):
        self.set_score(score)
        self.set_lives(lives)


    @staticmethod
    def get_border_rect(rect, pos):
        rect.centerx += pos[0]
        rect.centery += pos[1]
        rect = rect.inflate(15,15)
        rect = rect.move(0,-3)

        return rect

    def draw_text_with_border(self,screen,text,pos):
        screen.blit(text, pos)
        border_rect = self.get_border_rect(text.get_frect(), pos)
        pygame.draw.rect(screen, 'gray', border_rect, 5, 10)

    def draw_ui(self, screen):
        score_pos = (self.border_distance,self.border_distance)
        self.draw_text_with_border(screen,self.score_text,score_pos)

        lives_pos = (screen.get_width() - self.lives_text.get_width() - self.border_distance, self.border_distance)
        self.draw_text_with_border(screen,self.lives_text,lives_pos)
