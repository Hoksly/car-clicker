import pygame
import time
import random

start_time = time.time()
seconds_left = 0

pygame.init()
run = True

WINDOW_HEIGHT = 600
WINDOW_WIDTH = 1000
BUILDINGS_BEG = 308

window = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

'''Background images'''
background_image = pygame.image.load('data/backgroungs/background_img.png')
background_image_back = pygame.image.load('data/backgroungs/background_img.png')
lenin_background = pygame.image.load('data/backgroungs/Lenin_bg.jpeg')
wooden_background = pygame.image.load('data/backgroungs/wooden_background.png')
wooden_stick = pygame.image.load('data/backgroungs/wooden_bar.png')
f_stick = pygame.image.load('data/backgroungs/buildings_wooden_bar.png')

'''Other sprites'''
small_fuel_image = pygame.image.load('data/scaled_f.png')

'''Structures'''
A_canister = pygame.transform.scale(pygame.image.load('data/structures/A_canister.png'), (300, 64))
Oil_station_image = pygame.transform.scale(pygame.image.load('data/structures/Oil_station.png'), (300, 64))
Gas_station_image = pygame.transform.scale(pygame.image.load('data/structures/gas_station.png'), (300, 64))
Wild_territory = pygame.transform.scale(pygame.image.load('data/structures/Wild_territory.png'), (300, 64))
Pipeline = pygame.transform.scale(pygame.image.load('data/structures/Pipeline.png'), (300, 64))
Desert_well = pygame.transform.scale(pygame.image.load('data/structures/Desert_oil.png'), (300, 64))
Oil_tanker = pygame.transform.scale(pygame.image.load('data/structures/Tanker.png'), (300, 64))

'''Fonts'''
MAIN_FONT = pygame.font.SysFont('data/fonts/ChelseaMarket-Regular.ttf', 50)
font1 = pygame.font.SysFont('data/fonts/ChelseaMarket-Regular.ttf', 45)
font2 = pygame.font.SysFont('data/fonts/ChelseaMarket-Regular.ttf', 30)
font3 = pygame.font.SysFont('data/fonts/Piedra-Regular.ttf', 30)
font4 = pygame.font.SysFont('data/fonts/Piedra-Regular.ttf', 60)
'''Object characteristics'''
fuel_val = 7

'''Cars'''
ZAZ_image = pygame.image.load('data/cars/ZAZ.png')
mercedes_image = pygame.image.load('data/cars/mercedes.png')
track_image = pygame.image.load('data/cars/track.png')
random_car_image = pygame.image.load('data/cars/just_car.png')
lenin_image = pygame.image.load('data/cars/Lenin.png')
lanos_image = pygame.image.load('data/cars/lanos.png')
horse_image = pygame.image.load('data/cars/horse.png')

'''Dream cars'''
ZAZ_dream = pygame.transform.scale(pygame.image.load('data/structures/cars/ZAZ.png'), (300, 64))
Lanos_dream = pygame.transform.scale(pygame.image.load('data/structures/cars/Lanos.png'), (300, 64))
Mecredes_dream = pygame.transform.scale(pygame.image.load('data/structures/cars/Mercedes.png'), (300, 64))
Lenin_dream = pygame.transform.scale(pygame.image.load('data/structures/cars/Lenin.png'), (300, 64))
Cyber_track_dream = pygame.transform.scale(pygame.image.load('data/structures/cars/Cyber_track.png'), (300, 64))
Random_car_dream = pygame.transform.scale(pygame.image.load('data/structures/cars/Random_car.png'), (300, 64))

'''Colors'''
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Car:
    def __init__(self, x, y, car_image, base_click = 1, name = None):
        self.x = x
        self.y = y
        self.length = 250
        self.height = 250
        self.car_image = car_image
        self.animation_state = 0
        self.base_click = base_click
        self.name = name

    def draw(self):
        if self.animation_state > 0:
            cookie_img_scaled = pygame.transform.scale(self.car_image, (int(0.9 * self.length), int(0.9 * self.height)))
            window.blit(cookie_img_scaled, (
                cookie_img_scaled.get_rect(center=(int(self.x + self.length / 2), int(self.y + self.height / 2)))))
            self.animation_state -= 1
        else:
            window.blit(self.car_image,
                        (self.car_image.get_rect(
                            center=(int(self.x + self.length / 2), int(self.y + self.height / 2)))))

    def collidepoint(self, point):
        return pygame.Rect(self.x, self.y, self.length, self.height).collidepoint(point)

    def give_fuel(self):
        return self.base_click

