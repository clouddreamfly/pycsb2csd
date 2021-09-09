# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class UserCameraOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = UserCameraOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsUserCameraOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # UserCameraOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # UserCameraOptions
    def Node3DOption(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.Node3DOption import Node3DOption
            obj = Node3DOption()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # UserCameraOptions
    def Fov(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 60.0

    # UserCameraOptions
    def NearClip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 1.0

    # UserCameraOptions
    def FarClip(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Float32Flags, o + self._tab.Pos)
        return 1000.0

    # UserCameraOptions
    def CameraFlag(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # UserCameraOptions
    def SkyBoxEnabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # UserCameraOptions
    def LeftFileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # UserCameraOptions
    def RightFileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # UserCameraOptions
    def UpFileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # UserCameraOptions
    def DownFileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # UserCameraOptions
    def ForwardFileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # UserCameraOptions
    def BackFileData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def Start(builder): builder.StartObject(12)
def UserCameraOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddNode3DOption(builder, node3DOption): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(node3DOption), 0)
def UserCameraOptionsAddNode3DOption(builder, node3DOption):
    """This method is deprecated. Please switch to AddNode3DOption."""
    return AddNode3DOption(builder, node3DOption)
def AddFov(builder, fov): builder.PrependFloat32Slot(1, fov, 60.0)
def UserCameraOptionsAddFov(builder, fov):
    """This method is deprecated. Please switch to AddFov."""
    return AddFov(builder, fov)
def AddNearClip(builder, nearClip): builder.PrependFloat32Slot(2, nearClip, 1.0)
def UserCameraOptionsAddNearClip(builder, nearClip):
    """This method is deprecated. Please switch to AddNearClip."""
    return AddNearClip(builder, nearClip)
def AddFarClip(builder, farClip): builder.PrependFloat32Slot(3, farClip, 1000.0)
def UserCameraOptionsAddFarClip(builder, farClip):
    """This method is deprecated. Please switch to AddFarClip."""
    return AddFarClip(builder, farClip)
def AddCameraFlag(builder, cameraFlag): builder.PrependInt32Slot(4, cameraFlag, 0)
def UserCameraOptionsAddCameraFlag(builder, cameraFlag):
    """This method is deprecated. Please switch to AddCameraFlag."""
    return AddCameraFlag(builder, cameraFlag)
def AddSkyBoxEnabled(builder, skyBoxEnabled): builder.PrependBoolSlot(5, skyBoxEnabled, 0)
def UserCameraOptionsAddSkyBoxEnabled(builder, skyBoxEnabled):
    """This method is deprecated. Please switch to AddSkyBoxEnabled."""
    return AddSkyBoxEnabled(builder, skyBoxEnabled)
def AddLeftFileData(builder, leftFileData): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(leftFileData), 0)
def UserCameraOptionsAddLeftFileData(builder, leftFileData):
    """This method is deprecated. Please switch to AddLeftFileData."""
    return AddLeftFileData(builder, leftFileData)
def AddRightFileData(builder, rightFileData): builder.PrependUOffsetTRelativeSlot(7, flatbuffers.number_types.UOffsetTFlags.py_type(rightFileData), 0)
def UserCameraOptionsAddRightFileData(builder, rightFileData):
    """This method is deprecated. Please switch to AddRightFileData."""
    return AddRightFileData(builder, rightFileData)
def AddUpFileData(builder, upFileData): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(upFileData), 0)
def UserCameraOptionsAddUpFileData(builder, upFileData):
    """This method is deprecated. Please switch to AddUpFileData."""
    return AddUpFileData(builder, upFileData)
def AddDownFileData(builder, downFileData): builder.PrependUOffsetTRelativeSlot(9, flatbuffers.number_types.UOffsetTFlags.py_type(downFileData), 0)
def UserCameraOptionsAddDownFileData(builder, downFileData):
    """This method is deprecated. Please switch to AddDownFileData."""
    return AddDownFileData(builder, downFileData)
def AddForwardFileData(builder, forwardFileData): builder.PrependUOffsetTRelativeSlot(10, flatbuffers.number_types.UOffsetTFlags.py_type(forwardFileData), 0)
def UserCameraOptionsAddForwardFileData(builder, forwardFileData):
    """This method is deprecated. Please switch to AddForwardFileData."""
    return AddForwardFileData(builder, forwardFileData)
def AddBackFileData(builder, backFileData): builder.PrependUOffsetTRelativeSlot(11, flatbuffers.number_types.UOffsetTFlags.py_type(backFileData), 0)
def UserCameraOptionsAddBackFileData(builder, backFileData):
    """This method is deprecated. Please switch to AddBackFileData."""
    return AddBackFileData(builder, backFileData)
def End(builder): return builder.EndObject()
def UserCameraOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)