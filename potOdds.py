
def betting_percent(bet, pot):
        percent =  bet / (pot + bet) * 100
        floor_betting_percent = int(percent)
        return floor_betting_percent

def odds_ration(bet, pot):
        value = pot/bet
        floor_value = int(value)
        return floor_value


        
