print("Starting")

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.handlers.sequences import simple_key_sequence
from kmk.modules.layers import Layers
from kmk.extensions.rgb import RGB
from kmk.modules.encoder import EncoderHandler

keyboard = KMKKeyboard()

keyboard.col_pins = (board.GP0, board.GP01, board.GP02, board.GP03, board.GP04, board.GP05, board.GP06, board.GP07, board.GP08, board.GP09, board.GP10, board.GP11, board.GP12, board.GP13, board.GP14, board.GP21)
keyboard.row_pins = (board.GP15, board.GP16, board.GP17, board.GP18, board.GP19, board.GP20,)
keyboard.diode_orientation = DiodeOrientation.COL2ROW

encoder_handler = EncoderHandler()

keyboard.modules.append(Layers())
keyboard.modules.append(encoder_handler)

encoder_handler.pins = ((board.GP27, board.GP28, None))

rgb = RGB(pixel_pin=board.GP22, num_pixels=83, rgb_oder=(1,0,2), val_default=40, val_limit = 60)
keyboard.extensions.append(rgb)

LED = KC.LT(1)

## For calculator macro to work you need to create a shortcut with these keys that runs %WinDir%\System32\calc.exe
## For Windows devices
calc_macro = simple_key_sequence(
    (
        KC.LCTL(KC.LALT)(KC.C)
    )
)

screen_shot_macro = simple_key_sequence(
    (
        KC.WIN(KC.LSHIFT)(KC.S)
    )
)

save_macro = simple_key_sequence(
    (
        KC.LCTRl(KC.S)
    )
)

keyboard.keymap = [
    [ ## Base layer
     KC.ESC,  KC.F1,  KC.F2, KC.F3, KC.F4,
     KC.F5, KC.F6, KC.F7, KC.F8, KC.F9,
     KC.F10, KC.F11, KC.F12, calc_macro, KC.MPLY,
     KC.GRV, KC.N1, KC.N2, KC.N3, KC.N4,
     KC.N5, KC.N6, KC.N7, KC.N8, KC.N9,
     KC.N0, KC.MINUS, KC.EQUAL, KC.BSPC, KC.DEL,
     KC.TAB, KC.Q, KC.W, KC.E, KC.R,
     KC.T, KC.Y, KC.U, KC.I, KC.O,
     KC.P, KC.LBRC, KC.RBRC, KC.BSLS, KC.PGUP, KC.CAPSLOCK,
     KC.A, KC.S, KC.D, KC.F, KC.G,
     KC.H, KC.J, KC.K, KC.L, KC.SCLN,
     KC.QUOTE, KC.ENT, KC.PGDN, KC.LSHIFT, KC.Z,
     KC.X, KC.C, KC.V, KC.B, KC.N,
     KC.M, KC.COMM, KC.PERIOD, KC.SLASH, KC.RSHIFT,
     KC.UP, screen_shot_macro, KC.LCTRL, KC.WIN, KC.LALT, 
     KC.SPC, KC.RALT, KC.RFN, KC.RCTRL, KC.LEFT,
     KC.DOWN, KC.RIGHT, save_macro,
    ],

    [ ## LED
        KC.TRNS,  KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,
         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.MTRNSPLY,
         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
         KC.TRNS, KC.TRNSS, KC.TRNS, KC.TRNS, KC.TRNS,
         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,
         KC.RGB_VAI(), KC.RGB_MODE_PLAIN(), KC.TRNS, KC.TRNS, KC.TRNS, 
         KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.RGB_AND(),
         KC.RGB_VAD(), KC.RGB_ANI(), KC.RGB_TOG(),
        ]
]

encoder_handler.map = [
            ((KC.VOLD, KC.VOLU),),            
            ]

if __name__ == '__main__':
    keyboard.go()