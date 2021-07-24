class PitcherStats:
    def __init__(self, name, team, pos, ip, h, er, bb, k, cg, nh, pg, w, l, hbp, hr, sv, holds):
        self.name = name
        self.team= team
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
        self.holds= holds

    def espnscoring():
        return ((ip*3)+
                (h*-1)+
                (er*-2)+
                (bb*-1)+
                (k)+
                (cg*3)+
                (ng*4)+
                (pg*5)+
                (w*5)+
                (l*-3)+
                (sv*3))

    def ottoneu(self):
        return ((ip*7.4)+
                (k*2)+
                (h*-2.6)+
                (bb*-3)+
                (hbp*-3)+
                (hr*-12.3)+
                (sv*5)+
                (holds*4))