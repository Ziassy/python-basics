# throwing error
# try:
#    You do your operations here;
#    ......................
# except(Exception1[, Exception2[,...ExceptionN]]]):
#    If there is any exception from the given exception list,
#    then execute this block.
#    ......................
# else:
#    If there is no exception then execute this block.

ItemsInCart = 0
#2 items will be added to cart

if ItemsInCart != 2:
    # raise Exception('Products cart count not matching')
    pass

assert(ItemsInCart == 0)