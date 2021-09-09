# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class Sprite3DOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = Sprite3DOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSprite3DOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # Sprite3DOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # Sprite3DOptions
    def Node3DOption(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.Node3DOption import Node3DOption
            obj = Node3DOption()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Sprite3DOptions
    def FileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # Sprite3DOptions
    def RunAction(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # Sprite3DOptions
    def IsFlipped(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # Sprite3DOptions
    def LightFlag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(5)
def Sprite3DOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddNode3DOption(builder, node3DOption): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(node3DOption), 0)
def Sprite3DOptionsAddNode3DOption(builder, node3DOption):
    """This method is deprecated. Please switch to AddNode3DOption."""
    return AddNode3DOption(builder, node3DOption)
def AddFileData(builder, fileData): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(fileData), 0)
def Sprite3DOptionsAddFileData(builder, fileData):
    """This method is deprecated. Please switch to AddFileData."""
    return AddFileData(builder, fileData)
def AddRunAction(builder, runAction): builder.PrependBoolSlot(2, runAction, 0)
def Sprite3DOptionsAddRunAction(builder, runAction):
    """This method is deprecated. Please switch to AddRunAction."""
    return AddRunAction(builder, runAction)
def AddIsFlipped(builder, isFlipped): builder.PrependBoolSlot(3, isFlipped, 0)
def Sprite3DOptionsAddIsFlipped(builder, isFlipped):
    """This method is deprecated. Please switch to AddIsFlipped."""
    return AddIsFlipped(builder, isFlipped)
def AddLightFlag(builder, lightFlag): builder.PrependInt32Slot(4, lightFlag, 0)
def Sprite3DOptionsAddLightFlag(builder, lightFlag):
    """This method is deprecated. Please switch to AddLightFlag."""
    return AddLightFlag(builder, lightFlag)
def End(builder): return builder.EndObject()
def Sprite3DOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)