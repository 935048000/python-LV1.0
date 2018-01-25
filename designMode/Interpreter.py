"""

Interpreter
解释器模式

开发一个自动识别谱子的吉他模拟器，达到录入谱即可按照谱发声的效果。
除了发声设备外（假设已完成），最重要的就是读谱和译谱能力了。
根据规则翻译谱的内容；根据翻译的内容演奏。
"""

# 解释器模型
class PlayContext():
    """PlayContext类为谱的内容"""
    play_text = None

class Expression():
    """Expression即表达式，里面仅含两个方法，interpret负责转译谱，execute则负责演奏"""
    def interpret(self, context):
        if len(context.play_text) == 0:
            return
        else:
            play_segs=context.play_text.split(" ")
            for play_seg in play_segs:
                pos=0
                for ele in play_seg:
                    if ele.isalpha():
                        pos+=1
                        continue
                    break
                play_chord = play_seg[0:pos]
                play_value = play_seg[pos:]
                self.execute(play_chord,play_value)
    def execute(self,play_key,play_value):
        pass

class NormGuitar(Expression):
    """NormGuitar类覆写execute，以吉他 的方式演奏。"""
    def execute(self, key, value):
        print ("正常的吉他演奏--弦:%s 演奏:%s" % (key, value))


if __name__=="__main__":
    context = PlayContext()
    context.play_text = "C53231323 Em43231323 F43231323 G63231323"
    guitar=NormGuitar()
    guitar.interpret(context)







