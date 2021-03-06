# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class CSArmatureNodeOption(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = CSArmatureNodeOption()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsCSArmatureNodeOption(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # CSArmatureNodeOption
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # CSArmatureNodeOption
    def NodeOptions(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.WidgetOptions import WidgetOptions
            obj = WidgetOptions()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CSArmatureNodeOption
    def FileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceItemData import ResourceItemData
            obj = ResourceItemData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # CSArmatureNodeOption
    def IsLoop(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return True

    # CSArmatureNodeOption
    def IsAutoPlay(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return True

    # CSArmatureNodeOption
    def CurrentAnimationName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

def Start(builder): builder.StartObject(5)
def CSArmatureNodeOptionStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddNodeOptions(builder, nodeOptions): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(nodeOptions), 0)
def CSArmatureNodeOptionAddNodeOptions(builder, nodeOptions):
    """This method is deprecated. Please switch to AddNodeOptions."""
    return AddNodeOptions(builder, nodeOptions)
def AddFileData(builder, fileData): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(fileData), 0)
def CSArmatureNodeOptionAddFileData(builder, fileData):
    """This method is deprecated. Please switch to AddFileData."""
    return AddFileData(builder, fileData)
def AddIsLoop(builder, isLoop): builder.PrependBoolSlot(2, isLoop, 1)
def CSArmatureNodeOptionAddIsLoop(builder, isLoop):
    """This method is deprecated. Please switch to AddIsLoop."""
    return AddIsLoop(builder, isLoop)
def AddIsAutoPlay(builder, isAutoPlay): builder.PrependBoolSlot(3, isAutoPlay, 1)
def CSArmatureNodeOptionAddIsAutoPlay(builder, isAutoPlay):
    """This method is deprecated. Please switch to AddIsAutoPlay."""
    return AddIsAutoPlay(builder, isAutoPlay)
def AddCurrentAnimationName(builder, currentAnimationName): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(currentAnimationName), 0)
def CSArmatureNodeOptionAddCurrentAnimationName(builder, currentAnimationName):
    """This method is deprecated. Please switch to AddCurrentAnimationName."""
    return AddCurrentAnimationName(builder, currentAnimationName)
def End(builder): return builder.EndObject()
def CSArmatureNodeOptionEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)