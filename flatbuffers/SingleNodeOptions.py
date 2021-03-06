# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class SingleNodeOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = SingleNodeOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsSingleNodeOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # SingleNodeOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # SingleNodeOptions
    def NodeOptions(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.WidgetOptions import WidgetOptions
            obj = WidgetOptions()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def Start(builder): builder.StartObject(1)
def SingleNodeOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddNodeOptions(builder, nodeOptions): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(nodeOptions), 0)
def SingleNodeOptionsAddNodeOptions(builder, nodeOptions):
    """This method is deprecated. Please switch to AddNodeOptions."""
    return AddNodeOptions(builder, nodeOptions)
def End(builder): return builder.EndObject()
def SingleNodeOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)