# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TimeLine(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TimeLine()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTimeLine(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # TimeLine
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TimeLine
    def Property(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TimeLine
    def ActionTag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TimeLine
    def Frames(self, j):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = self._tab.Vector(o)
            x += flatbuffers.number_types.UOffsetTFlags.py_type(j) * 4
            x = self._tab.Indirect(x)
            from flatbuffers.Frame import Frame
            obj = Frame()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TimeLine
    def FramesLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.VectorLen(o)
        return 0

    # TimeLine
    def FramesIsNone(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        return o == 0

def Start(builder): builder.StartObject(3)
def TimeLineStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddProperty(builder, property): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(property), 0)
def TimeLineAddProperty(builder, property):
    """This method is deprecated. Please switch to AddProperty."""
    return AddProperty(builder, property)
def AddActionTag(builder, actionTag): builder.PrependInt32Slot(1, actionTag, 0)
def TimeLineAddActionTag(builder, actionTag):
    """This method is deprecated. Please switch to AddActionTag."""
    return AddActionTag(builder, actionTag)
def AddFrames(builder, frames): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(frames), 0)
def TimeLineAddFrames(builder, frames):
    """This method is deprecated. Please switch to AddFrames."""
    return AddFrames(builder, frames)
def StartFramesVector(builder, numElems): return builder.StartVector(4, numElems, 4)
def TimeLineStartFramesVector(builder, numElems):
    """This method is deprecated. Please switch to Start."""
    return StartFramesVector(builder, numElems)
def End(builder): return builder.EndObject()
def TimeLineEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)