balls = [1, 2, 3, 4]
weapons = [11, 12, 3, 14]

for ball_idx,ball_val in enumerate(balls):
    print("ball : ",ball_val)
    for weapon_idx, weapon_val in enumerate(weapons):
        print("weapons : " , weapon_val)
        if ball_val == weapon_val: # 충돌 체크
            print("공과 무기가 충돌")
            break
    else:
        continue
    print("바깥 for 문 break")
    break

# 버그 원인 : 이중 for 문을 모두다 빠져나가는 break를 상정했지만 내부 for문만 빠져나가는 break문으로만 사용되었다.

# 해결방법 : if문과 비슷하게 for문에도 else: 를 사용할수 있다.
