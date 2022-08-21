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

try:
    with open('filelog.txt', 'r') as reader:
        reader.read()
# message error will represent by e and print the error message
except Exception as e :
    print(e) #[Errno 2] No such file or directory: 'filelog.txt'
