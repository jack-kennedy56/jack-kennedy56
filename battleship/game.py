ships = []
guesses = []

def start_new(b_start, s_start, d_start):
    global ships
    global guesses
    # Create 20 blanks in ships and guesses
    for i in range(20):
        ships.append('_')
        guesses.append('_')

    # Adjust start positions back one to start at zero
    b_start = b_start - 1
    s_start = s_start - 1
    d_start = d_start - 1

    for i in range(b_start, b_start+4):
        ships[i] = 'b'

    for i in range(s_start, s_start+3):
        ships[i] = 's'

    for i in range(d_start, d_start+2):
        ships[i] = 'd'

    return ships


def get_ships():
    global ships
    return ships


def make_guess(position):
    global guesses

    # Adjust position to start at zero
    position = position - 1

    hit_or_miss = ''
    if ships[position] != '_':
        hit_or_miss = 'h'
    else:
        hit_or_miss = 'm'
    guesses[position] = hit_or_miss

    return hit_or_miss

def get_guesses():
    global guesses
    return guesses