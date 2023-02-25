shop_prices = [30000, 2000, 1500000]
user_coupons = [20, 40]

# 어떻게 해야 가장 할인액이 많을 수 있을까요?
# 바로, 가장 비싼 금액이 가장 많이 할인을 받으면 됩니다.
# 엇, 그렇다면 바로 정렬된 데이터들이 필요합니다!
# 정렬을 하기 위해서는 우리가 배웠던 아무 정렬을 사용해도 되지만!!!!!
# 저희는 이제 기본적인 정렬을 배웠으니, .sort 라는 함수를 사용할 자격이 생겼습니다.
#
# 그러면 이제 정렬을 했으니 반복문을 쓰..면 안되고!
# user_coupons 의 개수와 shop_prices 개수가 다를 수 있습니다!
# 따라서 아래와 같이 while 문과 인덱스를 사용해서 해결해야 합니다.
#
# 이 때, 할인율! 이라는 점도 깜빡하시면 안 됩니다.
# (100 - coupons[coupon_index]) / 100 이라는 연산을 통해 얼마나 할인 시킬 수 있는지를
# 계산해주셔야 됩니다!

def get_max_discounted_price(prices, coupons):
    # 이 곳을 채워보세요!
    # 내림차순정렬 (reverse = True)
    coupons.sort(reverse=True)
    prices.sort(reverse= True)
    price_index = 0
    coupon_index = 0
    max_discounted_price = 0

# 할인율 적용: 비싼값이 가장 큰 쿠폰할인율을 받는다
    while price_index < len(prices) and coupon_index < len(coupons):
        max_discounted_price += prices[price_index] * (100 - coupons[coupon_index]) / 100
        price_index += 1
        coupon_index += 1
# 할인율을 적용받지 못한 나머지 가격을 더하여준다
    while price_index < len(prices):
        max_discounted_price += prices[price_index]
        price_index += 1

    return max_discounted_price


print("정답 = 926000 / 현재 풀이 값 = ", get_max_discounted_price([30000, 2000, 1500000], [20, 40]))
print("정답 = 485000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], [10, 70, 30, 20]))
print("정답 = 1550000 / 현재 풀이 값 = ", get_max_discounted_price([50000, 1500000], []))
print("정답 = 1458000 / 현재 풀이 값 = ", get_max_discounted_price([20000, 100000, 1500000], [10, 10, 10]))
