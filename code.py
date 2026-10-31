print("Starting")

import microcontroller

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation

from kmk.extensions.RGB import RGB
from kmk.extensions.rgb import AnimationModes

keyboard = KMKKeyboard()

keyboard.col_pins = (microcontroller.pin.GPIO28,
                     microcontroller.pin.GPIO13,
                     microcontroller.pin.GPIO27,
                     microcontroller.pin.GPIO5,
                     microcontroller.pin.GPIO26,
                     microcontroller.pin.GPIO3,
                     microcontroller.pin.GPIO10,
                     microcontroller.pin.GPIO4,
                     microcontroller.pin.GPIO9)

keyboard.row_pins = (microcontroller.pin.GPIO19,
                     microcontroller.pin.GPIO22,
                     microcontroller.pin.GPIO23,
                     microcontroller.pin.GPIO2,
                     microcontroller.pin.GPIO0,
                     microcontroller.pin.GPIO17,
                     microcontroller.pin.GPIO7,
                     microcontroller.pin.GPIO16,
                     microcontroller.pin.GPIO6,
                     microcontroller.pin.GPIO15,
                     microcontroller.pin.GPIO29,
                     microcontroller.pin.GPIO14)

keyboard.diode_orientation = DiodeOrientation.COL2ROW

keyboard.keymap = [
    [
        KC.ESC, KC.F1, KC.F3, KC.F5, KC.F7, KC.F9, KC.F11, KC.PSCREEN, KC.PAUSE, KC.NO,
        KC.F2, KC.F4, KC.F6, KC.F8, KC.F10, KC.F12, KC.SCROLLLOCK, KC.NO,
     
        KC.GRAVE, KC.N2, KC.N4, KC.N6, KC.N8, KC.N0, KC.EQUAL, KC.INSERT, KC.PGUP,
        KC.N1, KC.N3, KC.N5, KC.N7, KC.N9, KC.MINUS, KC.BSPACE, KC.HOME, KC.NO,
     
        KC.TAB, KC.W, KC.R, KC.Y, KC.I, KC.P, KC.RBRACKET, KC.DELETE, KC.PGDOWN,
        KC.Q, KC.E, KC.T, KC.U, KC.O, KC.LBRACKET, KC.BSLASH, KC.END,

        KC.NO, KC.CAPSLOCK, KC.S, KC.F, KC.H, KC.K, KC.SCOLON, KC.ENTER, KC.NO, KC.RGUI,
        KC.A, KC.D, KC.G, KC.J, KC.L, KC.QUOTE, KC.NO, KC.NO, KC.NO,

        KC.LSHIFT, KC.X, KC.V, KC.N, KC.COMMA, KC.SLASH, KC.NO, KC.NO, KC.NO,
        KC.Z, KC.C, KC.B, KC.M, KC.DOT, KC.RSHIFT, KC.NO, KC.UP, KC.NO,

        KC.LCTRL, KC.LALT, KC.NO, KC.NO, KC.RALT, KC.WINMENU, KC.NO, KC.LEFT, KC.RIGHT,
        KC.LGUI, KC.NO, KC.SPACE, KC.NO, KC.NO, KC.RCTRL, KC.RALT, KC.DOWN
     ]
]

if __name__ == '__main__':
    # set led control pin low
    rgb_pin = microcontroller.pin.GPIO1
    rgb = RGB(pixel_pin=rgb_pin,
        num_pixels=87,
        val_limit=0,
        hue_default=0,
        sat_default=100,
        rgb_order=(1, 0, 2),  # GRB WS2812
        val_default=100,
        hue_step=5,
        sat_step=5,
        val_step=5,
        animation_speed=1,
        breathe_center=1,  # 1.0-2.7
        knight_effect_length=3,
        animation_mode=AnimationModes.STATIC,
        reverse_animation=False,
        refresh_rate=60,
        )
    keyboard.extensions.append(rgb)


    # actually start kmk
    keyboard.go()