class Player:
    def __init__(self):
        self.score = 0
        self.level = 1
        self.FPS = 0


class Small_fuel:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 40
        self.height = 40

    def draw(self):
        self.y += fuel_val
        window.blit(small_fuel_image, small_fuel_image.get_rect(
            center=(int(self.x + self.length / 2), int(self.y + self.height / 2 + 30))))


class Score_display:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.length = 100
        self.width = 100

    def draw(self):
        score = font1.render('{} fuels'.format(format(transform(user.score))), True, WHITE)
        FPS = font2.render('{} per second'.format(transform(user.FPS)), True, WHITE)

        window.blit(score, score.get_rect(center=(int(self.x + self.length / 2), int(self.y + self.width / 2))))
        window.blit(FPS, FPS.get_rect(center=(int(self.x + self.length / 2), int(self.y + self.width / 2 + 30))))


class Buy_object:
    def __init__(self, x, y, image, text, price):
        self.x = x
        self.y = y
        self.width = 100
        self.height = 30


class Wooden_background:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 300
        self.height = WINDOW_HEIGHT

    def draw(self):
        window.blit(wooden_background,
                    wooden_background.get_rect(center=(int(self.x + self.height / 2), int(self.y + self.width / 2))))


class Another_stick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = f_stick.get_width()
        self.height = f_stick.get_height()

    def draw(self):
        window.blit(f_stick, f_stick.get_rect(center=(int(self.x + self.height / 2), int(self.y + self.width / 2))))


class Structure:
    def __init__(self, name, base_cost, FPS, increase, height, width, pos, image):
        self.name = name
        self.base_cost = base_cost
        self.increase = increase
        self.level = 0
        self.FPS = FPS
        self.height = 64
        self.width = 300
        self.x = pos[0]
        self.y = pos[1]
        self.image = image
        self.mode = 0
        self.hides = False
    def upgrade_value(self):
        self.level += 1
        self.base_cost = int(self.increase * self.base_cost)

    def give_fuel(self):
        return self.FPS

    def hide(self):
        self.hides = True

    def dehide(self):
        self.hides = False

    def draw(self):
        value_text = font3.render(transform(self.base_cost) + ' => {}'.format(transform(self.FPS)), True, BLACK)
        level_text = font4.render(transform(self.level), True, BLACK)
        ''

        vt_x = 0.9
        vt_y = 1.275

        lt_x = 1.8
        lt_y = 0.9
        if self.name == 'oil_tanker' or 'pipeline' or 'desert_oil':
            vt_x = 0.8
            vt_y = 1.55

        if self.mode == 0:
            value_text.set_alpha(100)
            level_text.set_alpha(100)
            self.image.set_alpha(100)
        elif self.mode == 1:
            value_text.set_alpha(255)
            level_text.set_alpha(255)
            self.image.set_alpha(255)
        if not self.hides:
            window.blit(self.image,
                        self.image.get_rect(center=(int(self.x + self.width / 2), int(self.y + self.height / 2))))

            window.blit(value_text,
                        value_text.get_rect(center=(int(self.x + (self.width * vt_x + value_text.get_width()) / 2),
                                                    int(self.y + self.height * vt_y / 2))))

            window.blit(level_text, level_text.get_rect(
                center=(int(self.x + self.width * lt_x / 2), int(self.y + self.height * lt_y / 2))))

    def collidepoint(self, point):
        if not self.hides:
            return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(point)


class Dream_car:
    def __init__(self, car_object, p_g, pos, image, width, height):
        self.car_object = car_object
        self.base_cost = p_g[0]
        self.car_object.base_click = p_g[1]
        self.width = width
        self.height = height
        self.x = pos[0]
        self.y = pos[1]
        self.image = image
        self.mode = 0
        self.hides = False

    def draw(self):
        value_text = font3.render(transform(self.base_cost) + ' => {}'.format(transform(self.car_object.base_click)), True, BLACK)

        vt_x = 0.9
        vt_y = 1.275

        if self.mode == 0:
            value_text.set_alpha(100)
            self.image.set_alpha(100)
        elif self.mode == 1:
            value_text.set_alpha(255)
            self.image.set_alpha(255)

        if not self.hides:
            window.blit(self.image,
                        self.image.get_rect(center=(int(self.x + self.width / 2), int(self.y + self.height / 2))))

            window.blit(value_text,
                        value_text.get_rect(center=(int(self.x + (self.width * vt_x + value_text.get_width()) / 2),
                                                    int(self.y + self.height * vt_y / 2))))

    def collidepoint(self, point):
        if not self.hides:
            return pygame.Rect(self.x, self.y, self.width, self.height).collidepoint(point)

    def new_car(self):
        return self.car_object

    def hide(self):
        self.hides = True

    def dehide(self):
        self.hides = False


