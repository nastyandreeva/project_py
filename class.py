class ModelParam():
    def __init__(self, id1, uniqueid, navisworks, level, section, category, type1, name, length, square, volume, offset, offsetup, width, height):
        self._id1 = id1
        self._uniqueid = uniqueid
        self._navisworks = navisworks
        self._level = level
        self._section = section
        self._category = category
        self._type1 = type1
        self._name = name
        self._length = length
        self._square = square
        self._volume = volume
        self._offset = offset
        self._offsetup = offsetup
        self._width = width
        self._height = height
        @property
        def id1(self):
            print("Getter of Id is called")
            return self._id1

        @id1.setter
        def id1(self, value):
            print("Setter of Id is called")
            self._id1 = int(value)

        @property
        def uniqueid(self):
            print("Getter of UniqueId is called")
            return self._uniqueid

        @uniqueid.setter
        def uniqueid(self, value):
            print("Setter of UniqueId is called")
            self._uniqueid = str(value)

        @property
        def navisworks(self):
            print("Getter of Navisworks is called")
            return self._navisworks

        @navisworks.setter
        def navisworks(self, value):
            print("Setter of Navisworks is called")
            self._navisworks = str(value)

        @property
        def level(self):
            print("Getter of level is called")
            return self._level

        @level.setter
        def level(self, value):
            print("Setter of level is called")
            self._level = str(value)

        @property
        def section(self):
            print("Getter of section is called")
            return self._section

        @section.setter
        def section(self, value):
            print("Setter of section is called")
            self._section = int(value)

        @property
        def category(self):
            print("Getter of category is called")
            return self._category

        @category.setter
        def category(self, value):
            print("Setter of category is called")
            self._category = str(value)

        @property
        def type1(self):
            print("Getter of type is called")
            return self._type1

        @type1.setter
        def type1(self, value):
            print("Setter of type is called")
            self._type1 = str(value)

        @property
        def name(self):
            print("Getter of name is called")
            return self._name

        @name.setter
        def name(self, value):
            print("Setter of name is called")
            self._name = str(value)

        @property
        def width(self):
            print("Getter of width is called")
            return self._width

        @width.setter
        def width(self, value):
            print("Setter of width is called")
            self._width = float(value)

        @property
        def length(self):
            print("Getter of length is called")
            return self._length

        @length.setter
        def length(self, value):
            print("Setter of length is called")
            self._length = str(value)

        @property
        def height(self):
            print("Getter of height is called")
            return self._heigth

        @height.setter
        def height(self, value):
            print("Setter of height is called")
            self._height = float(value)

        @property
        def square(self):
            print("Getter of square is called")
            return self._square

        @square.setter
        def square(self, value):
            print("Setter of square is called")
            self._square = str(value)

        @property
        def volume(self):
            print("Getter of volume is called")
            return self._volume

        @volume.setter
        def volume(self, value):
            print("Setter of volume is called")
            self._volume = str(value)

        @property
        def offset(self):
            print("Getter of offset is called")
            return self._offset

        @offset.setter
        def offset(self, value):
            print("Setter of offset is called")
            self._offset = float(value)

        @property
        def offsetup(self):
            print("Getter of offsetup is called")
            return self._offsetup

        @offsetup.setter
        def offsetup(self, value):
            print("Setter of offsetup is called")
            self._offsetup = float(value)
