import pandas as pd

class Backtester:
    def __init__(self, data, long_threshold=0.6, liquidate_threshold=0.2, short_threshold=-0.5):
        self.long_threshold = long_threshold
        self.liquidate_threshold = liquidate_threshold
        self.short_threshold = short_threshold
        self.df = data.copy()
        self.df['position'] = 0
        self.df['pnl'] = 0.0
        self.df['balance'] = 0.0 
        self.current_balance = 0.0
        self.entry_price = 0.0
        self.current_position = 0

    def static_threshold_strategy(self, alpha):
        if self.current_position == 0:
            if alpha >= self.long_threshold:
                self.current_position = 1
            elif alpha <= self.short_threshold:
                self.current_position = -1
        elif self.current_position == 1:
            if alpha <= self.liquidate_threshold:
                self.current_position = 0
            elif alpha <= self.short_threshold:
                self.current_position = -1
        elif self.current_position == -1:
            if alpha >= self.liquidate_threshold:
                self.current_position = 0
            elif alpha >= self.long_threshold:
                self.current_position = 1
        return self.current_position

    def apply_strategy(self):
        self.df['position'] = self.df['alpha'].apply(self.static_threshold_strategy)
        self.df.loc[self.df.index[-1], 'position'] = 0  # Liquidate position at the end of the period

    def calculate_pnl(self):
        self.apply_strategy()
        prev_pos = 0

        for i in range(len(self.df)):
            curr_pos = self.df.loc[i, 'position']

            if prev_pos == 0 and curr_pos != 0:
                self.entry_price = self.df.loc[i, 'price']
                pnl = 0
                prev_pos = curr_pos
                
            elif prev_pos != 0 and curr_pos == 0:
                if prev_pos == 1:  # Long position
                    pnl = self.df.loc[i, 'price'] - self.entry_price
                elif prev_pos == -1:  # Short position
                    pnl = self.entry_price - self.df.loc[i, 'price']
                else:
                    pnl = 0
                self.df.loc[i, 'pnl'] = pnl
                self.current_balance += pnl
                prev_pos = curr_pos

            elif prev_pos != 0 and curr_pos != 0:
                if prev_pos == 1 and curr_pos == -1:  # From Long to Short position
                    pnl = self.df.loc[i, 'price'] - self.entry_price
                    self.entry_price = self.df.loc[i, 'price']
                elif prev_pos == -1 and curr_pos == 1:  # From Short to Long position
                    pnl = self.entry_price - self.df.loc[i, 'price']
                    self.entry_price = self.df.loc[i, 'price']
                else:
                    pnl = 0
                self.df.loc[i, 'pnl'] = pnl
                self.current_balance += pnl
                prev_pos = curr_pos

            self.df.loc[i, 'balance'] = self.current_balance

    def run(self):
        self.calculate_pnl()

    def get_pnl(self):
        return self.current_balance