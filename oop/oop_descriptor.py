# 描述符类, 一个描述符类要实现 __set_name__(self, owner, name) 和以下其中方法的最少一个:
# __get__(self, instance, owner)
# __set__(self, instance, value)
# __delete__(self, instance)


# 这个描述符对象可以对属性进行一定的约束
class StringDescriptor:
    def __init__(self, need_trim: bool, max_len: int):
        self.__need_trim = need_trim
        self.__max_len = max_len

    def __set_name__(self, owner, name):
        self.__property_name = name

    def __set__(self, instance, value):
        if self.__need_trim:
            value = value.strip()
        if len(value) > self.__max_len:
            raise ValueError('Too long')
        instance.__dict__[self.__property_name] = value

    def __get__(self, instance, owner):
        if self.__property_name in instance.__dict__:
            return instance.__dict__[self.__property_name]

        return None
    

# 业务类
class User:
    name = StringDescriptor(need_trim=True, max_len=100)  # 会调用 StringDescriptor 的 __set_name__ 方法
    age = 0

    def __init__(self, name='defaut'):
        self.name = 0
   
    

if __name__ == '__main__':
    user = User()
    user.name = '  hello world  '
    print(user.name)
    user.age = 100

    user2 = User()
    user2.name = 'This is another user instance'
    print(f'{user2.name} - {user2.age}')
    print(f'{user.name} - {user.age}')


    User.age = 300

    # user2.age = 120

    print(f'{user2.name} - {user2.age}')
    print(f'{user.name} - {user.age}')

    print(User.age)

