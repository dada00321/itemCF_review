from random import randint

def recommend_for_item(M, item_id):
    item_score = M[str(item_id)] # dict
    '''
    x[0]: 對推薦 item 的 item2item 所在 row，依編號排序
    x[1]: 對推薦 item 的 item2item 所在 row，
          依出現次數(商品相關性)排序
    reverse=True: 遞減排序
    '''
    item_score = sorted(item_score.items(),
                        key=lambda x:x[1],
                        reverse=True)
    print(f"為您推薦與 item {item_id} 有關的商品:")
    for (item_id, co_occurence) in item_score:
        print(f"item {item_id} (契合度: {co_occurence})")
    #return item_score

def show_item2item(M):
    min_, max_ = 1, 10
    header = [i for i in range(min_, max_+1)]
    print(" "*3, *(f"{i:3d}" for i in header))
    #M = {int(k), v for k, v in M.items()}
    for k, v in sorted(M.items(), key=lambda x:int(x[0])):
        print(f"{k:3s}", end=' ')
        for i in range(min_, max_+1):
            if i in v.keys():
                print(f"{v[i]:3d}", end=' ')
            else:
                print(f"{0:3d}", end=' ')
        print()
    print()

def get_item2item_matrix(is_show=False):
    n_orders = 30
    orders = [get_random_order(6, 1, 10) for i in range(n_orders)]

    item2item_matrix = dict()
    for order in orders:
        item2item_matrix = count_for_order(item2item_matrix,\
                                           order)

    if is_show:
        print("item2item_matrix:")
        print(item2item_matrix)
    return item2item_matrix

def get_random_order(n_nums, min_, max_):
    result = list()
    while len(result) < n_nums:
        t = randint(min_, max_)
        if t not in result:
            result.append(t)
    result.sort()
    #print(result)
    return sorted(result)

def count_for_order(M, order):
    for id_ in order:
        M.setdefault(str(id_), dict())
        # 自己的回合不將自己算進 item2item
        for other_id in set(order)-{id_}:
            M[str(id_)].setdefault(other_id, 0)
            M[str(id_)][other_id] += 1
    #print(M)
    return M

if __name__ == "__main__":
    #order_1 = [2,3,5,7,8,10]
    #count_for_order(order_1)
    #get_random_order(6, 1, 10)
    #item2item_demo()
    M = get_item2item_matrix(is_show=False)
    show_item2item(M)
    recommend_for_item(M, 3)
