# -*- coding: utf-8 -*-
"""
Connecting to KiteConnect API

@author: Mayank Rasu (http://rasuquant.com/wp/)
"""

from kiteconnect import KiteConnect
import pandas as pd

api_key = "vj15kaimhdw3x5yd"
api_secret = "bz87zihd4842w3ysuomjdqbte603c8mc"
kite = KiteConnect(api_key=api_key)
print(kite.login_url()) #use this url to manually login and authorize yourself

#generate trading session
request_token = "HSm0U8qM5yw09d73UcZfc5lny5HPbeKq" #Extract request token from the redirect url obtained after you authorize yourself by loggin in
data = kite.generate_session(request_token, api_secret=api_secret)

#create kite trading object
kite.set_access_token(data["access_token"])


#get dump of all NSE instruments
instrument_dump = kite.instruments("NSE")
instrument_df = pd.DataFrame(instrument_dump)
instrument_df.to_csv("NSE_Instruments.csv",index=False)