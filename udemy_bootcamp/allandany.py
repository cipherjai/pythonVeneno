# if all the iterable items are tue , then returns a true
# if any of the iterable items are true , then returns true

# all() and any()

"""
    def all(iterable):
        for element in iterable:
            if not element:
                :return False
            :return True
"""
# com
# def any(iterable):
#     for element in iterable:
#         if element:
#             return True
#             break
#
#     return False

li = [True, False, True, False, False, False, False]
print(all(li))
print(any(li))
