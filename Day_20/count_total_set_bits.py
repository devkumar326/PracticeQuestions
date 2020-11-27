
def CountBits(n):
    n+=1 
    count_set_bits = n//2 
    power_of_2 = 2 
    
    while power_of_2 <= n:
        total_group_of_0_and_1 = n // power_of_2
        total_group_set_bits = total_group_of_0_and_1//2 
        count_set_bits += total_group_set_bits * power_of_2 
        
        if total_group_of_0_and_1 & 1 == 1:
            count_set_bits += n % power_of_2
            
        power_of_2 <<= 1
    
    return count_set_bits

if __name__=="__main__":
    for _ in range(int(input())):
        print(CountBits(int(input())))