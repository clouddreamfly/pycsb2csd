# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class InnerActionFrame(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = InnerActionFrame()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsInnerActionFrame(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # InnerActionFrame
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # InnerActionFrame
    def FrameIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # InnerActionFrame
    def Tween(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return True

    # InnerActionFrame
    def InnerActionType(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # InnerActionFrame
    def CurrentAniamtionName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # InnerActionFrame
    def SingleFrameIndex(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # InnerActionFrame
    def EasingData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.EasingData import EasingData
            obj = EasingData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def Start(builder): builder.StartObject(6)
def InnerActionFrameStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddFrameIndex(builder, frameIndex): builder.PrependInt32Slot(0, frameIndex, 0)
def InnerActionFrameAddFrameIndex(builder, frameIndex):
    """This method is deprecated. Please switch to AddFrameIndex."""
    return AddFrameIndex(builder, frameIndex)
def AddTween(builder, tween): builder.PrependBoolSlot(1, tween, 1)
def InnerActionFrameAddTween(builder, tween):
    """This method is deprecated. Please switch to AddTween."""
    return AddTween(builder, tween)
def AddInnerActionType(builder, innerActionType): builder.PrependInt32Slot(2, innerActionType, 0)
def InnerActionFrameAddInnerActionType(builder, innerActionType):
    """This method is deprecated. Please switch to AddInnerActionType."""
    return AddInnerActionType(builder, innerActionType)
def AddCurrentAniamtionName(builder, currentAniamtionName): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(currentAniamtionName), 0)
def InnerActionFrameAddCurrentAniamtionName(builder, currentAniamtionName):
    """This method is deprecated. Please switch to AddCurrentAniamtionName."""
    return AddCurrentAniamtionName(builder, currentAniamtionName)
def AddSingleFrameIndex(builder, singleFrameIndex): builder.PrependInt32Slot(4, singleFrameIndex, 0)
def InnerActionFrameAddSingleFrameIndex(builder, singleFrameIndex):
    """This method is deprecated. Please switch to AddSingleFrameIndex."""
    return AddSingleFrameIndex(builder, singleFrameIndex)
def AddEasingData(builder, easingData): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(easingData), 0)
def InnerActionFrameAddEasingData(builder, easingData):
    """This method is deprecated. Please switch to AddEasingData."""
    return AddEasingData(builder, easingData)
def End(builder): return builder.EndObject()
def InnerActionFrameEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)