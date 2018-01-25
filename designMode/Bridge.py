"""

桥梁模式

在一个画图程序中，
常会见到这样的情况：有一些预设的图形，如矩形、圆形等，
还有一个对象-画笔，调节画笔的类型（如画笔还是画刷，还是毛笔效果等）
并设定参数（如颜色、线宽等），
选定图形，就可以在画布上画出想要的图形了。
要实现以上需求，
先从最抽象的元素开始设计，即形状和画笔（暂时忽略画布，同时忽略画笔参数，只考虑画笔类型）。
"""

class Shape:
    name=""
    param=""
    def __init__(self,*param):
        pass
    def getName(self):
        return self.name
    def getParam(self):
        return self.name,self.param

class Pen:
    shape=""
    type=""
    def __init__(self,shape):
        self.shape=shape
    def draw(self):
        pass


# 构造多个形状
class Rectangle(Shape):
    def __init__(self, long, width, *param):
        super ().__init__ (*param)
        self.name="矩形"
        self.param="长:%s 宽:%s"%(long,width)
        print ("创建一个矩形:%s" % self.param)


class Circle(Shape):
    def __init__(self, radius, *param):
        super ().__init__ (*param)
        self.name="圆形"
        self.param="半径:%s"%radius
        print ("创建一个圆:%s" % self.param)

# 构造多种画笔
class NormalPen(Pen):
    def __init__(self,shape):
        Pen.__init__(self,shape)
        self.type="标准"
    def draw(self):
        print ("绘画 %s:%s----参数:%s" % (self.type, self.shape.getName (), self.shape.getParam ()))


class BrushPen(Pen):
    def __init__(self,shape):
        Pen.__init__(self,shape)
        self.type="刷子"
    def draw(self):
        print ("绘画 %s:%s----参数:%s" % (self.type, self.shape.getName (), self.shape.getParam ()))


if __name__=="__main__":
    normal_pen=NormalPen(Rectangle("20cm","10cm"))
    brush_pen=BrushPen(Circle("15cm"))
    normal_pen.draw()
    brush_pen.draw()











