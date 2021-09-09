# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TabItemOption(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TabItemOption()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTabItemOption(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # TabItemOption
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TabItemOption
    def Header(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.TabHeaderOption import TabHeaderOption
            obj = TabHeaderOption()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TabItemOption
    def Container(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.NodeTree import NodeTree
            obj = NodeTree()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def Start(builder): builder.StartObject(2)
def TabItemOptionStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddHeader(builder, header): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(header), 0)
def TabItemOptionAddHeader(builder, header):
    """This method is deprecated. Please switch to AddHeader."""
    return AddHeader(builder, header)
def AddContainer(builder, container): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(container), 0)
def TabItemOptionAddContainer(builder, container):
    """This method is deprecated. Please switch to AddContainer."""
    return AddContainer(builder, container)
def End(builder): return builder.EndObject()
def TabItemOptionEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)