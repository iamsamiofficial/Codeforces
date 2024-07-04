# def main():
    
#     for _ in range(int(input())):
#         n = int(input())
        
#         s = str(n)
#         sz = len(s)
        
#         small = "01234"
#         large = "56789"
#         if small in s and large in s:
#             print("No")
#             continue
        
#         flag = False
#         sum_digits = 0
#         bad_total = 5 + 6 + 7 + 8 + 9
        
#         for i in range(sz - 1):
#             sum_digits += int(s[i])
#             if s[i] == '0':
#                 flag = True
        
#         if s[-1] == '9':
#             print("No")
#         elif sum_digits == bad_total:
#             print("No")
#         elif s[0] != '1':
#             print("No")
#         elif sz % 10 == 0:
#             print("No")
#         elif flag:
#             print("No")
#         else:
#             print("Yes")

# if __name__ == "__main__":
#     main()



