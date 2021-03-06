# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class RotationSkew(object):
    __slots__ = ['_tab']

    @classmethod
    def SizeOf(cls):
        return 8

    # RotationSkew
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # RotationSkew
    def RotationSkewX(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(0))
    # RotationSkew
    def RotationSkewY(self): return self._tab.Get(flatbuffers.number_types.Float32Flags, self._tab.Pos + flatbuffers.number_types.UOffsetTFlags.py_type(4))

def CreateRotationSkew(builder, rotationSkewX, rotationSkewY):
    builder.Prep(4, 8)
    builder.PrependFloat32(rotationSkewY)
    builder.PrependFloat32(rotationSkewX)
    return builder.Offset()
