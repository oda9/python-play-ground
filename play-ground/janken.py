# -*- coding: utf-8 -*-
import sys
import random

JANKEN = {"p":"パー", "c":"チョキ", "g":"グー"}

def main(player):

    if player != "p" and player != "c" and player != "g":
         print("正しい文字を入力してください。")

    else:
        cpu  = ["p", "c", "g"][random.randint(0, 2)]
        print("あなたの手は" + JANKEN[player] + "です。")
        print("相手の手は" + JANKEN[cpu] + "です。")

        if player == cpu:
            print("あいこです。")

        elif (player == "p" and cpu == "g") or (player == "c" and cpu == "p") or (player == "g" and cpu == "c"):
            print("あなたのかちです。")

        else:
            print("あなたのまけです。")
    print("---------------------------")

if __name__ == '__main__':

    print("じゃんけんをはじめます。")

    while(True):
        print("パー：p　チョキ：c　グー：g　おわり：e")

        player = input()
        if player == "e":
            print("おわり")
            sys.exit()

        main(player)