class Wooden_stick:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 20
        self.height = WINDOW_HEIGHT

    def draw(self):
        window.blit(wooden_stick,
                    wooden_stick.get_rect(center=(int(self.x + self.height / 2), int(self.y + self.width / 2))))


def transform(value, m= 0):
    if 0 <= value < 1000:
        return str(round(value, 1))
    elif 1000 <= value < 10**6:
        return str(round(value/1000, 1)) + 'k'
    elif 10**6 < value < 10**9:
        return str(round(value/ 10**6, 1)) + 'kk'
    elif 10**9 <= value < 10**12:
        return str(round(value/10**9, 1)) + 'kkk'
    elif 10 ** 12 <= value < 10 ** 15:
        return str(round(value / 10 ** 12, 1)) + 'kkkk'
    elif 10 ** 15 <= value < 10 ** 18:
        return str(round(value / 10 ** 18, 1)) + 'kkkkk'


def draw_structures(list_of_st):
    for structure in list_of_st:
        if structure.base_cost <= user.score:
            structure.mode = 1
        else:
            structure.mode = 0
        structure.draw()


def draw_dream_cars(list_of_cars):
    for dream_car in list_of_cars:
        if dream_car.base_cost <= user.score:
            dream_car.mode = 1
        else:
            dream_car.mode = 0

        dream_car.draw()



def draw():
    window.blit(background_image, (0, 0))
    car.draw()
    score_display.draw()
    wood_back.draw()
    wooden_st.draw()
    f_st.draw()
    draw_structures(LIST_OF_STRUCTURES)
    draw_dream_cars(LIST_OF_CARS)
    for fuel in sprite_list:
        if fuel.y > WINDOW_HEIGHT:
            sprite_list.remove(fuel)
        else:
            fuel.draw()
    pygame.display.update()


st_pos = 150
Car_x, Car_y = 175, 190
car = Car(Car_x, Car_y, horse_image)

user = Player()
score_display = Score_display(200, 100)
wood_back = Wooden_background(550, 150)
wooden_st = Wooden_stick(394, 290)
f_st = Another_stick(845, st_pos)
sprite_list = []
'''Structures'''
canister = Structure('canister', 15, 0.1, 1.2, 300, 64, (700, BUILDINGS_BEG), A_canister)
oil_station = Structure('oil_station', 100, 1, 1.2, 300, 64, (700, BUILDINGS_BEG + 64 * 1), Oil_station_image)
gas_station = Structure('gas_station', 1100, 8, 1.2, 300, 63, (700, BUILDINGS_BEG  + 64 * 2), Gas_station_image)
wild_territory = Structure('wild_territory', 12000, 47, 1.2, 300, 63, (700, BUILDINGS_BEG  + 64 * 3), Wild_territory)
desert_oil = Structure('desert_oil', 130000, 260, 1.2, 300, 63, (700, BUILDINGS_BEG  + 64 * 4), Desert_well)
pipeline = Structure('pipeline', 800 * 10 ** 3, 450 * 10**2, 1.2, 300, 63, (700, BUILDINGS_BEG  + 64 * 5), Pipeline)
tanker = Structure('oil_tanker', 1.3 * 10 ** 7, 10**5, 1.2, 300, 63, (700, BUILDINGS_BEG  + 64 * 6), Oil_tanker)

'''Adding them in the list'''
LIST_OF_STRUCTURES = list()
LIST_OF_STRUCTURES.append(canister)
LIST_OF_STRUCTURES.append(oil_station)
LIST_OF_STRUCTURES.append(gas_station)
LIST_OF_STRUCTURES.append(wild_territory)
LIST_OF_STRUCTURES.append(desert_oil)
LIST_OF_STRUCTURES.append(pipeline)
LIST_OF_STRUCTURES.append(tanker)

'''Cars'''
ZAZ = Car(Car_x, Car_y, ZAZ_image)
Lanos = Car(Car_x, Car_y, lanos_image)
Random_car = Car(Car_x, Car_y, random_car_image)
Lenin = Car(Car_x, Car_y, lenin_image, name= 'Lenin')
Mercedes = Car(Car_x, Car_y, mercedes_image)
Track = Car(Car_x, Car_y, track_image)

