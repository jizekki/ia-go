import eval


class AlphaBeta():

    def __init__(self, color):
        self.maCouleur = color
        self.noeuds = 0
        self.scoremax = 100000
        self.evaluation = eval.Eval(color)

    def AlphaBetaCoup(self, b, depth, turn):
        """ Premier niveau de Minmax avec Alpha Beta """
        if b.is_game_over() or depth == 0:
            return None

        v, coup = None, None
        self.noeuds = 0
        for m in b.generate_legal_moves():
            # éviter les bordures prendant premiers tours du jeu.
            if (turn < 15):
                x, y = b.unflatten(m)
                if (not (x < 1 or y < 1 or x >= b._BOARDSIZE-1 or y >= b._BOARDSIZE-1)):
                    b.push(m)

                    ret = self.AlphaBeta(
                        b, depth - 1, -self.scoremax, self.scoremax)

                    if v is None or ret > v:
                        coup = m
                        v = ret
                    b.pop()
                    self.noeuds += 1
            else:
                b.push(m)

                ret = self.AlphaBeta(
                    b, depth - 1, -self.scoremax, self.scoremax)

                if v is None or ret > v:
                    coup = m
                    v = ret
                b.pop()
                self.noeuds += 1
        return (coup, v)

    def AlphaBeta(self, b, depth, alpha, beta):
        self.noeuds += 1

        """ MinMax avec Alpha beta pruning"""
        if b.is_game_over():
            res = b.result()
            if res == "1-0":
                r = - ((-1)**self.maCouleur) * self.scoremax
            elif res == "0-1":
                r = ((-1)**self.maCouleur) * self.scoremax
            else:
                r = 0
            return r

        if depth == 0:
            self.evaluation = eval.Eval(self.maCouleur)
            e = self.evaluation.evaluate(b)
            return e

        v = None
        for move in b.generate_legal_moves():
            b.push(move)
            ret = self.BetaAlpha(b, depth-1, alpha, beta)
            b.pop()
            if v is None or ret < v:
                v = ret
            if beta > v:
                beta = v

            if alpha >= beta:
                return alpha

        return beta

    def BetaAlpha(self, b, depth, alpha, beta):
        self.noeuds += 1
        """ MaxMin avec Alpha beta pruning"""
        if b.is_game_over():
            resultat = b.result()
            if resultat == "1-0":
                r = - ((-1)**self.maCouleur) * self.scoremax
            elif resultat == "0-1":
                r = ((-1)**self.maCouleur) * self.scoremax
            else:
                r = 0
            return r

        if depth == 0:
            self.evaluation = eval.Eval(self.maCouleur)
            e = self.evaluation.evaluate(b)
            return e

        v = None
        for m in b.generate_legal_moves():
            b.push(m)
            ret = self.AlphaBeta(b, depth - 1, alpha, beta)
            b.pop()
            if v is None or ret > v:
                v = ret
            if alpha < v:
                alpha = v
            if alpha >= beta:
                return beta
        return alpha
