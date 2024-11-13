class InformationHideExample():
    __secretNum = 90
    notSecretNum = 3535
    def increase(self):
        self.__secretNum += 1
        print("SecretNum increas: ", self.__secretNum)

example = InformationHideExample()

print(example.increase())
print("Not secret Num:", example.notSecretNum)
print("SecretNum:",example.__secretNum)