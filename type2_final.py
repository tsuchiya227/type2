def main():
    # 昇順にソートされた配列
    sorted_array = [1, 2, 3, 5, 12, 7890, 12345]
    # 探索対象の番号
    target_number = 7890
    # 探索実行
    target_index = serch_index(sorted_array, target_number)
    # 結果出力
    print(target_index)

def serch_index(sorted_array, target_number):

    # ここから記述
    result = 0
    copy_array = sorted_array

    while len(sorted_array) > 1:
        sorted_array, result_add = new_array(sorted_array, target_number)
        result += result_add
        #新しい配列とresultの確認
        #print(sorted_array, result)

    #配列が1になったときにそれがtarget_numberと等しいか判断(copy_arrayを使う場合)
    if copy_array[result] == target_number:
        return result
    # 探索対象が存在しない場合、-1を返却
    else:
        return -1


#中央値のインデックス取得(与えられた配列が偶数のときは中央値の大きい方)
def off_set(array):
    length = len(array)
    return length//2

#新しい配列の作成
def new_array(array, target_number):
    off = off_set(array)
    if target_number == array[off]:
        array = [array[off]]
        result = off
    elif target_number > array[off]:
        array = array[off+1:]
        result = off+1
    elif target_number < array[off]:
        array = array[:off]
        result = 0
    return array, result

#ここまで記述

if __name__ == '__main__':
    main()