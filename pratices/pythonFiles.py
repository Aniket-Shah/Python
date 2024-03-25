# s = "Aniket is an anime toy story"
#Writing to a file
# with open("test.txt", "w") as f:
#     f.write(s)
#
# fp = open("test.txt", "w")
# fp.write(s)
# fp.close()


#Reading to a file
with open("test.txt", "r") as f:
    s=f.read()
    print (s)
# fp = open("test.txt", "w")
# fp.write(s)
# fp.close()