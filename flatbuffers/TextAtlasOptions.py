# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TextAtlasOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TextAtlasOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTextAtlasOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # TextAtlasOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TextAtlasOptions
    def WidgetOptions(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.WidgetOptions import WidgetOptions
            obj = WidgetOptions()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TextAtlasOptions
    def CharMapFileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TextAtlasOptions
    def StringValue(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TextAtlasOptions
    def StartCharMap(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TextAtlasOptions
    def ItemWidth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TextAtlasOptions
    def ItemHeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

def Start(builder): builder.StartObject(6)
def TextAtlasOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddWidgetOptions(builder, widgetOptions): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(widgetOptions), 0)
def TextAtlasOptionsAddWidgetOptions(builder, widgetOptions):
    """This method is deprecated. Please switch to AddWidgetOptions."""
    return AddWidgetOptions(builder, widgetOptions)
def AddCharMapFileData(builder, charMapFileData): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(charMapFileData), 0)
def TextAtlasOptionsAddCharMapFileData(builder, charMapFileData):
    """This method is deprecated. Please switch to AddCharMapFileData."""
    return AddCharMapFileData(builder, charMapFileData)
def AddStringValue(builder, stringValue): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(stringValue), 0)
def TextAtlasOptionsAddStringValue(builder, stringValue):
    """This method is deprecated. Please switch to AddStringValue."""
    return AddStringValue(builder, stringValue)
def AddStartCharMap(builder, startCharMap): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(startCharMap), 0)
def TextAtlasOptionsAddStartCharMap(builder, startCharMap):
    """This method is deprecated. Please switch to AddStartCharMap."""
    return AddStartCharMap(builder, startCharMap)
def AddItemWidth(builder, itemWidth): builder.PrependInt32Slot(4, itemWidth, 0)
def TextAtlasOptionsAddItemWidth(builder, itemWidth):
    """This method is deprecated. Please switch to AddItemWidth."""
    return AddItemWidth(builder, itemWidth)
def AddItemHeight(builder, itemHeight): builder.PrependInt32Slot(5, itemHeight, 0)
def TextAtlasOptionsAddItemHeight(builder, itemHeight):
    """This method is deprecated. Please switch to AddItemHeight."""
    return AddItemHeight(builder, itemHeight)
def End(builder): return builder.EndObject()
def TextAtlasOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)