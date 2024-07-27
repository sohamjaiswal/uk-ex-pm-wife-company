numRows = int(input("Enter the number of rows: "))
def acceptCols():
    colStr = input("Enter the 2 columns: ")
    try:
        col1, col2 = map(int, colStr.split())
        return [col1, col2]
    except:
        print("Invalid input. Please try again.")
        return acceptCols()
matrice = [acceptCols() for _ in range(numRows)]
def navigate(rows):
    total = 0
    for i, row in enumerate(rows):
        if i == 0:
            total += max(row)
        else:
            betterVal = max(row[0], row[1])
            if betterVal > max(rows[i-1]):
                total += betterVal
            else:
                break
    return total
print(navigate(matrice))