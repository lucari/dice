dicenum = 0

def on_gesture_shake():
    global dicenum
    dicenum = randint(1, 6)
    if dicenum == 1:
        basic.show_leds("""
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """)
    elif dicenum == 2:
        basic.show_leds("""
            . . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . .
            """)
    elif dicenum == 3:
        basic.show_leds("""
            . . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . .
            """)
    elif dicenum == 4:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . . . .
            . . . . .
            # . . . #
            """)
    elif dicenum == 5:
        basic.show_leds("""
            # . . . #
            . . . . .
            . . # . .
            . . . . .
            # . . . #
            """)
    elif dicenum == 6:
        basic.show_leds("""
            # . . . #
            . . . . .
            # . . . #
            . . . . .
            # . . . #
            """)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)
