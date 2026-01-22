# 1) შექმენით სახელებით სავსე სია, თუ სიტყვის ყველა ასო არის პატარა და პირველი ასო არის d, მაშინ ახალ სიაში ჩაამატეთ სახელი "NIKA", თუ სიტყვის ყველა ასო არის დიდი ან იწყება ასო K-თი, მაშინ სიაში ჩაამატეთ სახელი "GOGA", სხვა შემთხვევაში სიაში ჩაამატეთ სიტყვა "ლიდერი". დაპრინტეთ მიღებული სია.

names = ["dato", "TATA", "data", "LUKA", "koka", "giorgi"]
new_name = []

for i in names:
    if i.islower() and i.startswith('d'):
        new_name.append("NIKA")
    elif i.isupper() or i.startswith('K'):
        new_name.append("GOGA")
    else:
        new_name.append("ლიდერი")

print(new_name)