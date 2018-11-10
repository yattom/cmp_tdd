# coding: utf8

class Piece:
    def __init__(self, code, name):
        self._code = code
        self._name = name

OUSHO = Piece('a', 'OU')
KIN = Piece('b', 'KN')
GIN = Piece('c', 'GN')
KEIMA = Piece('d', 'KI')
KYOSHA = Piece('e', 'KY')
HISHA = Piece('f', 'HI')
KAKU = Piece('g', 'KK')
FU = Piece('h', 'FU')
NARI_GIN = Piece('i', 'NG')
NARK_KEI = Piece('j', 'NK')
NARK_KYO = Piece('k', 'NY')
RYUOU = Piece('l', 'RY')
RYUMA = Piece('m', 'MA')
TOKIN = Piece('n', 'TO')

MOCHIGOMA = object()

PIECES = {
    'a': OUSHO,
    'b': KIN,
    'c': GIN,
    'd': KEIMA,
    'e': KYOSHA,
    'f': HISHA,
    'g': KAKU,
    'h': FU,
    'i': NARI_GIN,
    'j': NARK_KEI,
    'k': NARK_KYO,
    'l': RYUOU,
    'm': RYUMA,
    'n': TOKIN,
}

class Board:
    def __init__(self):
        self._sente = []
        self._gote = []

    def initialize_game(self):
        self._sente = [
            (OUSHO, (5, 9)),
            (KIN, (4, 9)),
            (KIN, (6, 9)),
            (GIN, (3, 9)),
            (GIN, (7, 9)),
            (KEIMA, (2, 9)),
            (KEIMA, (8, 9)),
            (KYOSHA, (1, 9)),
            (KYOSHA, (9, 9)),
            (HISHA, (2, 8)),
            (KAKU, (8, 8)),
            (FU, (9, 7)),
            (FU, (8, 7)),
            (FU, (7, 7)),
            (FU, (6, 7)),
            (FU, (5, 7)),
            (FU, (4, 7)),
            (FU, (3, 7)),
            (FU, (2, 7)),
            (FU, (1, 7)),
        ]
        self._gote = [
            (OUSHO, (5, 1)),
            (KIN, (4, 1)),
            (KIN, (6, 1)),
            (GIN, (3, 1)),
            (GIN, (7, 1)),
            (KEIMA, (2, 1)),
            (KEIMA, (8, 1)),
            (KYOSHA, (1, 1)),
            (KYOSHA, (9, 1)),
            (HISHA, (8, 2)),
            (KAKU, (2, 2)),
            (FU, (9, 3)),
            (FU, (8, 3)),
            (FU, (7, 3)),
            (FU, (6, 3)),
            (FU, (5, 3)),
            (FU, (4, 3)),
            (FU, (3, 3)),
            (FU, (2, 3)),
            (FU, (1, 3)),
        ]

    def dump(self):
        sente_mochigoma = []
        gote_mochigoma = []
        out = ''.join([f"  {i} " for i in range(1, 10)]) + "\n"
        board = [[' __ ' for i in range(9)] for j in range(9)]
        for p, loc in self._sente:
            if loc == MOCHIGOMA:
                sente_mochigoma += p
                continue
            row, col = loc
            board[col - 1][row - 1] = f' {p._name} '
        for p, loc in self._gote:
            if loc == MOCHIGOMA:
                sente_mochigoma += p
                continue
            row, col = loc
            board[col - 1][row - 1] = f'({p._name})'
        out += '\n'.join([''.join(r) + f' {i+1}' for i, r in enumerate(board)])
        out += "\n"
        out += f"Sente: {', '.join([p._name for p in sente_mochigoma])}\n"
        out += f"Gote: {', '.join([p._name for p in gote_mochigoma])}\n"
        return out


    def save(self):
        sente_mochigoma = []
        gote_mochigoma = []
        board = [[' ' for i in range(9)] for j in range(9)]
        for p, loc in self._sente:
            if loc == MOCHIGOMA:
                sente_mochigoma += p
                continue
            row, col = loc
            board[col - 1][row - 1] = p._code
        for p, loc in self._gote:
            if loc == MOCHIGOMA:
                gote_mochigoma += p
                continue
            row, col = loc
            board[col - 1][row - 1] = p._code.upper()
        out = '\n'.join([''.join(r) for r in board])
        out += "\n"
        out += f"{' '.join([p._code for p in sente_mochigoma])}\n"
        out += f"{' '.join([p._code.upper() for p in gote_mochigoma])}\n"
        return out

    def load(self, lines):

        pass

class Shogi:
    def __init__(self):
        self.board = Board()
        self.next_player = 1

    def dump(self):
        out = ('Sente' if self.next_player == 1 else 'Gote') + '\n'
        out += self.board.dump()
        return out

    def save(self):
        out = "1\n"
        out += self.board.save()
        return out

def main():
    shogi = Shogi()
    shogi.board.initialize_game()
    print(shogi.dump())
    print(shogi.save())

if __name__=='__main__':
    main()
