genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 2500]

# 일단 genre (sum of the same genre) 별로 count 를 비교하고 가장 인기많은 genre 안에서 또 가장 인기있는 2개의 index 를 앞에 넣는다.
# 두번째 인기의 genre 안에서, 즉, 똑같은 genre 들중 가장 인기많은 두개를 다음에 넣어준다...

def get_melon_best_album(genre_array, play_array):
    n = len(genre_array)
    genre_total_play_dict = {} # genre 별 count total so {'classic': 1450, 'pop': 3100}
    genre_index_play_array_dict = {} # genre 안에서 ordered number
    for i in range(n):
        genre = genre_array[i]
        play = play_array[i]
        if genre not in genre_total_play_dict:
            genre_total_play_dict[genre] = play # 그 genre 가 존재하지 않는다면 add new key & value
            genre_index_play_array_dict[genre] = [[i, play]]
        else:
            genre_total_play_dict[genre] += play # 그 genre 가 존재한다면 add value to that key.
            genre_index_play_array_dict[genre].append([i, play])

    print(genre_total_play_dict)
    # {'classic': 1450, 'pop': 3100} 이 출력됩니다!
    print(genre_index_play_array_dict)
    # {'classic': [[0, 500], [2, 150], [3, 800]], 'pop': [[1, 600], [4, 2500]]} 이 출력됩니다!

    # 여기까지 장르별 총 곡의 재생횟수와 장르별 곡의 인덱스와 재생 수를 저장했습니다!
    # 가장 재생수가 높은 장르: genre_total_play_dict 을 sort 한다

    # 딕셔너리의 키 - 값을 배열 형태로 추출하는 방법 : convert dictionary to array in order to sort
    # dict.items() 함수

    # when using sort on arrayified dictionary! need to specifiy either you want to sort by Key or Value
    # sorted(genre_total_play_dict.items(), key = lambda items: item[0]) // by key so "classic"
    # sorted(genre_total_play_dict.items(), key = lambda items: item[1]) // by value so "1450"
    # 내림차순은 reverse = True
    # sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)

    # 어떤것을 정렬할지에대해 정해주는 sorted 함수의 key 부분에서 lambda 라는 python 문법을 쓰는데
    # 현재 genre_total_play_dict 의 각 원소는 [인덱스, 플레이 수] 형태의 배열이다
    # 이중 어떤걸 기준으로 정렬할것이냐 를 정해주는 코드이다. : 파이썬의 lambda

    ...
    # sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    # print(sorted_genre_play_array)
    # 그러면 이렇게 밸류값을 기준으로 정렬할 수 있습니다!
    # [('pop', 3100), ('classic', 1450)]
    ...

    sorted_genre_play_array = sorted(genre_total_play_dict.items(), key=lambda item: item[1], reverse=True)
    # [('hiphop', 4000), ('pop', 3100), ('classic', 1450)]
    result = []
    for genre, _value in sorted_genre_play_array:
        # genre_index_play_array_dic: Before: {'classic': [[0, 500], [2, 150], [3, 800]], 'pop': [[1, 600], [4, 2500]]}
        index_play_array = genre_index_play_array_dict[genre] # 위의 dic 에서 index 와 playtime 을 가져온다.
        sorted_by_play_and_index_play_index_array = sorted(index_play_array, key=lambda item: item[1], reverse=True) #두번째 값 (플레이 수) 으로 정렬
        for i in range(len(sorted_by_play_and_index_play_index_array)): # 한 genre 당 2개씩 result 에 넣기
            if i > 1:
                break
            result.append(sorted_by_play_and_index_play_index_array[i][0]) # Index 를 반환 #[[4, 800], [1, 500], [3, 150]] -> [i][0] -> [0][0] = 800 [1][0] -> 500 //

    return result

print("정답 = [4, 1, 3, 0] / 현재 풀이 값 = ", get_melon_best_album(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
print("정답 = [0, 6, 5, 2, 4, 1] / 현재 풀이 값 = ", get_melon_best_album(["hiphop", "classic", "pop", "classic", "classic", "pop", "hiphop"], [2000, 500, 600, 150, 800, 2500, 2000]))