# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class ParticleSystemOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = ParticleSystemOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsParticleSystemOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # ParticleSystemOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # ParticleSystemOptions
    def NodeOptions(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.WidgetOptions import WidgetOptions
            obj = WidgetOptions()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ParticleSystemOptions
    def FileNameData(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # ParticleSystemOptions
    def BlendFunc(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            x = o + self._tab.Pos
            from flatbuffers.BlendFunc import BlendFunc
            obj = BlendFunc()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

def Start(builder): builder.StartObject(3)
def ParticleSystemOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddNodeOptions(builder, nodeOptions): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(nodeOptions), 0)
def ParticleSystemOptionsAddNodeOptions(builder, nodeOptions):
    """This method is deprecated. Please switch to AddNodeOptions."""
    return AddNodeOptions(builder, nodeOptions)
def AddFileNameData(builder, fileNameData): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(fileNameData), 0)
def ParticleSystemOptionsAddFileNameData(builder, fileNameData):
    """This method is deprecated. Please switch to AddFileNameData."""
    return AddFileNameData(builder, fileNameData)
def AddBlendFunc(builder, blendFunc): builder.PrependStructSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(blendFunc), 0)
def ParticleSystemOptionsAddBlendFunc(builder, blendFunc):
    """This method is deprecated. Please switch to AddBlendFunc."""
    return AddBlendFunc(builder, blendFunc)
def End(builder): return builder.EndObject()
def ParticleSystemOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)