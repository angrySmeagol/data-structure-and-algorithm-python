# -*- coding: utf-8 -*-


class Board(object):
    def __init__(self):
        self.board = {}
        for i in xrange(1, 10):
            for j in xrange(-5, 6):
                if j != 0:
                    self.board['{}|{}'.format(i, j)] = None


class Piece(object):
    def __init__(self, col, row, army='red'):
        self.army = army
        self.col = col
        self.row = row

    @classmethod
    def init_piece(cls, *args, **kwargs):
        piece = cls(*args, **kwargs)
        return piece


class Soldier(Piece):
    """
    兵，卒
    """

    def target(self, board):
        assert isinstance(board, Board), '{} should be a instance of Board'.format(board)
        if self.army == 'red':
            if self.row > 0:
                if self.row == 2:
                    return [(self.col, self.row - 1)]
                if self.row == 1:
                    return [(self.col, self.row - 2)]
            else:
                resp = []
                if self.row - 1 > -6:
                    resp.append((self.col, self.row - 1))
                if self.col - 1 > 0:
                    resp.append((self.col - 1, self.row))
                if self.col + 1 < 10:
                    resp.append((self.col + 1, self.row))
                return resp
        else:
            if self.row < 0:
                if self.row == -2:
                    return [(self.col, self.row + 1)]
                if self.row == -1:
                    return [(self.col, self.row + 2)]
            else:
                resp = []
                if self.row + 1 < 6:
                    resp.append((self.col, self.row + 1))
                if self.col - 1 > 0:
                    resp.append((self.col - 1, self.row))
                if self.col + 1 < 10:
                    resp.append((self.col + 1, self.row))


class Cannon(Piece):
    """
    炮
    """

    def target(self, board):
        assert isinstance(board, Board), '{} should be a instance of Board'.format(board)
        resp = []

        # 上下左右

        def run(start, end, step, horizon=False):
            jump = False
            if not horizon:
                for i in range(start, end, step):
                    col = self.col
                    row = self.row + i
                    key = "{}|{}".format(col, row)
                    if self.row + i == 0:
                        continue
                    if -5 <= row <= 5:
                        if board.board[key] and not jump:
                            jump = True
                            continue
                        if (not jump) and (not board.board[key]):
                            resp.append((col, row))
                        elif jump and board.board[key] and board.board[key].army != self.army:
                            resp.append((col, row))
                            break
                    else:
                        break
            else:
                for i in range(start, end, step):
                    col = self.col + i
                    row = self.row
                    key = "{}|{}".format(col, row)
                    if 1 <= col <= 9:
                        if board.board[key] and not jump:
                            jump = True
                            continue
                        if (not jump) and (not board.board[key]):
                            resp.append((col, row))
                        elif jump and board.board[key] and board.board[key].army != self.army:
                            resp.append((col, row))
                            break
                    else:
                        break

        run(-1, -11, -1)
        run(1, 11, 1)
        run(1, 9, 1, True)
        run(-1, -9, -1, True)

        return resp


class Vehicle(Piece):
    """
    车
    """

    def target(self, board):
        assert isinstance(board, Board), '{} should be a instance of Board'.format(board)
        resp = []

        # 上下左右

        def run(start, end, step, horizon=False):
            if not horizon:
                for i in range(start, end, step):
                    col = self.col
                    row = self.row + i
                    key = "{}|{}".format(col, row)
                    if self.row + i == 0:
                        continue
                    if -5 <= row <= 5:
                        if board.board[key]:
                            if board.board[key].army != self.army:
                                resp.append((col, row))
                                break
                            else:
                                break
                        else:
                            resp.append((col, row))
                    else:
                        break
            else:
                for i in range(start, end, step):
                    col = self.col + i
                    row = self.row
                    key = "{}|{}".format(col, row)
                    if 1 <= col <= 9:
                        if board.board[key]:
                            if board.board[key].army != self.army:
                                resp.append((col, row))
                                break
                            else:
                                break
                        else:
                            resp.append((col, row))
                    else:
                        break

        run(-1, -11, -1)
        run(1, 11, 1)
        run(1, 9, 1, True)
        run(-1, -9, -1, True)
        return resp


