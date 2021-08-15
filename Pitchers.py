class PitcherStats:
    def __init__(self, name, team, pos, ip, h, er, bb, k, cg, nh, pg, w, l, hbp, hr, sv, holds, bs, qs, so):
        self.so = so
        self.qs = qs
        self.name = name
        self.team = team
        self.pos = pos
        self.ip = ip
        self.k = k
        self.h = h
        self.bb = bb
        self.cg = cg
        self.nh = nh
        self.pg = pg
        self.w = w
        self.l = l
        self.hbp = hbp
        self.sv = sv
        self.holds = holds
        self.bs = bs

    def espnscoring():
        return ((ip * 3) +
                (h * -1) +
                (er * -2) +
                (bb * -1) +
                (k) +
                (cg * 3) +
                (ng * 4) +
                (pg * 5) +
                (w * 5) +
                (l * -3) +
                (sv * 3))

    def ottoneu(self):
        return ((ip * 7.4) +
                (k * 2) +
                (h * -2.6) +
                (bb * -3) +
                (hbp * -3) +
                (hr * -12.3) +
                (sv * 5) +
                (holds * 4))

    def cbs(self):
        return ((bs * 5) +
                (cg * 5) +
                (er * -1) +
                (ip) +
                (k) +
                (l * - 5) +
                (nh * 10) +
                (pg * 15) +
                (qs * 5) +
                (s * 9) +
                (so * 5) +
                (w * 10))
