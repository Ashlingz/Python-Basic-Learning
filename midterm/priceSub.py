from msvcrt import getch
def productInput():
    p1 = float(input("Enter p1 = $"))
    p2 = float(input("Enter p2 = $"))
    p3 = float(input("Enter p3 = $"))
    discount = float(input("Enter Discount = %"))
    return p1,p2,p3,discount


def calculator(p1,p2,p3,discount):
    sub_total = p1+p2+p3
    discount_amount = sub_total *(discount/100)
    grand_total = sub_total-discount_amount
    return sub_total,discount_amount,grand_total



def output(sub_total,discount_amount,grand_total):
    print("-----------------")
    print(f"Sub Total: {sub_total}")
    print(f"Discount Amount: {discount_amount}")
    print(f"Grand Total: {grand_total}")


p1,p2,p3,discount=productInput()
sub_total,discount_amount,grand_total=calculator(p1,p2,p3,discount)
output(sub_total,discount_amount,grand_total)
getch()