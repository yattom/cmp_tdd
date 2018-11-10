MOCHIGOMA = object()

SENTE = 1
GOTE = 2

def opposite(player):
    return SENTE if player == GOTE else GOTE

class Shogi:
    def __init__(self):
        self.next_player = 1
        self.pieces = [
            ('(KY)', (9, 1), GOTE),
            ('(KE)', (8, 1), GOTE),
            ('(GN)', (7, 1), GOTE),
            ('(KN)', (6, 1), GOTE),
            ('(OU)', (5, 1), GOTE),
            ('(KN)', (4, 1), GOTE),
            ('(GN)', (3, 1), GOTE),
            ('(KE)', (2, 1), GOTE),
            ('(KY)', (1, 1), GOTE),
            ('(HI)', (8, 2), GOTE),
            ('(KK)', (2, 2), GOTE),
            ('(FU)', (9, 3), GOTE),
            ('(FU)', (8, 3), GOTE),
            ('(FU)', (7, 3), GOTE),
            ('(FU)', (6, 3), GOTE),
            ('(FU)', (5, 3), GOTE),
            ('(FU)', (4, 3), GOTE),
            ('(FU)', (3, 3), GOTE),
            ('(FU)', (2, 3), GOTE),
            ('(FU)', (1, 3), GOTE),
            (' KY ', (9, 9), SENTE),
            (' KE ', (8, 9), SENTE),
            (' GN ', (7, 9), SENTE),
            (' KN ', (6, 9), SENTE),
            (' OU ', (5, 9), SENTE),
            (' KN ', (4, 9), SENTE),
            (' GN ', (3, 9), SENTE),
            (' KE ', (2, 9), SENTE),
            (' KY ', (1, 9), SENTE),
            (' HI ', (2, 8), SENTE),
            (' KK ', (8, 8), SENTE),
            (' FU ', (9, 7), SENTE),
            (' FU ', (8, 7), SENTE),
            (' FU ', (7, 7), SENTE),
            (' FU ', (6, 7), SENTE),
            (' FU ', (5, 7), SENTE),
            (' FU ', (4, 7), SENTE),
            (' FU ', (3, 7), SENTE),
            (' FU ', (2, 7), SENTE),
            (' FU ', (1, 7), SENTE),
        ]

    def dump(self):
        mochigoma = []
        next_player = 'Sente' if self.next_player == 1 else 'Gote'
        board = [[' __ ' for i in range(9)] for j in range(9)]
        for p, loc, player in self.pieces:
            if loc == MOCHIGOMA:
                mochigoma.append((p, loc, player))
                continue
            row, col = loc
            board[col - 1][9 - row] = p
        board_str = "\n".join([''.join(p) + f' {i+1}' for i, p in enumerate(board)])
        sente_mochigoma = ''.join([p[1:3] for p, loc, player in mochigoma if player == SENTE])
        gote_mochigoma = ''.join([p[1:3] for p, loc, player in mochigoma if player == GOTE])
        return f"""{next_player}
  9   8   7   6   5   4   3   2   1
{board_str}
{sente_mochigoma}
{gote_mochigoma}
"""

    LABEL_MAP = {
            ' OU ': 'a',
            ' KN ': 'b',
            ' GN ': 'c',
            ' KE ': 'd',
            ' KY ': 'e',
            ' HI ': 'f',
            ' KK ': 'g',
            ' FU ': 'h',
            '(OU)': 'A',
            '(KN)': 'B',
            '(GN)': 'C',
            '(KE)': 'D',
            '(KY)': 'E',
            '(HI)': 'F',
            '(KK)': 'G',
            '(FU)': 'H',
    }

    def save(self):
        next_player = 'Sente' if self.next_player == 1 else 'Gote'
        board = [[' ' for i in range(9)] for j in range(9)]
        for p, loc, player in self.pieces:
            if loc == MOCHIGOMA:
                mochigoma.append((p, loc))
                continue
            row, col = loc
            board[col - 1][9 - row] = Shogi.LABEL_MAP[p]
        board_str = "\n".join([''.join(p) for p in board])
        return f"""{self.next_player}
{board_str}


"""


    def move(self, from_at, to_at):
        for i, (p, loc, player) in enumerate(self.pieces):
            if loc == MOCHIGOMA:
                continue
            row, col = loc
            if from_at == (row, col):
                self.toru(to_at)
                self.pieces[i] = (p, to_at, player)
                break
        else:
            raise ValueError(f'invalid move {from_at}')
        self.next_player = 1 if self.next_player == 2 else 2

    def toru(self, at):
        for i, (p, loc, player) in enumerate(self.pieces):
            if loc == MOCHIGOMA:
                continue
            row, col = loc
            if at == (row, col):
                self.pieces[i] = (p, MOCHIGOMA, opposite(player))
                break

