#import theater_module
#theater_module.price(3)
#theater_module.morning_price(5)
#theater_module.soldier_price(1)

#줄여 쓸때

import theater_module as mv
mv.price(3)
mv.morning_price(5)
mv.soldier_price(1)


#from theater_module import*
#price(3)
#morning_price(5)
#soldier_price(1)

#from theater_module import price,morning_price
#morning_price(5)

from theater_module import soldier_price as price
price(1)