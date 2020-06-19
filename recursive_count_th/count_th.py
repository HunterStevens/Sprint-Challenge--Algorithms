'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    count = 0
    arr=[]
    #convert the 'word' into an array
    if type(word) is str:
        arr = list(word)
        # print(f"arr: {arr}")
    else:
        arr = word
    #check if the arr is reduced to its end
    if len(arr) < 3:
        return 0
    else:
        #check if a t is in the remainding arr along with and h next to it
        if 't' in arr:
            t_ind = arr.index('t')
            # print(f"t_ind {t_ind}")
            if t_ind == len(arr)-1:
                return 0
            elif arr[t_ind +1] == 'h':
                #add to the counter if it exists and remove the 'th'
                count += 1
                arr.remove('t')
                arr.remove('h')
                # print(arr)
            #remove the stranding 't' that does not have the 'h' next to it.
            else:
                arr.remove('t')
        else:
            return 0
    #recursive do this till it runs out of 'th' to find
    return count + count_th(arr)

print(count_th("abcthefthghith"))