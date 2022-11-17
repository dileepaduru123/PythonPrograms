class ArithmeticClass:
    """
    simple class to operate arithmetic operations
    """
    first_num = 20
    second_num = 40


    def get_sum_of_two_num(self):

        """
        addition of two numbers
        :return: int
        """

        return self.first_num + self.second_num

    def get_mul_of_two_num(self):
        """
        multiplication of two numbers
        :return: int
        """
        return self.first_num * self.second_num

    def get_sub_of_two_num(self):

        """
        subtraction of two numbers
        :return:int
        """
        return self.second_num - self.first_num
    def get_div_of_two_num(self):
        """
        division of two numbers
        :return: float
        """

        return self.first_num / self.second_num

 #   def print_multiplication(self):
  #      for item in range(1,11):
   #         print("{} * {} = {}".format(self.second_num, item, self.second_num*item))

ac = ArithmeticClass()
#ac.print_multiplication()
res = ac.get_div_of_two_num()
print(res)
res = ac.get_sub_of_two_num()
print(res)
res = ac.get_sum_of_two_num()
print(res)

res=ac.get_mul_of_two_num()
print(res)

