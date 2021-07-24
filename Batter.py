# This will be the OOP page to assign scores between both leagues, ESPN vs OTTONEU League





class BatterStats:
    def __init__(self, name, team, pos, ab, r, tb, rbi, bb, k, sb, cs, h, 2b, 3b, hr):
        self.name = name
        self.team = team
        self.pos = pos
        self.r = r
        self.tb = tb
        self.rbi = rbi
        self.bb = bb
        self.k = k
        self.sb = sb
        self.cs = cs
        self.ab = ab
        self.h = h
        self.2b = 2b
        self.3b = 3b
        self.hr = hr

    def espnscoring(self):
        return (r + tb + rbi + bb + sb) - (k + cs)

    def ottoneu(self):
        return ((ab * -1) +
                (5.6 * h) +
                (2b * 2.9) +
                (3b * 5.7) +
                (hr * 9.4) +
                (bb * 3) +
                (hbp * 3) +
                (sb * 1.9) -
                (cs * -2.8))