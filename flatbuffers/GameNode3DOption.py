# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class GameNode3DOption(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = GameNode3DOption()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsGameNode3DOption(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # GameNode3DOption
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # GameNode3DOption
    def Name(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GameNode3DOption
    def SkyBoxMask(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # GameNode3DOption
    def SkyBoxEnabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # GameNode3DOption
    def LeftFileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GameNode3DOption
    def RightFileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GameNode3DOption
    def UpFileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GameNode3DOption
    def DownFileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GameNode3DOption
    def ForwardFileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GameNode3DOption
    def BackFileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # GameNode3DOption
    def FrameEvent(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GameNode3DOption
    def CustomProperty(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # GameNode3DOption
    def UseDefaultLight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def Start(builder): builder.StartObject(12)
def GameNode3DOptionStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddName(builder, name): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(name), 0)
def GameNode3DOptionAddName(builder, name):
    """This method is deprecated. Please switch to AddName."""
    return AddName(builder, name)
def AddSkyBoxMask(builder, skyBoxMask): builder.PrependInt32Slot(1, skyBoxMask, 0)
def GameNode3DOptionAddSkyBoxMask(builder, skyBoxMask):
    """This method is deprecated. Please switch to AddSkyBoxMask."""
    return AddSkyBoxMask(builder, skyBoxMask)
def AddSkyBoxEnabled(builder, skyBoxEnabled): builder.PrependBoolSlot(2, skyBoxEnabled, 0)
def GameNode3DOptionAddSkyBoxEnabled(builder, skyBoxEnabled):
    """This method is deprecated. Please switch to AddSkyBoxEnabled."""
    return AddSkyBoxEnabled(builder, skyBoxEnabled)
def AddLeftFileData(builder, leftFileData): builder.PrependUOffsetTRelativeSlot(3, flatbuffers.number_types.UOffsetTFlags.py_type(leftFileData), 0)
def GameNode3DOptionAddLeftFileData(builder, leftFileData):
    """This method is deprecated. Please switch to AddLeftFileData."""
    return AddLeftFileData(builder, leftFileData)
def AddRightFileData(builder, rightFileData): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(rightFileData), 0)
def GameNode3DOptionAddRightFileData(builder, rightFileData):
    """This method is deprecated. Please switch to AddRightFileData."""
    return AddRightFileData(builder, rightFileData)
def AddUpFileData(builder, upFileData): builder.PrependUOffsetTRelativeSlot(5, flatbuffers.number_types.UOffsetTFlags.py_type(upFileData), 0)
def GameNode3DOptionAddUpFileData(builder, upFileData):
    """This method is deprecated. Please switch to AddUpFileData."""
    return AddUpFileData(builder, upFileData)
def AddDownFileData(builder, downFileData): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(downFileData), 0)
def GameNode3DOptionAddDownFileData(builder, downFileData):
    """This method is deprecated. Please switch to AddDownFileData."""
    return AddDownFileData(builder, downFileData)
def AddForwardFileData(builder, forwardFileData): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(forwardFileData), 0)
def GameNode3DOptionAddForwardFileData(builder, forwardFileData):
    """This method is deprecated. Please switch to AddForwardFileData."""
    return AddForwardFileData(builder, forwardFileData)
def AddBackFileData(builder, backFileData): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(backFileData), 0)
def GameNode3DOptionAddBackFileData(builder, backFileData):
    """This method is deprecated. Please switch to AddBackFileData."""
    return AddBackFileData(builder, backFileData)
def AddFrameEvent(builder, frameEvent): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(frameEvent), 0)
def GameNode3DOptionAddFrameEvent(builder, frameEvent):
    """This method is deprecated. Please switch to AddFrameEvent."""
    return AddFrameEvent(builder, frameEvent)
def AddCustomProperty(builder, customProperty): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(customProperty), 0)
def GameNode3DOptionAddCustomProperty(builder, customProperty):
    """This method is deprecated. Please switch to AddCustomProperty."""
    return AddCustomProperty(builder, customProperty)
def AddUseDefaultLight(builder, useDefaultLight): builder.PrependBoolSlot(11, useDefaultLight, 0)
def GameNode3DOptionAddUseDefaultLight(builder, useDefaultLight):
    """This method is deprecated. Please switch to AddUseDefaultLight."""
    return AddUseDefaultLight(builder, useDefaultLight)
def End(builder): return builder.EndObject()
def GameNode3DOptionEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)