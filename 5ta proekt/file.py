inp = input("faylga nom berish= ")
text = input("faylni ichiga biron nima yozing : ")
file = open(f"{inp}", 'w')
start = file.write(f"{text}")
