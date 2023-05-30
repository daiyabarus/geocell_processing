class AntennaProperties:
    def __init__(self, freq, site_isd):
        self.freq = freq
        self.site_isd = site_isd
        self.ant_bw = None
        self.ant_size = None

    def calculate_antenna_properties(self):
        if self.freq == 600:
            self.ant_bw = 15
            self.ant_size = self.site_isd / 4
        elif self.freq == 850:
            self.ant_bw = 25
            self.ant_size = self.site_isd / 4.5
        elif self.freq == 1900:
            self.ant_bw = 35
            self.ant_size = self.site_isd / 5
        elif self.freq == 2100:
            self.ant_bw = 45
            self.ant_size = self.site_isd / 5.5
        elif self.freq == 2500:
            self.ant_bw = 55
            self.ant_size = self.site_isd / 6
        elif self.freq == 3500:
            self.ant_bw = 65
            self.ant_size = self.site_isd / 6.5
        else:
            self.ant_bw = 70
            self.ant_size = 0.02
