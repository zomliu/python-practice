

class Student:
    
    @classmethod
    def get_instance(cls):  # 类方法的参数是类本身
        return cls()
    
    def say_hello(self):
        print("hello")

    # 静态方法不需要self参数, 静态方法和类方法一样，都可以通过类名直接调用, 但从逻辑上和类其实没什么关系, 只是属于当前类而已
    # 如果类中方法不访问类实例方法和属性, 一般建议声明为静态方法
    @staticmethod       
    def say_hi():
        print("hi")
    

class CommonMethod:

    def __init__(self, name: str) -> None:
        self.name = name

    # 类似于java中的toString方法 
    def __str__(self) -> str:
        return "This is class CommonMethod"

    # 和__str__方法类似, 但是__repr__方法返回的字符串是更详细的, 一般是日志输出或者调试输出(面向开发者)
    # 通过传入实例给 repr(instance) 使用
    def __repr__(self) -> str:
        return "This is class CommonMethod"
    

    def __eq__(self, value: object) -> bool:
        if not isinstance(value, CommonMethod):
            return False
        return self.name == value.name

    def __hash__(self) -> int:
        return hash(self.name)
    
    

if __name__ == "__main__":
    student = Student.get_instance()
    student.say_hello()