'''Cars to buy'''
Zaz_buy = Dream_car(ZAZ, (8000, 5), (700, 0), ZAZ_dream, 300, 64)
Lanos_buy = Dream_car(Lanos, (50000, 15), (700, 64*1), Lanos_dream, 300, 64)
Random_car_buy = Dream_car(Random_car, (200000, 40), (700, 64*2), Random_car_dream, 300, 64)
Mercedes_buy = Dream_car(Mercedes, (500* 10**3, 100), (700, 64*3), Mecredes_dream, 300, 64)
Track_buy = Dream_car(Track, (1* 10**7, 800), (700, 64*4), Cyber_track_dream, 300, 64)
Lenin_sell = Dream_car(Lenin, (10**9, 10**4), (700, 64*5), Lenin_dream, 300, 64)
Track_buy.hide()
Lenin_sell.hide()

LIST_OF_CARS = list()

LIST_OF_CARS.append(Zaz_buy)
LIST_OF_CARS.append(Lanos_buy)
LIST_OF_CARS.append(Random_car_buy)
LIST_OF_CARS.append(Mercedes_buy)
LIST_OF_CARS.append(Track_buy)
LIST_OF_CARS.append(Lenin_sell)

user.score = 8000

while run:

    pygame.time.delay(10)
    if time.time() - start_time > seconds_left:
        seconds_left += 1
        user.score += user.FPS
        if user.FPS > 0:
            x, y = random.randint(0, int(WINDOW_WIDTH * 0.8)), random.randint(0, int(WINDOW_HEIGHT * 0.8))
            sprite_list.append(Small_fuel(x, y))

    for el in pygame.event.get():
        if el.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = el.pos
            if car.collidepoint(mouse_pos):
                user.score += car.base_click
                car.animation_state = 1
                sprite_list.append(Small_fuel(mouse_pos[0], mouse_pos[1]))
            for structure in LIST_OF_STRUCTURES:
                if structure.collidepoint(mouse_pos):
                    if user.score >= structure.base_cost:
                        user.score -= structure.base_cost
                        structure.upgrade_value()
                        user.FPS += structure.give_fuel()
            for dream_car in LIST_OF_CARS:
                if dream_car.collidepoint(mouse_pos):
                    if user.score >= dream_car.base_cost:
                        car = dream_car.new_car()
                        user.score -= dream_car.base_cost
                        if car.name == 'Lenin':
                            background_image = lenin_background
                        else:
                            background_image = background_image_back

        if el.type == pygame.QUIT:
            run = False
        x, y = pygame.mouse.get_pos()[0], pygame.mouse.get_pos()[1]

        if 700 < x < 1000 and 550 <= y <= 600:
            for structure in LIST_OF_STRUCTURES:
                if structure.y <= BUILDINGS_BEG or structure.y >= 600:
                    structure.hide()
                else:
                    structure.dehide()
            if LIST_OF_STRUCTURES[-2].y >= BUILDINGS_BEG + 1 :
                for structure in LIST_OF_STRUCTURES:
                    structure.y -= 4

        elif 700 < x < 1000 and BUILDINGS_BEG <= y <= BUILDINGS_BEG+50:
            for structure in LIST_OF_STRUCTURES:
                if structure.y <= BUILDINGS_BEG or structure.y >= 600:
                    structure.hide()
                else:
                    structure.dehide()
            if LIST_OF_STRUCTURES[0].y <= BUILDINGS_BEG:
                for structure in LIST_OF_STRUCTURES:
                        structure.y += 4

        elif 700 < x < 1000 and 0 <= y <= 50:
            for dream_car in LIST_OF_CARS:

                if dream_car.y < 0 or dream_car.y >= BUILDINGS_BEG-64:
                    dream_car.hide()
                else:
                    dream_car.dehide()
            if LIST_OF_CARS[0].y < 0:
                for dream_car in LIST_OF_CARS:
                    dream_car.y += 4

        elif 700 < x < 1000 and BUILDINGS_BEG-50 < y <= BUILDINGS_BEG:
            for dream_car in LIST_OF_CARS:

                if dream_car.y < 0 or dream_car.y >= BUILDINGS_BEG - 64:
                    dream_car.hide()
                else:
                    dream_car.dehide()
            if LIST_OF_CARS[2].y >= 0:
                for dream_car in LIST_OF_CARS:
                    dream_car.y -= 4
    draw()

pygame.quit()
