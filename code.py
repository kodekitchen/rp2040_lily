from kb import KMKKeyboard

from kmk.extensions.media_keys import MediaKeys

from kmk.keys import KC
from kmk.modules.holdtap import HoldTap
from kmk.modules.layers import Layers
from kmk.modules.split import Split


keyboard = KMKKeyboard()
# keyboard.debug_enabled = True

# Adding modules
# Using drive names (LILY58L, LILY58R) to recognize sides; use split_side arg if you're not doing it
split = Split(
    split_flip=False,
    use_pio=True,
)

keyboard.modules = [split, Layer(), HoldTap()]

keyboard.extensions = [MediaKeys()]

# Cleaner key names
_______ = KC.TRNS
XXXXXXX = KC.NO


LOWER = KC.MO(1)
RAISE = KC.MO(2)


# fmt:off
keyboard.keymap = [
    [  #QWERTY
        KC.ESC,  KC.N1,   KC.N2,   KC.N3,   KC.N4,   KC.N5,                          KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0,   KC.MINS,
        KC.TAB,  KC.Q,    KC.W,    KC.E,    KC.R,    KC.T,                           KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,    KC.LBRC,
        KC.LCTL, KC.A,    KC.S,    KC.D,    KC.F,    KC.G,                           KC.H,    KC.J,    KC.K,    KC.L,    KC.SCLN, KC.QUOT,
        KC.LSFT, KC.Z,    KC.X,    KC.C,    KC.V,    KC.B,    KC.ENTER,     KC.BSPC, KC.N,    KC.M,    KC.COMM, KC.DOT,  KC.SLSH, KC.RSFT,
                                   KC.LALT, KC.LCTL, LOWER,   KC,SPC,       KC.SPC,  RAISE,  KC.LGUI,  KC.RALT,
    ],
    [   #LOWER
        _______, KC.MUTE,       KC.VOLU,       KC.VOLD,        XXXXXXX,        XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        _______, KC.RALT(KC.Q), XXXXXXX,       KC.RALT(KC.E),  KC.LSFT(KC.N4), KC.PLUS,                        XXXXXXX, KC.KP_7, KC.KP_8, KC.KP_9, XXXXXXX, XXXXXXX,
        _______, KC.GRAVE,      KC.SLSH(KC_1), KC.LBRC,        KC.RBRC,        KC.EQL,                         XXXXXXX, KC.KP_4, KC.KP_5, KC.KP_6, XXXXXXX, XXXXXXX,
        _______, XXXXXXX,       XXXXXXX,       XXXXXXX,        XXXXXXX,        XXXXXXX, XXXXXXX,      XXXXXXX, KC.KP_0, KC.KP_1, KC.KP_2, KC.KP_3, KC.BSLS, XXXXXXX,
                                                      _______, _______,        _______, _______,      _______, _______, _______, _______,
    ],
    [   #RAISE
        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        XXXXXXX, XXXXXXX, KC.UP,   XXXXXXX, XXXXXXX, XXXXXXX,                        KC.PSCR, KC.DEL,  KC.HOME, KC.END,  XXXXXXX, XXXXXXX,
        _______, KC.LEFT, KC.DOWN, KC.RGHT, XXXXXXX, XXXXXXX,                        XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
        _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, _______,      _______, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX, XXXXXXX,
                                   _______, _______, _______, _______,      _______, _______, _______, _______,
    ]
]
# fmt:on

if __name__ == '__main__':
    keyboard.go()
