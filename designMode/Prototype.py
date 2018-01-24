
"""
prototype 原型模式
"""

# 图层对象
class simpleLayer:
    background=[0,0,0,0]
    content="blank"
    def getContent(self):
        return self.content
    def getBackgroud(self):
        return self.background
    def paint(self,painting):
        self.content=painting
    def setParent(self,p):
        self.background[3]=p
    def fillBackground(self,back):
        self.background=back


# 可以用复制的方法来实现，而复制（clone）这个动作，就是原型模式的精髓
from copy import copy, deepcopy
class simpleLayer:
    background=[0,0,0,0]
    content="blank"
    def getContent(self):
        return self.content
    def getBackgroud(self):
        return self.background
    def paint(self,painting):
        self.content=painting
    def setParent(self,p):
        self.background[3]=p
    def fillBackground(self,back):
        self.background=back
    def clone(self):
        return copy(self)
    def deep_clone(self):
        return deepcopy(self)

# 新建图层，填充蓝底并画一只狗，
if  __name__=="__main__":
    # 浅拷贝后，直接对拷贝后引用（这里的数组）进行操作，原始对象中该引用的内容也会变动。
    dog_layer=simpleLayer()
    dog_layer.paint("狗")
    dog_layer.fillBackground([0,0,255,0])
    print ("原始的背景:", dog_layer.getBackgroud ())
    print ("原始的绘画:", dog_layer.getContent ())
    another_dog_layer=dog_layer.clone()
    another_dog_layer.setParent (128)
    another_dog_layer.paint ("小狗")
    print ("原始的背景:", dog_layer.getBackgroud ())
    print ("原始的绘画:", dog_layer.getContent ())
    print ("原始的背景:", another_dog_layer.getBackgroud ())
    print ("原始的绘画:", another_dog_layer.getContent ())
    
    print("---------------------------------------")
    # 深拷贝后，其对象内的引用内容也被进行了复制。
    dog_layer=simpleLayer()
    dog_layer.paint("狗")
    dog_layer.fillBackground([0,0,255,0])
    print ("原始的背景:", dog_layer.getBackgroud ())
    print ("原始的绘画:", dog_layer.getContent ())
    another_dog_layer=dog_layer.deep_clone()
    another_dog_layer.setParent (128)
    another_dog_layer.paint ("小狗")
    print ("原始的背景:", dog_layer.getBackgroud ())
    print ("原始的绘画:", dog_layer.getContent ())
    print ("原始的背景:", another_dog_layer.getBackgroud ())
    print ("原始的绘画:", another_dog_layer.getContent ())
#

















