# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class AnimationInfo(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = AnimationInfo()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsAnimationInfo(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # AnimationInfo
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # AnimationInfo
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # AnimationInfo
    def StartIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # AnimationInfo
    def EndIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(3)
def AnimationInfoStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def AnimationInfoAddName(builder, name):
    """This method is deprecated. Please switch to AddName."""
    return AddName(builder, name)
def AddStartIndex(builder, startIndex): builder.PrependInt32Slot(1, startIndex, 0)
def AnimationInfoAddStartIndex(builder, startIndex):
    """This method is deprecated. Please switch to AddStartIndex."""
    return AddStartIndex(builder, startIndex)
def AddEndIndex(builder, endIndex): builder.PrependInt32Slot(2, endIndex, 0)
def AnimationInfoAddEndIndex(builder, endIndex):
    """This method is deprecated. Please switch to AddEndIndex."""
    return AddEndIndex(builder, endIndex)
def End(builder): return builder.EndObject()
def AnimationInfoEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)