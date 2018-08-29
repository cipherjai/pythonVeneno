# using map to solve the str dictionary

# g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
# ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj.

t = input()

# t = input().split(' ')
# print(t)
#
#
# def changer(words):
#     fin = ""
#     for w in words:
#         if 97 <= ord(w) <= 122:
#             if ord(w) == 121:
#                 fin += 'a'
#             elif ord(w) == 122:
#                 fin += 'b'
#             else:
#                 fin += chr(ord(w) + 2)
#         else:
#             fin += w
#     return fin+" "
#
#
# str1 = ''.join(list(map(changer, t)))
# print(str1)


# // better way

intab = "abcdefghijklmnopqrstuvwxyz"
outab = "cdefghijklmnopqrstuvwxyzab"
trantab = str.maketrans(intab, outab)
print(t.translate(trantab))

