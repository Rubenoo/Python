cijferICOR = int(8)
cijferPROG = int(7)
cijferCSN = int(8)
gemCijfer = float((cijferCSN + cijferICOR + cijferPROG) /3)
beloning = "$" + str(gemCijfer * 30)
line = "Mijn cijfer {:.2f} leveren een beloning op van {} op!".format(gemCijfer, beloning)
print(cijferPROG)
print(cijferCSN)
print(cijferICOR)
print(gemCijfer)
print(beloning)
print(line)
