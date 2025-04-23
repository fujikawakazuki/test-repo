import random


def guess_the_number():
    """1から100までの数当てゲーム"""
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    print("数当てゲームへようこそ！")
    print("1から100までの数を当ててください。")

    while guess != number_to_guess:
        try:
            guess_input = input("あなたの予想を入力してください: ")
            guess = int(guess_input)
            attempts += 1

            if guess < 1 or guess > 100:
                print("1から100までの数を入力してください。")
            elif guess < number_to_guess:
                print("もっと大きい数です！")
            elif guess > number_to_guess:
                print("もっと小さい数です！")
            else:
                print(f"おめでとうございます！ {attempts}回で正解しました！")
        except ValueError:
            print("有効な数値を入力してください。")


if __name__ == "__main__":
    guess_the_number()

