def kttamgiac(a, b, c):
    if a + b <= c or b + c <= a or a + c <= b:
        return "K phai tam giac"
    if a == b == c:
        return "Tam giac deu"
    if a == b or a == c or b == c:
        if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
            return "Tam giac vuong can"
        return "Tam giac can"
    if a**2 == b**2 + c**2 or b**2 == a**2 + c**2 or c**2 == a**2 + b**2:
        return "Tam giac vuong"
    return "Tam giac thuong"
a, b, c = sorted(map(float, input("Nhap do dai cac canh : ").split()))
print("Loai tam giac : ", kttamgiac(a, b, c))

