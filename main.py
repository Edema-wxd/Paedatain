import openpyxl


raw = openpyxl.load_workbook("C:\\Users\\USER\\Desktop\\Copy.xlsx")

print(raw.sheetnames)

octo = raw["OCT 21"]
print(octo)

flow = 1

while flow == 1:
    name = input("Patient Name:")
    temp = float(input("Temp"))
    simps = input("Does the patient have symptoms (y/n): ")
    if simps == "n":
        simsval = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    else:
        break
    final = [0, name, temp] + simsval
    for i in final:
        octo.append(i)

    print(final)
    cont = input("continue(y/n):")
    if cont == "n":
        flow = 0

raw.save("C:\\Users\\USER\\Desktop\\Copy.xlsx")
print("done")
