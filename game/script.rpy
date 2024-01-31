define player = Character("[player_name]")

label start:
    python:
        player_name = renpy.input("Як тебе звати?")

    return
