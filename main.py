def on_on_overlap(sprite, otherSprite):
    otherSprite.destroy()
    info.change_score_by(1)
sprites.on_overlap(SpriteKind.player, SpriteKind.food, on_on_overlap)

scene.set_background_color(9)
tiles.set_current_tilemap(tilemap("""
    level2
"""))
mySprite = sprites.create(img("""
        3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 
            3 3 3 3 3 3 3 3 3 3 3 3 3 3 3 3
    """),
    SpriteKind.player)
controller.move_sprite(mySprite, 100, 100)
scene.camera_follow_sprite(mySprite)
mySprite2 = sprites.create(img("""
        5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
    """),
    SpriteKind.player)
for index in range(100):
    tiles.place_on_random_tile(mySprite2, assets.tile("""
        myTile0
    """))
    mySprite2 = sprites.create(img("""
            5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 
                    5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
        """),
        SpriteKind.food)