class Horse(Piece):
    """
    马
    """

    def target(self, board):
        assert isinstance(board, Board), '{} should be a instance of Board'.format(board)
        resp = []
        # 下
        row = self.row + 1 if self.row + 1 != 0 else self.row + 2
        if -4 <= row <= 4:
            if not board.board["{}|{}".format(self.col, row)]:
                row += 1
                col = self.col + 1
                if 1 <= col <= 9:
                    key = "{}|{}".format(col, row)
                    if not board.board[key] or board.board[key].army != self.army:
                        resp.append((col, row))
                col = self.col - 1
                if 1 <= col <= 9:
                    key = "{}|{}".format(col, row)
                    if not board.board[key] or board.board[key].army != self.army:
                        resp.append((col, row))
        # 上
        row = self.row - 1 if self.row - 1 != 0 else self.row - 2
        if -4 <= row <= 4:
            if not board.board["{}|{}".format(self.col, row)]:
                row -= 1
                col = self.col + 1
                if 1 <= col <= 9:
                    key = "{}|{}".format(col, row)
                    if not board.board[key] or board.board[key].army != self.army:
                        resp.append((col, row))
                col = self.col - 1
                if 1 <= col <= 9:
                    key = "{}|{}".format(col, row)
                    if not board.board[key] or board.board[key].army != self.army:
                        resp.append((col, row))
        # 右
        col = self.col - 1
        if 2 <= col <= 8:
            if not board.board["{}|{}".format(col, self.row)]:
                col -= 1
                row = self.row + 1
                if -5 <= row <= 5:
                    key = "{}|{}".format(col, row)
                    if not board.board[key] or board.board[key].army != self.army:
                        resp.append((col, row))
                row = self.row - 1
                if -5 <= row <= 5:
                    key = "{}|{}".format(col, row)
                    if not board.board[key] or board.board[key].army != self.army:
                        resp.append((col, row))
        # 左
        col = self.col + 1
        if 2 <= col <= 8:
            if not board.board["{}|{}".format(col, self.row)]:
                col += 1
                row = self.row + 1
                if -5 <= row <= 5:
                    key = "{}|{}".format(col, row)
                    if not board.board[key] or board.board[key].army != self.army:
                        resp.append((col, row))
                row = self.row - 1
                if -5 <= row <= 5:
                    key = "{}|{}".format(col, row)
                    if not board.board[key] or board.board[key].army != self.army:
                        resp.append((col, row))
        return resp


class Minister(Piece):
    """
    象
    """

    def target(self, board):
        assert isinstance(board, Board), '{} should be a instance of Board'.format(board)
        resp = []
        # 下
        row = self.row + 1
        if self.army == 'red':
            if 2 <= row <= 4:
                col = self.col + 1
                if not board.board["{}|{}".format(col, self.row + 1)]:
                    col += 1
                    row = self.row + 2
                    key = "{}|{}".format(col, row)
                    if (not board.board[key]) or board.board[key].army != self.army:
                        resp.append((col, row))
                col = self.col - 1
                if not board.board["{}|{}".format(col, self.row + 1)]:
                    col -= 1
                    row = self.row + 2
                    key = "{}|{}".format(col, row)
                    if (not board.board[key]) or board.board[key].army != self.army:
                        resp.append((col, row))
        else:
            if -2 <= row <= -4:
                col = self.col + 1
                if not board.board["{}|{}".format(col, self.row + 1)]:
                    col += 1
                    row = self.row + 2
                    key = "{}|{}".format(col, row)
                    if (not board.board[key]) or board.board[key].army != self.army:
                        resp.append((col, row))
                col = self.col - 1
                if not board.board["{}|{}".format(col, self.row + 1)]:
                    col -= 1
                    row = self.row + 2
                    key = "{}|{}".format(col, row)
                    if (not board.board[key]) or board.board[key].army != self.army:
                        resp.append((col, row))
        # 上
        row = self.row - 1
        if self.army == 'red':
            if 2 <= row <= 4:
                col = self.col + 1
                if not board.board["{}|{}".format(col, self.row - 1)]:
                    col += 1
                    row = self.row - 2
                    key = "{}|{}".format(col, row)
                    if (not board.board[key]) or board.board[key].army != self.army:
                        resp.append((col, row))
                col = self.col - 1
                if not board.board["{}|{}".format(col, self.row - 1)]:
                    col -= 1
                    row = self.row - 2
                    key = "{}|{}".format(col, row)
                    if (not board.board[key]) or board.board[key].army != self.army:
                        resp.append((col, row))
        else:
            if -2 <= row <= -4:
                col = self.col + 1
                if not board.board["{}|{}".format(col, self.row - 1)]:
                    col += 1
                    row = self.row - 2
                    key = "{}|{}".format(col, row)
                    if (not board.board[key]) or board.board[key].army != self.army:
                        resp.append((col, row))
                col = self.col - 1
                if not board.board["{}|{}".format(col, self.row - 1)]:
                    col -= 1
                    row = self.row - 2
                    key = "{}|{}".format(col, row)
                    if (not board.board[key]) or board.board[key].army != self.army:
                        resp.append((col, row))
        return resp


