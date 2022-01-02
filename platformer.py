import random
WIDTH = 1000
HEIGHT = 500
mu = Actor("jumper-1")
hi=Actor("hih")
mu.y_speed = 0
mu.x_speed = 0
um = ZRect((0, 450), (1000, 500))
p = ZRect((200, 350), (500, 40))
i = ZRect((0, 450), (1000, 500))
pl = ZRect((700, 350), (60, 20))
pl2 = ZRect((850, 300), (60, 20))
opl = ZRect((300, 350), (60, 20))
opl2 = ZRect((150, 300), (60, 20))
pl3=ZRect((1000, 0), (50, 500))
s = Actor("spikes")
l = Actor("lava")
l.y = 500
l.x = 500
hi.x=900
hi.x_speed=10
hi.y_speed=10
e = 0
death=0
g = e + 1
level = 1

def draw():
    global death
    screen.clear()
    screen.draw.text(
            "deathcounter: "+str(death), topleft=(0, 0), fontsize=30, color=("red")
        )
    screen.draw.filled_rect(um, (170, 126, 20))
    mu.draw()
    if level == 1:
        screen.draw.text(
            "hi,I am your mentor", center=(500, 20), fontsize=30, color=("white")
        )
    if level == 2:
        s.draw()
        screen.draw.text(
            "jump over the spike", center=(500, 20), fontsize=30, color=("white")
        )
    if level == 3:
        l.draw()
        screen.draw.filled_rect(p, (170, 126, 20))
        screen.draw.text(
            "lava also kills you", center=(500, 20), fontsize=30, color=("white")
        )
    if level == 4:
        screen.draw.filled_rect(i, "blue")
        screen.draw.text(
            "you can get a high mometome if you keep moving from left to right",
            center=(500, 20),
            fontsize=30,
            color=("white"),
        )
    if level == 5:
        s.draw()
        l.draw()
        screen.draw.filled_rect(i, "blue")
        screen.draw.filled_rect(pl, "white")
        screen.draw.filled_rect(pl2, "white")
    if level == 6:
        screen.draw.filled_rect(i, "blue")
        screen.draw.filled_rect(pl, "white")
        screen.draw.filled_rect(pl2, "white")
        screen.draw.filled_rect(opl, "white")
        screen.draw.filled_rect(opl2, "white")
        s.draw()
        screen.draw.text(
            "If you jump at the bottom of the platform,you will jump higher",
            center=(500, 20),
            fontsize=30,
            color=("white"),
        )
        hi.draw()
    if level==7:
        screen.draw.text(
            "Good job",
            center=(500, 20),
            fontsize=30,
            color=("white"),
        )
        screen.draw.filled_rect(pl3, "black")
        screen.draw.filled_rect(i, "blue")
        s.draw()
        screen.draw.filled_rect(i, "blue")
        screen.draw.filled_rect(pl, "white")
        screen.draw.filled_rect(pl2, "white")
        screen.draw.filled_rect(opl, "white")
        screen.draw.filled_rect(opl2, "white")
        l.draw()
def update():
    global g, e, level,death
    if mu.x <= 0:
        mu.x_speed = 1
        mu.x = 3
    mu.x += mu.x_speed
    mu.y += mu.y_speed
    if level == 1 or level == 2 or level == 3:
        mu.x_speed = 0
    if level == 4 or level == 5:
        if not mu.colliderect(i):
            mu.x_speed = 0
    if level == 5:
        l.x = 1000
    mu.y_speed += g
    mu.x = mu.x - 1
    g = e + 1
    if level == 2 or level == 5:
        if mu.colliderect(s):
            death=death+1
            mu.y = 0
            mu.x = 0
    if level == 3 or level == 5:
        if mu.colliderect(l):
            death=death+1
            mu.y = 0
            mu.x = 0
    if mu.x >= WIDTH:
        level = level + 1
        s.bottom = 450
        s.x = 500
        mu.x = 0
        mu.y = 0
    if keyboard.right:
        mu.image = "jumper-right"
        mu.x_speed = 5
    if um.colliderect(mu):
        e = 0
        g = 0
        mu.y_speed = 0
        if keyboard.up:
            if not mu.top <= 0:
                mu.y_speed = -15
                mu.y += mu.y_speed
                e = e + 0.01
    if level == 3:
        if p.colliderect(mu):
            e = 0
            g = 0
            mu.y_speed = 0
            if keyboard.up:
                if not mu.top <= 0:
                    mu.y_speed = -15
                    mu.y += mu.y_speed
                    e = e + 0.01
    if level == 5:
        if pl.colliderect(mu) or pl2.colliderect(mu):
            e = 0
            g = 0
            mu.y_speed = 0
            if keyboard.up:
                if not mu.top <= 0:
                    mu.y_speed = -15
                    mu.y += mu.y_speed
                    e = e + 0.01
    if level == 6:
        s.x = 500
        s.bottom = 450
        if mu.colliderect(s):
            death=death+1
            mu.y = 0
            mu.x = 0
        if (
            pl.colliderect(mu)
            or pl2.colliderect(mu)
            or opl.colliderect(mu)
            or opl2.colliderect(mu)
        ):
            e = 0
            g = 0
            mu.y_speed = 0
            if keyboard.up:
                if not mu.top <= 0:
                    mu.y_speed = -15
                    mu.y += mu.y_speed
                    e = e + 0.01
        if random.randint(1,100)<70:
                hi.x+=hi.x_speed
        else:
                hi.x_speed=hi.x_speed*-1
                hi.x+=hi.x_speed
        if random.randint(1,100)<70:
            hi.y+=hi.y_speed
        else:
            hi.y_speed=hi.y_speed*-1
            hi.y+=hi.y_speed
        if mu.colliderect(hi):
            death=death+1
            mu.x=0
            mu.y=0
            hi.x=900
            hi.y=0
        if hi.x>WIDTH or hi.x<0:
            hi.x_speed=hi.x_speed*-1
            hi.x+=hi.x_speed
        if hi.y>HEIGHT or hi.y<0:
            hi.y_speed=hi.y_speed*-1
            hi.y+=hi.y_speed
    if level ==7:
        if pl3.colliderect(mu):
            mu.x_speed=0
        if mu.colliderect(s):
            death=death+1
            mu.y = 0
            mu.x = 0
        if (
            pl.colliderect(mu)
            or pl2.colliderect(mu)
            or opl.colliderect(mu)
            or opl2.colliderect(mu)
        ):
            e = 0
            g = 0
            mu.y_speed = 0
            if keyboard.up:
                if not mu.top <= 0:
                    mu.y_speed = -15
                    mu.y += mu.y_speed
                    e = e + 0.01
        if mu.colliderect(l):
            death=death+1
            mu.x=0
            mu.y=0
    if not keyboard.right:
        mu.image = "jumper-1"
    if keyboard.left:
        if not mu.left <= 0:
            mu.x_speed = -5
            mu.image = "jumper-left"
