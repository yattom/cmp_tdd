from shogi import *

def test_dump_initial_state():
    expected = """Sente
  9   8   7   6   5   4   3   2   1
(KY)(KE)(GN)(KN)(OU)(KN)(GN)(KE)(KY) 1
 __ (HI) __  __  __  __  __ (KK) __  2
(FU)(FU)(FU)(FU)(FU)(FU)(FU)(FU)(FU) 3
 __  __  __  __  __  __  __  __  __  4
 __  __  __  __  __  __  __  __  __  5
 __  __  __  __  __  __  __  __  __  6
 FU  FU  FU  FU  FU  FU  FU  FU  FU  7
 __  KK  __  __  __  __  __  HI  __  8
 KY  KE  GN  KN  OU  KN  GN  KE  KY  9


"""
    shogi = Shogi()
    actual = shogi.dump()
    assert expected == actual

def test_dump_initial_state_gote():
    expected = """Gote
  9   8   7   6   5   4   3   2   1
(KY)(KE)(GN)(KN)(OU)(KN)(GN)(KE)(KY) 1
 __ (HI) __  __  __  __  __ (KK) __  2
(FU)(FU)(FU)(FU)(FU)(FU)(FU)(FU)(FU) 3
 __  __  __  __  __  __  __  __  __  4
 __  __  __  __  __  __  __  __  __  5
 __  __  __  __  __  __  __  __  __  6
 FU  FU  FU  FU  FU  FU  FU  FU  FU  7
 __  KK  __  __  __  __  __  HI  __  8
 KY  KE  GN  KN  OU  KN  GN  KE  KY  9


"""
    shogi = Shogi()
    shogi.next_player = 2
    actual = shogi.dump()
    assert expected == actual

def test_dump_initial_state_after_a_move():
    expected = """Gote
  9   8   7   6   5   4   3   2   1
(KY)(KE)(GN)(KN)(OU)(KN)(GN)(KE)(KY) 1
 __ (HI) __  __  __  __  __ (KK) __  2
(FU)(FU)(FU)(FU)(FU)(FU)(FU)(FU)(FU) 3
 __  __  __  __  __  __  __  __  __  4
 __  __  __  __  __  __  __  __  __  5
 __  __  FU  __  __  __  __  __  __  6
 FU  FU  __  FU  FU  FU  FU  FU  FU  7
 __  KK  __  __  __  __  __  HI  __  8
 KY  KE  GN  KN  OU  KN  GN  KE  KY  9


"""
    shogi = Shogi()
    shogi.move((7, 7), (7, 6))
    actual = shogi.dump()
    assert expected == actual

def test_dump_with_mochigoma():
    expected = """Gote
  9   8   7   6   5   4   3   2   1
(KY)(KE)(GN)(KN)(OU) __ (GN)(KE)(KY) 1
 __ (HI) __  __  __ (KN) __ (KK) __  2
(FU)(FU)(FU)(FU)(FU)(FU) KK (FU)(FU) 3
 __  __  __  __  __  __  __  __  __  4
 __  __  __  __  __  __  __  __  __  5
 __  __  FU  __  __  __  __  __  __  6
 FU  FU  __  FU  FU  FU  FU  FU  FU  7
 __  __  __  __  __  __  __  HI  __  8
 KY  KE  GN  KN  OU  KN  GN  KE  KY  9
FU

"""
    shogi = Shogi()
    shogi.move((7, 7), (7, 6))
    shogi.move((4, 1), (4, 2))
    shogi.move((8, 8), (3, 3))
    actual = shogi.dump()
    assert expected == actual

def test_dump_with_mochigoma_2():
    expected = """Sente
  9   8   7   6   5   4   3   2   1
(KY)(KE)(GN)(KN)(OU) __ (GN)(KE)(KY) 1
 __ (HI) __  __  __  __  __ (KK) __  2
(FU)(FU)(FU)(FU)(FU)(FU)(KN)(FU)(FU) 3
 __  __  __  __  __  __  __  __  __  4
 __  __  __  __  __  __  __  __  __  5
 __  __  FU  __  __  __  __  __  __  6
 FU  FU  __  FU  FU  FU  FU  FU  FU  7
 __  __  __  __  __  __  __  HI  __  8
 KY  KE  GN  KN  OU  KN  GN  KE  KY  9
FU
KK
"""
    shogi = Shogi()
    shogi.move((7, 7), (7, 6))
    shogi.move((4, 1), (4, 2))
    shogi.move((8, 8), (3, 3))
    shogi.move((4, 2), (3, 3))
    actual = shogi.dump()
    assert expected == actual

def test_save():
    expected = """1
EDCBABCDE
 F     G 
HHHHHHHHH
         
         
         
hhhhhhhhh
 g     f 
edcbabcde


"""
    shogi = Shogi()
    actual = shogi.save()
    assert expected == actual