class Guard(Piece):
    """
    士
    """

    def target(self, board):
        assert isinstance(board, Board), '{} should be a instance of Board'.format(board)
        resp = []
        temp = [(self.col - 1, self.row - 1), (self.col - 1, self.row + 1), (self.col + 1, self.row - 1),
                (self.col + 1, self.row + 1)]
        temp = set(temp) & set([(4, 5), (4, 3), (6, 5), (6, 3), (5, 4), (4, -5), (4, -3), (6, -5), (6, -3), (5, -4)])
        for i in temp:
            key = "{}|{}".format(i[0], i[1])
            try:
                if (not board.board[key]) or (board.board[key].army != self.army):
                    resp.append(i)
            except:
                pass
        return resp


class Commander(Piece):
    """
    帅， 将
    """

    def target(self, board):
        assert isinstance(board, Board), '{} should be a instance of Board'.format(board)
        resp = []
        # 上下
        row = self.row - 1
        if self.army == 'red':
            if 3 <= row <= 5:
                key = "{}|{}".format(self.col, row)
                if (not board.board[key]) or (board.board[key].army != self.army):
                    resp.append((self.col, row))
        else:
            if -3 <= row <= -5:
                key = "{}|{}".format(self.col, row)
                if (not board.board[key]) or (board.board[key].army != self.army):
                    resp.append((self.col, row))
        row = self.row + 1
        if self.army == 'red':
            if 3 <= row <= 5:
                key = "{}|{}".format(self.col, row)
                if (not board.board[key]) or (board.board[key].army != self.army):
                    resp.append((self.col, row))
        else:
            if -3 <= row <= -5:
                key = "{}|{}".format(self.col, row)
                if (not board.board[key]) or (board.board[key].army != self.army):
                    resp.append((self.col, row))

        # 左右
        def commander_see_each(col):
            if self.army == 'red':
                for i in range(-1, -10, -1):
                    try:
                        key = "{}|{}".format(col, self.row + i)
                        if board.board[key] and (not isinstance(board.board[key], Commander)):
                            break
                        elif board.board[key] and isinstance(board.board[key], Commander):
                            return True
                    except:
                        break
                return False

        col = self.col + 1
        if 4 <= col <= 6:
            key = "{}|{}".format(col, self.row)
            if not commander_see_each(col) and ((not board.board[key]) or (board.board[key].army != self.army)):
                resp.append((col, self.row))
        col = self.col - 1
        if 4 <= col <= 6:
            key = "{}|{}".format(col, self.row)
            if not commander_see_each(col) and ((not board.board[key]) or (board.board[key].army != self.army)):
                resp.append((col, self.row))
        return resp


class Army(object):
    def __init__(self, color='red'):
        self.pieces = []
        self.color = color
        self.stand_on = None

        j = 2 if color == 'red' else -2
        k = 3 if color == 'red' else -3
        l = 5 if color == 'red' else -5
        for i in range(1, 10, 2):
            self.pieces.append(Soldier.init_piece(i, j, color))
        for i in (2, 8):
            self.pieces.append(Cannon.init_piece(i, k, color))
        for i in (1, 9):
            self.pieces.append(Vehicle.init_piece(i, l, color))
        for i in (2, 8):
            self.pieces.append(Horse.init_piece(i, l, color))
        for i in (3, 7):
            self.pieces.append(Minister.init_piece(i, l, color))
        for i in (4, 6):
            self.pieces.append(Guard.init_piece(i, l, color))
        self.pieces.append(Commander.init_piece(5, l, color))

    def army_stand_on_the_board(self, board):
        assert isinstance(board, Board), '{} should be Board Class'.format(board)

        for piece in self.pieces:
            board.board["{}|{}".format(piece.col, piece.row)] = piece
        self.stand_on = board

    def get_target_list(self, piece):
        assert piece in self.pieces, '{} is not a piece of mine army'
        return piece.target(self.stand_on)




class Game(object):
    def __init__(self):
        self.board = Board()
        self.red = Army('red')
        self.blue = Army('blue')
        self.red.army_stand_on_the_board(self.board)
        self.blue.army_stand_on_the_board(self.board)

    def play(self, piece, target):
        self.board.board["{}|{}".format(piece.col, piece.row)] = None
        piece.col, piece.row = target
        over = False
        if piece.army == 'red':
            for i in self.blue.pieces:
                if (i.col, i.row) == target:
                    self.blue.pieces.remove(i)
                    if isinstance(i, Commander):
                        over = True
                    break
        else:
            for i in self.red.pieces:
                if (i.col, i.row) == target:
                    self.red.pieces.remove(i)
                    if isinstance(i, Commander):
                        over = True
                    break
        self.board.board["{}|{}".format(target[0], target[1])] = piece
        if over:
            return False
        return True
