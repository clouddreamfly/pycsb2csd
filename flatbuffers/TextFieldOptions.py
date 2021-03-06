# automatically generated by the FlatBuffers compiler, do not modify

# namespace: flatbuffers

import flatbuffers
from flatbuffers.compat import import_numpy
np = import_numpy()

class TextFieldOptions(object):
    __slots__ = ['_tab']

    @classmethod
    def GetRootAs(cls, buf, offset=0):
        n = flatbuffers.encode.Get(flatbuffers.packer.uoffset, buf, offset)
        x = TextFieldOptions()
        x.Init(buf, n + offset)
        return x

    @classmethod
    def GetRootAsTextFieldOptions(cls, buf, offset=0):
        """This method is deprecated. Please switch to GetRootAs."""
        return cls.GetRootAs(buf, offset)
    # TextFieldOptions
    def Init(self, buf, pos):
        self._tab = flatbuffers.table.Table(buf, pos)

    # TextFieldOptions
    def WidgetOptions(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(4))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.WidgetOptions import WidgetOptions
            obj = WidgetOptions()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TextFieldOptions
    def FontResource(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(6))
        if o != 0:
            x = self._tab.Indirect(o + self._tab.Pos)
            from flatbuffers.ResourceData import ResourceData
            obj = ResourceData()
            obj.Init(self._tab.Bytes, x)
            return obj
        return None

    # TextFieldOptions
    def FontName(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(8))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TextFieldOptions
    def FontSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(10))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TextFieldOptions
    def Text(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(12))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TextFieldOptions
    def IsLocalized(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(14))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TextFieldOptions
    def PlaceHolder(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(16))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TextFieldOptions
    def PasswordEnabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(18))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TextFieldOptions
    def PasswordStyleText(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(20))
        if o != 0:
            return self._tab.String(o + self._tab.Pos)
        return None

    # TextFieldOptions
    def MaxLengthEnabled(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(22))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

    # TextFieldOptions
    def MaxLength(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(24))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TextFieldOptions
    def AreaWidth(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(26))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TextFieldOptions
    def AreaHeight(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(28))
        if o != 0:
            return self._tab.Get(flatbuffers.number_types.Int32Flags, o + self._tab.Pos)
        return 0

    # TextFieldOptions
    def IsCustomSize(self):
        o = flatbuffers.number_types.UOffsetTFlags.py_type(self._tab.Offset(30))
        if o != 0:
            return bool(self._tab.Get(flatbuffers.number_types.BoolFlags, o + self._tab.Pos))
        return False

def Start(builder): builder.StartObject(14)
def TextFieldOptionsStart(builder):
    """This method is deprecated. Please switch to Start."""
    return Start(builder)
def AddWidgetOptions(builder, widgetOptions): builder.PrependUOffsetTRelativeSlot(0, flatbuffers.number_types.UOffsetTFlags.py_type(widgetOptions), 0)
def TextFieldOptionsAddWidgetOptions(builder, widgetOptions):
    """This method is deprecated. Please switch to AddWidgetOptions."""
    return AddWidgetOptions(builder, widgetOptions)
def AddFontResource(builder, fontResource): builder.PrependUOffsetTRelativeSlot(1, flatbuffers.number_types.UOffsetTFlags.py_type(fontResource), 0)
def TextFieldOptionsAddFontResource(builder, fontResource):
    """This method is deprecated. Please switch to AddFontResource."""
    return AddFontResource(builder, fontResource)
def AddFontName(builder, fontName): builder.PrependUOffsetTRelativeSlot(2, flatbuffers.number_types.UOffsetTFlags.py_type(fontName), 0)
def TextFieldOptionsAddFontName(builder, fontName):
    """This method is deprecated. Please switch to AddFontName."""
    return AddFontName(builder, fontName)
def AddFontSize(builder, fontSize): builder.PrependInt32Slot(3, fontSize, 0)
def TextFieldOptionsAddFontSize(builder, fontSize):
    """This method is deprecated. Please switch to AddFontSize."""
    return AddFontSize(builder, fontSize)
def AddText(builder, text): builder.PrependUOffsetTRelativeSlot(4, flatbuffers.number_types.UOffsetTFlags.py_type(text), 0)
def TextFieldOptionsAddText(builder, text):
    """This method is deprecated. Please switch to AddText."""
    return AddText(builder, text)
def AddIsLocalized(builder, isLocalized): builder.PrependBoolSlot(5, isLocalized, 0)
def TextFieldOptionsAddIsLocalized(builder, isLocalized):
    """This method is deprecated. Please switch to AddIsLocalized."""
    return AddIsLocalized(builder, isLocalized)
def AddPlaceHolder(builder, placeHolder): builder.PrependUOffsetTRelativeSlot(6, flatbuffers.number_types.UOffsetTFlags.py_type(placeHolder), 0)
def TextFieldOptionsAddPlaceHolder(builder, placeHolder):
    """This method is deprecated. Please switch to AddPlaceHolder."""
    return AddPlaceHolder(builder, placeHolder)
def AddPasswordEnabled(builder, passwordEnabled): builder.PrependBoolSlot(7, passwordEnabled, 0)
def TextFieldOptionsAddPasswordEnabled(builder, passwordEnabled):
    """This method is deprecated. Please switch to AddPasswordEnabled."""
    return AddPasswordEnabled(builder, passwordEnabled)
def AddPasswordStyleText(builder, passwordStyleText): builder.PrependUOffsetTRelativeSlot(8, flatbuffers.number_types.UOffsetTFlags.py_type(passwordStyleText), 0)
def TextFieldOptionsAddPasswordStyleText(builder, passwordStyleText):
    """This method is deprecated. Please switch to AddPasswordStyleText."""
    return AddPasswordStyleText(builder, passwordStyleText)
def AddMaxLengthEnabled(builder, maxLengthEnabled): builder.PrependBoolSlot(9, maxLengthEnabled, 0)
def TextFieldOptionsAddMaxLengthEnabled(builder, maxLengthEnabled):
    """This method is deprecated. Please switch to AddMaxLengthEnabled."""
    return AddMaxLengthEnabled(builder, maxLengthEnabled)
def AddMaxLength(builder, maxLength): builder.PrependInt32Slot(10, maxLength, 0)
def TextFieldOptionsAddMaxLength(builder, maxLength):
    """This method is deprecated. Please switch to AddMaxLength."""
    return AddMaxLength(builder, maxLength)
def AddAreaWidth(builder, areaWidth): builder.PrependInt32Slot(11, areaWidth, 0)
def TextFieldOptionsAddAreaWidth(builder, areaWidth):
    """This method is deprecated. Please switch to AddAreaWidth."""
    return AddAreaWidth(builder, areaWidth)
def AddAreaHeight(builder, areaHeight): builder.PrependInt32Slot(12, areaHeight, 0)
def TextFieldOptionsAddAreaHeight(builder, areaHeight):
    """This method is deprecated. Please switch to AddAreaHeight."""
    return AddAreaHeight(builder, areaHeight)
def AddIsCustomSize(builder, isCustomSize): builder.PrependBoolSlot(13, isCustomSize, 0)
def TextFieldOptionsAddIsCustomSize(builder, isCustomSize):
    """This method is deprecated. Please switch to AddIsCustomSize."""
    return AddIsCustomSize(builder, isCustomSize)
def End(builder): return builder.EndObject()
def TextFieldOptionsEnd(builder):
    """This method is deprecated. Please switch to End."""
    return End(builder)