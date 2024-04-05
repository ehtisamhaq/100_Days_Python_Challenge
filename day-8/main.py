# old calculator

preference = input(""" 
      "What do you want to do?"
      \033[32m +
      \033[33m -
      \033[33m *
      \033[37m / \033[0m
      """)

f_num= input("Give the first number: ")
s_num= input("Give the first number: ")

if preference == "+" :
    print(f_num+s_num)
elif preference == "-" :
    print(f_num-s_num)
elif preference == "*" :
    print(f_num*s_num)
elif preference == "/" :
    print(f_num/s_num)
else:
    print(f_num, s_num)