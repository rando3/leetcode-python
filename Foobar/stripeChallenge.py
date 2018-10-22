# Complete the balance function below.
from urllib.parse import urlparse

def balance(lines):
    bal = {}
    ret_bal = []
    cnt = 0
    for i, line in enumerate(lines):
        if line[:4] == "API:":
            param_split = line[5:].split("&")
            amt = int(param_split[0].split("=")[1])
            merch = param_split[1].split("=")[1]
            striped_amt = stripe(amt)
            # print(striped_amt)
            if len(param_split) == 2:
                if merch not in bal:
                    bal[merch] = striped_amt
                else:
                    bal[merch] += striped_amt
            else:
                dest_act = param_split[2].split("=")[1]
                dest_amt = int(param_split[3].split("=")[1])
                merch_amt = striped_amt - dest_amt
                if dest_act not in bal:
                    bal[dest_act] = dest_amt
                else:
                    bal[dest_act] += dest_amt
                if merch not in bal:
                    bal[merch] = merch_amt
                else:
                    bal[merch] += merch_amt
        else:
            cnt += 1
            merch = line[5:].split("=")[1]
            if merch in bal:
                ret_bal.append(bal[merch])
            else:
                ret_bal.append(0)
    if len(ret_bal) != cnt:
        print("HEY!")
    return ret_bal

def stripe(amt):
    return round(0.971 * amt) - 30

if __name__ == "__main__":
    print(stripe)


