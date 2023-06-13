# # クラス(データ型)の定義
# class UserName:
#     def __init__(self, name):
#         self.name = name


# # 実体化
# tanaka = UserName(name='tanaka')
# # 出力
# print(tanaka)


# class UserName:
#     def __init__(self, name):
#         self.name = name


# tanaka = UserName(name="tanaka")
# # typeを入れデータ型を出力
# print(type(tanaka))


# class UserName:
#     def __init__(self, name):
#         self.name = name


# tanaka = UserName(name="tanaka")
# # データ型の値を出力
# print(tanaka.name)


# class UserName:
#     def __init__(self, name):
#         self.name = name


# # UserNameクラスのインスタンス化
# tanaka = UserName(name="tanaka")
# bob = UserName(name="bob")
# # クラスの値の出力
# print(tanaka.name)
# print(bob.name)


# class UserName:
#     def __init__(self, name):
#         # もしnameの文字数が4文字以上20文字以下でなければ
#         if not (4 <= len(name) <= 20):
#             # エラー文を表示して終了する
#             raise ValueError(f"{name}はルール違反です")

#         self.name = name


# # UserNameクラスのインスタンス化
# tanaka = UserName(name="tanaka")
# bob = UserName(name="bob")
# print(tanaka.name)
# print(bob.name)


class UserName:
    def __init__(self, name):
        if not (4 <= len(name) <= 20):
            raise ValueError(f'{name}はルール違反です')

        self.name = name

    # screen_nameメソッドの作成
    def screen_name(self):
        # upperは大文字に変換する
        return self.name.upper()


tanaka = UserName(name='tanaka')
# screen_nameで出力したいのでこの部分をメソッドを追加していく
print(tanaka.screen_name())
