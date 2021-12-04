info.set_score(0)
info.start_countdown(30)
lemon = sprites.create(img("""
        4 4 4 . . 4 4 4 4 4 . . . . . . 
            4 5 5 4 4 5 5 5 5 5 4 4 . . . . 
            b 4 5 5 1 5 1 1 1 5 5 5 4 . . . 
            . b 5 5 5 5 1 1 5 5 1 1 5 4 . . 
            . b d 5 5 5 5 5 5 5 5 1 1 5 4 . 
            b 4 5 5 5 5 5 5 5 5 5 5 1 5 4 . 
            c d 5 5 5 5 5 5 5 5 5 5 5 5 5 4 
            c d 4 5 5 5 5 5 5 5 5 5 5 1 5 4 
            c 4 5 5 5 d 5 5 5 5 5 5 5 5 5 4 
            c 4 d 5 4 5 d 5 5 5 5 5 5 5 5 4 
            . c 4 5 5 5 5 d d d 5 5 5 5 5 b 
            . c 4 d 5 4 5 d 4 4 d 5 5 5 4 c 
            . . c 4 4 d 4 4 4 4 4 d d 5 d c 
            . . . c 4 4 4 4 4 4 4 4 5 5 5 4 
            . . . . c c b 4 4 4 b b 4 5 4 4 
            . . . . . . c c c c c c b b 4 .
    """),
    SpriteKind.player)
scene.set_background_color(8)
controller.move_sprite(lemon)
lemon.set_flag(SpriteFlag.STAY_IN_SCREEN, True)

def reset_coin():
    coin.set_position(Math.random_range(0,160),Math.random_range(0,120))
    coin.say_text("Im here")
coin = sprites.create(img("""
    . . b b b b . .
    . b 5 5 5 5 b .
    b 5 d 3 3 5 5 b
    b 5 3 5 5 1 5 b
    c 5 3 5 5 1 5 c
    c 5 5 1 1 5 5 c
    . f 5 5 5 5 f .
    . . f f f f . .
"""), SpriteKind.food)
reset_coin()

def create_strawberry():
    strawberry = sprites.create_projectile_from_side(img("""
        . . . . . . . 6 . . . . . . . .
        . . . . . . 8 6 6 . . . 6 8 . .
        . . . e e e 8 8 6 6 . 6 7 8 . .
        . . e 2 2 2 2 e 8 6 6 7 6 . . .
        . e 2 2 4 4 2 7 7 7 7 7 8 6 . .
        . e 2 4 4 2 6 7 7 7 6 7 6 8 8 .
        e 2 4 5 2 2 6 7 7 6 2 7 7 6 . .
        e 2 4 4 2 2 6 7 6 2 2 6 7 7 6 .
        e 2 4 2 2 2 6 6 2 2 2 e 7 7 6 .
        e 2 4 2 2 4 2 2 2 4 2 2 e 7 6 .
        e 2 4 2 2 2 2 2 2 2 2 2 e c 6 .
        e 2 2 2 2 2 2 2 4 e 2 e e c . .
        e e 2 e 2 2 4 2 2 e e e c . . .
        e e e e 2 e 2 2 e e e c . . . .
        e e e 2 e e c e c c c . . . . .
        . c c c c c c c . . . . . . . .
    """), Math.random_range(50,10), Math.random_range(10,50))
game.on_update_interval(500, create_strawberry) 

def create_cherry():
    cherry = sprites.create_projectile_from_side(img("""
        . . . . . . . . . . . 6 6 6 6 6
        . . . . . . . . . 6 6 7 7 7 7 8
        . . . . . . 8 8 8 7 7 8 8 6 8 8
        . . e e e e c 6 6 8 8 . 8 7 8 .
        . e 2 5 4 2 e c 8 . . . 6 7 8 .
        e 2 4 2 2 2 2 2 c . . . 6 7 8 .
        e 2 2 2 2 2 2 2 c . . . 8 6 8 .
        e 2 e e 2 2 2 2 e e e e c 6 8 .
        c 2 e e 2 2 2 2 e 2 5 4 2 c 8 .
        . c 2 e e e 2 e 2 4 2 2 2 2 c .
        . . c 2 2 2 e e 2 2 2 2 2 2 2 e
        . . . e c c e c 2 2 2 2 2 2 2 e
        . . . . . . . c 2 e e 2 2 e 2 c
        . . . . . . . c e e e e e e 2 c
        . . . . . . . . c e 2 2 2 2 c .
        . . . . . . . . . c c c c c . .
    """), Math.random_range(-50,-10), Math.random_range(10,50))
game.on_update_interval(2000, create_cherry)

def berry_overlap(sprite, otherSprite):
    info.change_score_by(-1)
    otherSprite.destroy()
    sprite.say_text("ouch")
sprites.on_overlap(SpriteKind.player, SpriteKind.projectile, berry_overlap)

def coin_overlap(sprite, otherSprite):
    info.change_score_by(2)
    reset_coin()
sprites.on_overlap(SpriteKind.player, SpriteKind.food, coin_overlap)
