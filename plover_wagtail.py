KEYS = (
    '#',
    'Ƨ-', 'G-', 'B-', 'D-', 'Z-', 'I-', 'U-', 'A-', 'Ǝ-', 'N-', 'У-', 'Ч-',
    '-Ƨ', '-G', '-B', '-D', '-Z', '-I', '-U', '-A', '-Ǝ', '-N', '-У', '-Ч',
)

IMPLICIT_HYPHEN_KEYS = ()

SUFFIX_KEYS = ()

NUMBER_KEY = '#'

NUMBERS = {
    'N-': '5-',
    'A-': '4-',
    'I-': '3-',
    'D-': '2-',
    'G-': '1-',
    '-G': '-6',
    '-D': '-7',
    '-I': '-8',
    '-A': '-9',
    '-N': '-0',
}

UNDO_STROKE_STENO = "-Ƨ"

ORTHOGRAPHY_RULES = []

ORTHOGRAPHY_RULES_ALIASES = {}

ORTHOGRAPHY_WORDLIST = None

KEYMAPS = {
    'Keyboard': {
        '#': ('1', '2', '3', '4', '5', '6', '7', '8', '9', '0'),

        'N-': 'q',
        'У-': 'a',
        'A-': 'w',
        'Ǝ-': 's',
        'I-': 'e',
        'U-': 'd',
        'D-': 'r',
        'Z-': 'f',
        'Ƨ-': 't',
        'Ƨ-': 'g',
        'B-': 'c',
        'G-': 'v',

        '-G': 'n',
        '-B': 'm',
        '-Ƨ': 'y',
        '-Ƨ': 'h',
        '-D': 'u',
        '-Z': 'j',
        '-I': 'i',
        '-U': 'k',
        '-A': 'o',
        '-Ǝ': 'l',
        '-N': 'p',
        '-У': ';',
	'-Ч': '[',
	'-Ч': ''',

        'arpeggiate': 'space',
        'no-op': ('b'),
    },
    'Gemini PR': {
        '#': ('#1', '#2', '#3', '#4', '#5', '#6', '#7', '#8', '#9', '#A', '#B', '#C'),

        'N-': 'S1-',
        'У-': 'S2-',
        'A-': 'T-',
        'Ǝ-': 'K-',
        'I-': 'P-',
        'U-': 'W-',
        'D-': 'H-',
        'Z-': 'R-',
        'Ƨ-': '*1',
        'Ƨ-': '*3',
        'B-': 'A-',
        'G-': 'O-',

        '-G': '-E',
        '-B': '-U',
        '-Ƨ': '*2',
        '-Ƨ': '*4',
        '-D': '-F',
        '-Z': '-R',
        '-I': '-P',
        '-U': '-B',
        '-A': '-L',
        '-Ǝ': '-G',
        '-N': '-T',
        '-У': '-S',
	'-Ч': '-D',
	'-Ч': '-Z',

        'no-op': ('res1', 'res2', 'Fn', 'pwr'),
    }
}

DICTIONARIES_ROOT = './dictionaries/'
DEFAULT_DICTIONARIES = (
	'wagtail_main.json'

)
