
try:
    a = 10
    b = 0
    c = a/b
    print(c)

except ZeroDivisionError as e:
    print("Exception occured => " + str(e))

except ValueError as e:
    print("Exception => "+ str(e))

except:
    print("Exception occured")

else:
    print("Program Excuted Successfully")

finally:
    print("Harman Ltd")