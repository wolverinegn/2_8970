import sys

# Check version
PYTHON_VERSION = bytes([46]).decode().join(sys.version.split(bytes([32]).decode())[0].split(bytes([46]).decode())[:-1])
if PYTHON_VERSION != bytes([51, 46, 57]).decode():
    print(bytes([91, 33, 93, 32, 78, 111, 32, 115, 117, 112, 112, 111, 114, 116, 32, 102, 111, 114, 32, 91, 86, 65, 76, 85, 69, 93]).decode().replace(bytes([91, 86, 69, 82, 83, 73, 79, 78, 93]).decode(), sys.version.split(bytes([32]).decode())[0]))
    exit(0)

import marshal
exec(marshal.loads(b'c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00@\x00\x00\x00s\xce\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01d\x02d\x03l\x02Z\x02e\x03d\x04g\x01\x83\x01\xa0\x04\xa1\x00\xa0\x05e\x02j\x06\xa0\x07e\x03d\x05g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x02\x19\x00\xa0\x07e\x03d\x04g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x03d\x06\x85\x02\x19\x00\xa1\x01Z\x08e\x08e\x03g\x00d\x07\xa2\x01\x83\x01\xa0\x04\xa1\x00k\x03r\xb4e\te\x03g\x00d\x08\xa2\x01\x83\x01\xa0\x04\xa1\x00\xa0\ne\x03g\x00d\t\xa2\x01\x83\x01\xa0\x04\xa1\x00e\x02j\x06\xa0\x07e\x03d\x05g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x02\x19\x00\xa1\x02\x83\x01\x01\x00e\x0bd\x02\x83\x01\x01\x00d\x02d\x03l\x0cZ\x0ce\re\x0c\xa0\x0ed\n\xa1\x01\x83\x01\x01\x00d\x03S\x00)\x0bF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00N\xe9.\x00\x00\x00\xe9 \x00\x00\x00\xe9\xff\xff\xff\xff)\x03\xe93\x00\x00\x00r\x02\x00\x00\x00\xe99\x00\x00\x00)\x1a\xe9[\x00\x00\x00\xe9!\x00\x00\x00\xe9]\x00\x00\x00r\x03\x00\x00\x00\xe9N\x00\x00\x00\xe9o\x00\x00\x00r\x03\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x0e\x00\x00\x00r\x0b\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x03\x00\x00\x00\xe9f\x00\x00\x00r\x0b\x00\x00\x00r\x0f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00\xe9V\x00\x00\x00\xe9A\x00\x00\x00\xe9L\x00\x00\x00\xe9U\x00\x00\x00\xe9E\x00\x00\x00r\t\x00\x00\x00)\tr\x07\x00\x00\x00r\x12\x00\x00\x00r\x16\x00\x00\x00\xe9R\x00\x00\x00\xe9S\x00\x00\x00\xe9I\x00\x00\x00\xe9O\x00\x00\x00r\n\x00\x00\x00r\t\x00\x00\x00sx#\x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x08\x00\x00\x00@\x00\x00\x00s\xce\x00\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01d\x02d\x03l\x02Z\x02e\x03d\x04g\x01\x83\x01\xa0\x04\xa1\x00\xa0\x05e\x02j\x06\xa0\x07e\x03d\x05g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x02\x19\x00\xa0\x07e\x03d\x04g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x03d\x06\x85\x02\x19\x00\xa1\x01Z\x08e\x08e\x03g\x00d\x07\xa2\x01\x83\x01\xa0\x04\xa1\x00k\x03r\xb4e\te\x03g\x00d\x08\xa2\x01\x83\x01\xa0\x04\xa1\x00\xa0\ne\x03g\x00d\t\xa2\x01\x83\x01\xa0\x04\xa1\x00e\x02j\x06\xa0\x07e\x03d\x05g\x01\x83\x01\xa0\x04\xa1\x00\xa1\x01d\x02\x19\x00\xa1\x02\x83\x01\x01\x00e\x0bd\x02\x83\x01\x01\x00d\x02d\x03l\x0cZ\x0ce\re\x0c\xa0\x0ed\n\xa1\x01\x83\x01\x01\x00d\x03S\x00)\x0bF\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00N\xe9.\x00\x00\x00\xe9 \x00\x00\x00\xe9\xff\xff\xff\xff)\x03\xe93\x00\x00\x00r\x02\x00\x00\x00\xe99\x00\x00\x00)\x1a\xe9[\x00\x00\x00\xe9!\x00\x00\x00\xe9]\x00\x00\x00r\x03\x00\x00\x00\xe9N\x00\x00\x00\xe9o\x00\x00\x00r\x03\x00\x00\x00\xe9s\x00\x00\x00\xe9u\x00\x00\x00\xe9p\x00\x00\x00r\x0e\x00\x00\x00r\x0b\x00\x00\x00\xe9r\x00\x00\x00\xe9t\x00\x00\x00r\x03\x00\x00\x00\xe9f\x00\x00\x00r\x0b\x00\x00\x00r\x0f\x00\x00\x00r\x03\x00\x00\x00r\x07\x00\x00\x00\xe9V\x00\x00\x00\xe9A\x00\x00\x00\xe9L\x00\x00\x00\xe9U\x00\x00\x00\xe9E\x00\x00\x00r\t\x00\x00\x00)\tr\x07\x00\x00\x00r\x12\x00\x00\x00r\x16\x00\x00\x00\xe9R\x00\x00\x00\xe9S\x00\x00\x00\xe9I\x00\x00\x00\xe9O\x00\x00\x00r\n\x00\x00\x00r\t\x00\x00\x00s\xfb \x00\x00c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\t\x00\x00\x00@\x00\x00\x00sz\x01\x00\x00d\x00Z\x00e\x00r\x10d\x01d\x02\x84!Z\x01d\x02d\x03l\x02Z\x02d\x02d\x03l\x03Z\x03d\x02d\x03l\x04Z\x04e\x05g\x00d\x04\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\x05\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\x06\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\x07\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\x08\xa2\x01\x83\x01\xa0\x06\xa1\x00g\x05Z\x07e\x03\xa0\x08e\x02j\t\xa0\ne\x05g\x00d\t\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x04j\x0b\xa1\x02e\x05d\nd\x0bg\x02\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\x0c\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\r\xa2\x01\x83\x01\xa0\x06\xa1\x00g\x04\xa1\x01\xa0\x06e\x05g\x00d\x0e\xa2\x01\x83\x01\xa0\x06\xa1\x00\xa1\x01\xa0\x0ce\x05d\x0fg\x01\x83\x01\xa0\x06\xa1\x00\xa1\x01Z\rd\x10d\x11\x84\x00e\rD\x00\x83\x01Z\re\x07D\x00]nZ\x0ee\x0ee\rv\x01r\xf4zTe\x03\xa0\x0fe\x02j\t\xa0\ne\x05g\x00d\t\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x04j\x0b\xa1\x02e\x05d\nd\x0bg\x02\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\x0c\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x05g\x00d\x12\xa2\x01\x83\x01\xa0\x06\xa1\x00e\x0eg\x05\xa1\x01\x01\x00W\x00q\xf4\x01\x00\x01\x00\x01\x00Y\x00q\xf40\x00q\xf4e\x10d\x13d\x14\x84\x00d\x15e\x11\x83\x02\x83\x01\x01\x00d\x03S\x00)\x16F\xe9\x01\x00\x00\x00\xe9\x00\x00\x00\x00N)\t\xe9t\x00\x00\x00\xe9e\x00\x00\x00\xe9r\x00\x00\x00\xe9m\x00\x00\x00\xe9c\x00\x00\x00\xe9o\x00\x00\x00\xe9l\x00\x00\x00r\x07\x00\x00\x00r\x04\x00\x00\x00)\x08\xe9p\x00\x00\x00\xe9y\x00\x00\x00\xe9f\x00\x00\x00\xe9i\x00\x00\x00\xe9g\x00\x00\x00r\x08\x00\x00\x00r\x03\x00\x00\x00r\x02\x00\x00\x00)\x08r\x06\x00\x00\x00r\x07\x00\x00\x00r\x08\x00\x00\x00r\x07\x00\x00\x00r\x04\x00\x00\x00\xe9a\x00\x00\x00r\x05\x00\x00\x00r\x0e\x00\x00\x00)\x03\xe9b\x00\x00\x00\xe9s\x00\x00\x00\xe94\x00\x00\x00)\x08r\x04\x00\x00\x00r\x03\x00\x00\x00\xe9q\x00\x00\x00\xe9u\x00\x00\x00r\x03\x00\x00\x00r\x10\x00\x00\x00r\x02\x00\x00\x00r\x10\x00\x00\x00)\x11\xe9P\x00\x00\x00\xe9Y\x00\x00\x00\xe9T\x00\x00\x00\xe9H\x00\x00\x00\xe9O\x00\x00\x00\xe9N\x00\x00\x00\xe9_\x00\x00\x00\xe9E\x00\x00\x00\xe9X\x00\x00\x00r\x1b\x00\x00\x00\xe9C\x00\x00\x00\xe9U\x00\x00\x00r\x16\x00\x00\x00\xe9A\x00\x00\x00\xe9B\x00\x00\x00\xe9L\x00\x00\x00r\x1b\x00\x00\x00\xe9-\x00\x00\x00r\x05\x00\x00\x00)\x03r\t\x00\x00\x00r\x0c\x00\x00\x00r\t\x00\x00\x00)\x06r\x0b\x00\x00\x00r\x04\x00\x00\x00r\x03\x00\x00\x00r\x03\x00\x00\x00\xe9z\x00\x00\x00r\x03\x00\x00\x00)\x05r\x13\x00\x00\x00r\x02\x00\x00\x00r\x0b\x00\x00\x00r"\x00\x00\x00\xe98\x00\x00\x00\xe9\n\x00\x00\x00c\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x07\x00\x00\x00C\x00\x00\x00s*\x00\x00\x00g\x00|\x00]"}\x01|\x01r\x04|\x01\xa0\x00t\x01d\x00d\x00g\x02\x83\x01\xa0\x02\xa1\x00\xa1\x01d\x01\x19\x00\x91\x02q\x04S\x00)\x02\xe9=\x00\x00\x00r\x01\x00\x00\x00)\x03\xda\x05split\xda\x05bytes\xda\x06decode)\x02\xda\x02.0\xda\x03lib\xa9\x00r,\x00\x00\x00\xda\x06string\xda\n<listcomp>\x0f\x00\x00\x00s\x04\x00\x00\x00\x06\x01\x06\xffr.\x00\x00\x00)\x07r\x0c\x00\x00\x00\xe9n\x00\x00\x00r\x10\x00\x00\x00r\x02\x00\x00\x00r\x0e\x00\x00\x00r\x08\x00\x00\x00r\x08\x00\x00\x00c\x02\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x06\x00\x00\x00C\x00\x00\x00sD\x00\x00\x00|\x01t\x00d\x01d\x02\x84\x00t\x01g\x00\x83\x01\xa0\x02\xa1\x00g\x00d\x03\xa2\x01t\x03\x83\x03\x83\x01|\x00\x83\x01t\x01g\x00d\x04\xa2\x01\x83\x01\xa0\x02\xa1\x00t\x01g\x00d\x05\xa2\x01\x83\x01\xa0\x02\xa1\x00\x83\x03S\x00)\x06Nc\x03\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x03\x00\x00\x00\x05\x00\x00\x00\x13\x00\x00\x00s\x18\x00\x00\x00|\x00\xa0\x00\x87\x00f\x01d\x01d\x02\x84\x08|\x01D\x00\x83\x01\xa1\x01S\x00)\x03Nc\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x02\x00\x00\x00\x04\x00\x00\x00\x13\x00\x00\x00s\x14\x00\x00\x00g\x00|\x00]\x0c}\x01\x88\x00|\x01\x83\x01\x91\x02q\x04S\x00r,\x00\x00\x00r,\x00\x00\x00)\x02r*\x00\x00\x00Z\x03___\xa9\x01\xda\x01_r,\x00\x00\x00r-\x00\x00\x00r.\x00\x00\x00\x1a\x00\x00\x00\xf3\x00\x00\x00\x00z.<lambda>.<locals>.<lambda>.<locals>.<listcomp>)\x01\xda\x04join)\x03\xda\x04____\xda\x02__r1\x00\x00\x00r,\x00\x00\x00r0\x00\x00\x00r-\x00\x00\x00\xda\x08<lambda>\x1a\x00\x00\x00r2\x00\x00\x00z\x1a<lambda>.<locals>.<lambda>)\x1dr\x1a\x00\x00\x00r\x1a\x00\x00\x00r\x0c\x00\x00\x00r\x05\x00\x00\x00r\t\x00\x00\x00r\x07\x00\x00\x00r\x04\x00\x00\x00r\x02\x00\x00\x00r\x1a\x00\x00\x00r\x1a\x00\x00\x00\xe9(\x00\x00\x00\xe9"\x00\x00\x00r#\x00\x00\x00r\x08\x00\x00\x00r\x0c\x00\x00\x00r\x0f\x00\x00\x00r8\x00\x00\x00\xe9)\x00\x00\x00\xe9.\x00\x00\x00\xe9d\x00\x00\x00r\x03\x00\x00\x00r\x06\x00\x00\x00r\x07\x00\x00\x00r\x05\x00\x00\x00r\t\x00\x00\x00r\x04\x00\x00\x00r\x03\x00\x00\x00r\x10\x00\x00\x00r\x10\x00\x00\x00)\n\xe9<\x00\x00\x00\xe9G\x00\x00\x00r\x17\x00\x00\x00r\x18\x00\x00\x00\xe9S\x00\x00\x00r\x16\x00\x00\x00r>\x00\x00\x00r\x19\x00\x00\x00r\x1b\x00\x00\x00r\x16\x00\x00\x00)\x04r\x03\x00\x00\x00\xe9x\x00\x00\x00r\x03\x00\x00\x00r\x06\x00\x00\x00)\x04\xda\x04evalr(\x00\x00\x00r)\x00\x00\x00\xda\x03chr)\x02Z\x05_____Z\x06______r,\x00\x00\x00r,\x00\x00\x00r-\x00\x00\x00r6\x00\x00\x00\x1a\x00\x00\x00r2\x00\x00\x00r6\x00\x00\x00sq\x19\x00\x00x\x9cUZ\t[T9\xd7\xfc+l*\xab\xde\xdc5\x11\x18vA\x11\x14\xdc\x10[\xf1.\x89\x80\xd0l\xad\xe2\xc6o\xffR\xa7N\xcf;\xdf<C\xb7}\xd7\xe4,u\xeaT\xe2o};9yV\x9f7]=r\x84\xfff\xf9u4\xf2X\xff1\xe9\xbf\xd7g\xff\xef\x9aY\xfc\xaf\xe7\x1f\x9e^\x9c\xf4\'?\x1cM\xc6\x7fO\x8d\x84\x8bk\x1c\x1d9\xe9\xc7\xaf\x8fSS\x93\x0f\x1e\xcc~p\xc5\xec\x08\xfeL"\x1f.~\x98\x14\x1f\x06\x1f9>J^\x81\xbf<\x99\x1d\xc9p0\xc55\x89\xd5\xfb\x9c\xe5\xe1<\xde\x94\x978\x98\xe0#\xfern\xf8\xac\xff<:\xd7\x93\xc6\x14\xf2\xf1q\xb6=\xbe\x8e\xe3\x91\x19M\xcd\x8e-ln\xbdx\xf5\xfa\xd5\xee\xc6\xeb\xb1\xd91\x1f\x8d0\x16O6\x0fn{\xb7\xae}s\xd8\x1b|x\xd5\xbbm\x9b\xde\xadI{\xb7\xa1\x9d\xe9\xdd&\xa6w\xdb\xb9\xf8\x1d\x0f$6s\xf3\xbd\xdb:\xe9\xdd\xdat$~\xd8x,\x7f\x89\x8f\r\x9c\x8d\xb7\xa6xP<\xd3\xbd)\xe3\x91\x0c\xa7V\xee\xe2\xa3\xe2#]\xfc\xf35\xfe\x16\xe2#C\xef\xb6i\xf8\xddv\xb8\xd1}\x89G\xe2M\xde\x0f/\xe3\x9f\xf5o\xe2+\xc3t\xbc\xa6\xc4\xdf\xc3xS\x8b#\xf1\xf2v\x80W\xada\xa8U<\x17\x87i\xf1\xbc\x8c\xd7\xda6\xbe\xd9\xc4\x83u\xc3\xc7vxQ\x11\xaf\x0e\x8b\xf1\x12\xeb\xf0\xaf\xf8\x87#8\x9bs\xa6]\xfc\xed\xe3\xb7\x8f\xdf\x9d\xe59\x1f\xad\xe0,\xaf\xef\xfc\x19.~\x17\xdf\x1f_\xda\xc4\xa3]\x1d?\x9a\xf8\xf0\x10\x1fa\xe2%I\xc5Y\xf9\x92\x8f\xf0\xc3\xbf\x1c#*w\xe2\xe1\x10\x8d\xd8\xa4O\xf08\x98:\x84\x0f\xd1\x07M\x16?\x928\xda`p]\xfc\xcez\x03\xccs5S/\xd8\xcb\xf83\x9e\xb4\xc5\x97\xe7qb\xb0Q\x86\x07\xc5\xe1\xc5w\xbbjmi\x12\x13\xbf\x8a\x97\xc7\xab|\xc2q`\xd8\xae\x88\xf3\x08\xf1G\x83y\xfb/\xb0\xee\xcb\x8b\xc3\xf8\x9e\x86\xa6\xeb\xf0m\xba\xab\xebx\x06C\xa8\xc6{\x0fNw\xe3;\xe3}m\xfc\xab\xbb?4}\x88\x7fM\x8d\x87}\xe3\xeba\xf0P\xf2u>\xffL\xd3\xd9\x0e\xbf\xec\x05\xadPc\x94\xdd\xee\xa3\x99\xef\xdf\xe7\xf1\xaf\x9c1\xd1\x95\xb45\xe6\xd6\xc4\xeb\xbbl&U+;\xba\x1f&\xc5w\x972Xl\xcd\x01\x84h\xe2`\xc5B2z\x98\xbc\xd2\xfbBx\x1f\xa7\x15\xc7\xe0\xe2t\x9dg\x00\xd8r~1\xfe\xca\xf8b\xcc0\x89W$\xe5\x01\xae\x7f\xc600\xc5\x8f_\xf1\xea\x82^\xf4\x08\xb3\xf4Q\xfc\x91\xdd\x1d\xc7\x9f02\xc2\xcb]\xd2XIx\x8e\xb9\xc3\xacbp\x89\x9b{|\x12\xe6\x1b/~\x10o\x968\xc3<\x11kf<\x9e\x8bC\xad\xdb\xe9\xa5\xf8i\xbfq(x]\xc8\xd6b\x907p\x917_\x9eE\xf7\xb5q\x00m8\xed\xf5\xfb\x18T\xca\xcc\x94\xec\x84\x7f\xfc8\x86\xc0Hj\xcbw\x12\xea\x0f\x18\xaeuIc\xb4\t_\r\xe3\xc0\xd4\xae\xfbD\x83H`h\xb2\x19\xb1\xdak\x9a\xb45K8{\xf1\xfa\xee\xe8\x1bb\xe7\xd5\x01\xdd\x81\xe8F\xbaK\xd8VK\xe7\x1f\xaf\x18Lm\xcd7\xd5\xe1\xf2\x7f\xfeB\x84\xf9\x1cF\xf0\x1c\x0f\xc29\xc4\x83\x0eN\xc4\xc1\xc4\xff\x9e\xe7\x0bq\xb3\xc1=\xe1\x96\xc8\x92\xb47\xb0a\x1bmk\xd5Y0\x18B\xbc\xab44k:\x00\xb9\xe7\xeb\xb7\x98\xa3Q\x18q\x1c"\xf25\xf1\x15r\xb4L\x18\x81x\xffpp\x80\xa9P\\\x01\xab\xa6h\xa5\xd6\x96\xb4\xa6s|\'bZ\x02\xd7o\xf2e\xa6H\x0e\xf6\xae^\xc2f\t#\xcb\x88\xab\xfc\xf1Gb[\xb0\xf3\xf716\xc79\xc3y&\xfb\x1cc\xceW42P\x02\xe0\x08\xd8\xa8sF%r\x19\x81\x914K7Hu\x13f\x19\xd7\xb8(\xa4\x8a1\x81\xe9-3L\x00\xce?f\xee\x98\x940\xb3m\xe8#\xa4\x86\x18\xa0\x9b~\xf87\xa3\xf90\x1a\xc0\x1e\xaei\x1a\xdce*\r\xd5\x82o\xae\xb3~\xcb$\x8c\x19s\x1d\xe3\xc3\xe6\xc4\xa0\x06\xd6\x87!1\x9c\xa4\xc4\x81\'\x98R\xfcG\xbe\xa6\x80Z\xcd2\x0c:\x7fC\xa4k<\xf3F\xf0\xbd\xe5\x18\x9aN\x014\xf9\xfbx\x8cC\x92{py\x1b1\xc5\x1a&V\xe8\xe6\x16P4\xd6\xe6\xf5\x19\x00\xe0pE?\xb4\xe1\xe8\x13\xa7\x8c{\xady\x05\xb3<Q\x94L\x90P\xc8\x8f\xf2\xa7\xd6\x1a\x00\xad\r?7\xb6\xe1\xc9\x0f0\xdb\xca\'\x8e*\xd8G\x00C\xfc\xf8y~\x85\xe0\x8b\x18\x98h\xa2\xd4\x02k\x1f\x9910y\x93\x13z0\xbe\xf8\xef\xc1}\x14\x0b\xf7\x9e!\xdd\x95K1\x1e\xbado\na\xfb\x15\x89\xd3^\x00c\xa6\t"\xae\xb8d\x11\x94\xa9\xa6\xa8e\xcbx\xcc\xf2\xb3\xd5IVV\xdb\xfc\x84\xcf\xfe2#cA\xbc\xe6\xbf\x10\xe1b\x02\x94Z\x81\x99\xca\\\xb1\xc42\xd4\xe8\x9e\xba2\x021\xd9\x97\x08\xbaM!\'\xfax\r\xab\x15J@\r\x1c\xb4-\xe1+\x04T\x07\t\xfe\r\xc6\x0cR\x0b\x07L\xfe\x1b\xb1\x0e\x87e\xa8\xec\xf5dR|~\t<\xd0J"\x11\xe3\xceYa1\'W3\xe2b\x82lm\xe5\x1ay\x08\x83\xd6\x7ff\xa86\r\xd0-\xd9\xd8\x1b\x16\xa2\x03I\x12F@m\x9e2*q\n\xcf\xf3\xd5\x14\xd3\x01\xfe\x85GQ\xb9}\x15Q\xc1w("\xe6\xf3\x94\x02\xba\x9b\xc6\x8cv`\x8e\xf1y\x00l\xf9\xb1\xf7\xe0\x9fZp\x06\xe6l75u0:C\xa0\x13\xe4\xe9\xe8\xcb\x00\xb6"T\xa3"\xa6\xd8B+\x7fJ\x0cK\xaa]\x82\x93-\xf7\xc0`X\x031\xea\xb6X$\xf5p\x85[EuP\x18\xad\xb7\x81\xb6\x88\xae\x80\x8c\xaf\xa5J\x0e\x98\x0e\xad\xfb\xca\x08\x80\x9d\xe1$S\x1d\xad,&{\xd7\x08\xbb;\x1eFz\x18\xa9\xf5\xad\x7f7\x02 \xfcJK#\x19\xbbV\r\x1a\x84k \xf0\xe7\xf9$\xc9\xacB\xcd&\xe54\xa5\xbb\xe0p\x17\x04\x1b\xe6\x89!\x08\x9d\xba\xc3,J&\x8d\xf5\xb3<\x83\x14\xb5\xc9\xc3}\x84H\xc4R\xd3\xce\x11\x88\x83\x9fg\x96\xcb[\x9a\xeb\'\rkGb&\xe6\x10_\xdf\xceYBCn\x95@$[\x0cK\xd8\x14\x89\x03\xb7\x12\x040\x81z\r.\x19A\x88\x07\xb8\x03\x80,$\xa9\xe5k,2 \xbcE\x85\xc0cb\xea\xc8P[\xa0\x11\x82:\x9c\xbc\x8c\x961\x86T\xaa\xb5\x08\xda\xc1\t \x00/7\tg"\xef\xac\xc9W\x91E&\x07l\x94;g\x1cR\x93\x1f\x11O\x90}\xcd\xb0z\n\xbco\xfed\xe6\x18\xb8\n~\xc6kj%}\xf04R\xda\xfb\x81\x1eE\xec\x0b\xda!\x85\xe1C$&\x92\xc2\xe7\x0fw1\xdc/\xf0\xc7"\xcb&.\x96\x02\xdc\x94?4\x1bjr\x17\xe3\x0e4\xb4\x04\x82\xce`\xf7\xdd=\\\t\xbc\xca\x167ny\xaa\xc3\xa3\xe1\xb7\xba\xfd\x00\xa2\xf7As\xb7\x83yno\x19)^k}H\xa7_\x8e\xaae\x03\x99\xae\x000B\xd5N\xce\xb0\x1c!\\\x11\xbc\x89\xef#b\xeas\xa1\x9a9\'\x11\xc4\xbc\xdf\xf9\x02\x97\xf7\x91\x85z\x8b\xa7e\xe2\xd8\x94\xca\xb8\x0f\x9fi\xff\xae:\x04\x1bK\xceX&\x12\xad\xfe\xc2\xa7,#\xb6\xad>\xd3\x87\xd1\xdb\x0f~!\x002T\xadnA\xcb\x8c\x9ffYG\x19\xf6\xd9+\xf8g\x02\xe1\xfc\x16\x11\xb7.\xd3\x18(<4#\xa7B\x05\x07t[\xe3\xc6F9 \x98\xb7+\x7f\xe9\x00*\xe1Bj\xf1\xd6\xec\xb2\x96\x01\xf0\xdbt\x8b\x84\xd6z^\xdb\x98u1\xd8\xb562\x92{\x87\x80\x01fURf\xa8_\xe9G\x84u`\x0c\xc1\xc6\xd6|!\xe7B@5\xf5\xc2#m \x00\xbf\xed/6SHf\x00P\xe3\xf7\xb6\x9f0 \x10\xf0\xb5\xd4\x16\xd0\xcf\xf2\x856+\xa5\x96\xb9\x92&\xb1v\x06fK8D\x10\xe7\xa6\xd8\xcax\x9d)\xaa^\xff\x99\x96h\x0b\x98h\xdaSfU\x17\n;\xb6\xb6|0Kd\x10\x8by%\xf9\xd9W\xf8`\x9dL5i\x19W\xd2\x8d%\xe4\xcd\x82\x92\xa8\x91I\xbe\x0e\xf3\xfb\x05\x85eG\xfe I\x8e\x02W\xef\x92\xe8 \xca\\\xf3\xf1\xf3y 95U\x8c\x18Sw\x03ukA\xee\x95\xb4\xbfe\xda\xd7\xcc9i\x89\x0c\x9d\x8d)\'\xd5\xce\xc8{\xad,Z\x00Lq\xb9\xc1|K\xcc\xdd\t\xd0\xb2\xbe]f.\xf1\x0e\x98\xfa\xb2\xdb;\xc0\xef\xd7\xa8\x06\xc0\xc2\x88\x98\xdf\xf9\x0c\xaf@c\x844\xcc\xbd%V\nD\xe6(\xa8\xd9)\xce\xe1\xee\xb0\xb5\xfa\x02\xb0\xb2\xcf\x8c5\xa9\x94\rSOap\xf5%i\x8am\xef\x0fh\x024\x12\xdeO<gv"\xb3Z\xa1rW\xa4\x06m>\xe7\x9fr\n8\x97\xb41\'l\xa5 \x87AW\x92h\x93|\x98\xad&\xb5\xde\xa1\x14\xc7\x91\xdc\x12\xc0\x84u\x00\xd1PP\x80/pzh6\x87=\xb8\xf2\x13\xb7\xfc\xba\xd7\xbbQ3\xe5\xc2\x080\xa6\xe2\xe3\xde(\xfd\t\xdf\xa1t6\xb9vi\x16\xa1\x88x2\xe54\xae\xfe\xcb\n\x89)\xc73\xd7J!0\x84&\xfd\xcb\xb7H\x99\xa8\x18\xf0\x12\x89\t\xa3\t\x11i\x05\x90W1\x7f\xe4n\xf6\xf0;\xf2@\x0b!,\x05\x14\x91\xb6\xbc\xd3^\xdb\xd1\x87Ms\xc2\xa2b\xb4KK4N\x85\x86;Bd"\x16z\x8aW\xac`\x9c\xaf\x08/\xd2\x19\xf8\x15X\xe8-\xa2\xe0\\\x11Q\xdbYTi\\\xe6\xd1d#\x03\xe5\xb1\xc8\xf2\x0c\xc8\xdc\x8e"\xcc\xef1\xd3\x85\xad\x96\xbb\xda\xe3c\xac\xd2Q\x97\xc4-S\xd32\x129\x9e\x13j\xec3\xbc\xe6XA\x1c\xe9\xe7\x81\xc0mus\xceP\x81+\xe1\x90.\xdc\xf4Y\x12\xa5\x0b\xea\xa4\xb0\xf4A{\x93\x85\xb1\xa7\x08\xc1\xb1G\xf0\xe5\x18\xabv\xa8\xc2\x0f\xd0\x16\xe1,;;\x8a\xc8n\x9fI\x87\x8cq\xe0\xa7>\xff\xfbpN\x18\xcc`\x16I\xd4\x97d\x1ep(\xc8H\xb8EB\xab\xc1@\x1b-0\xb12\x0e\xe0\xbew\x8c\x1e\x8cX\xa8\xb8\x085\x9bOOy?B\xc1\x81o6vkvX\xd4\xb4\xf5B\xfd\xb4v\rUg\x9e\xac")\xb7y\x0b\x06\x88\xc6\xa1F\xaa\x87j\x1c \x91/\xad,\xb6\xbc\x0e\xee\x04@v\xb6\x1a\x01m)?\xe3q\x1f\x8b\xed\xfe\t|\x8c!\xf9\x03p\xf1b~ \xc6\xbaf\xe5\x02\xff\xea\xfc:b\x15\xe1\x99<\xc6\xdb\xee! /X+\x84\xbf\x1a\xa9\x00\x1c\x00p91o\xb4\xf0Y\x82\x8d\x13\xbe\xbc\xab\x00\x86 \x91\xf9d\xcc\x10\x9b/\xec<c\x81\xebRD\x92-\xad\x8a\x07\xd2]4\n!\x8es1\x18T(\xd6\x97nI\x8fZ\xc3\xc0C\xff\x00[\xdb\xc4"\x85\xcd\'m-\x12-z\xc81t\x83\xd9sm\xca\xfd<\xc6l?\xd3\xba]jnhk\xd0\xd3\xda\xb8)D\xdf\x1d\x83\x00\x946\x90\xc5\xf5\x010:\xb2,\\\xac\xbfx\x8c\xd4:\xe6\xf8m\xf6\xa2{\xc8\xa1\xd6\x85\xb4^gd\x89\x0e)\x01\xde\xe4\xf2\xad9\xa5\xc8\xed\x96\na\xf6\x0f\x10F4\x03Vg\x19\xb8\xafX\xfd\x9a\nBQ=\nU/\x9a\xbc?\xceKlX\xb1`?\x8dvq\x08\xba\xa4Z\x99Y\xe54\xc1\xfd|\x01\xb8n \xabtW\x1cG\xed\x8b\x9b\xfb\xac\x88\x98j(\x0f\xd5\x07\xed\xce\x92\xd6 irg\xef\xc1\xb8\x93\xcf\xb4ahYZ\x90\xab\x06\xf4\xacE\x81j\xa5\xd1\x7f\xbc\xdeW.Y/\xd1\t(\xebRv\x93>\xfc\x00q\xa2]\xe4\x9cq\xb8\x96\x81NH\xc2?\x18\x05A\x10\x99\'A\xd5\x00\xe8:\x15\xf0\x104._\x7f\xc2\x1e\xc1\xd4\xcbs\xff\t\xb7\xfc\xb5\xb6\x0eAky\xf5n\x1b\x91t\xbd\xf7\x97\to\xec\xce\x8a\xf2B\xbc\xb39R\xe5!c\xfd7\xa8\xd5.\x1bg\xd2\x01W\x9d\xd9dQFBv\x90/-X\x16&\x93\xa4\x1e\x94.\xb8o\x88\xc4\x13\xa2Rp\xf9\xf1\x11R\x18\xd9a\x7f\xd0\xea\xa8\xa8M\x83\xc6\xb7D\x13\x91~aSc\xcd;<\x05\xa5\xdf\xa1\xab\xb1o\x91\x17;<)\xb1\x9d\x0f\xe9\xe4\n9\x9bM/\n\xb5y\xbe\xbcB\x92\xee\xbb\xd9\xe4#\xcaV\x9b\x93:DV\xd5\xdf\xd3\xf0\x16\x85\xd2\xc3\x9a\xf3^) \xc6R\xbd\xff\xa5\xd2\x95\xf6X@\xfe\xae\x85\xd0T\x9c0\x8am\xbav\xade\xc2\x9a\x8bM\x02q[L\xb3*\x86r\x15\xd5\x08\xb1\x89\xfe9\xf9\x82\xd7\xdd-\x10c\x9b\xe4\xb5\xf4e\x83\xc2*y\x19&Z\xb7\xb2\xb7|\xa42\x08\xe6-\x82F\xdb\xeb\xff\x9c\xff\x84\xc0\xfa\xa88\x9d\xa7\xacMu\x1d\xb6\xe7\xd6$@\xc6\xd4\xe6\xaa\n\xb4\xd2b\x9d++i\x19\x9f\xa1\xba\xff\x9d]\xa2\x11\x9e\x01V\x9d\x9f\x009\x9e`P7\xd4z\xc4\x08JV@@}\xb8Y\xd5\xda\t\x05\xa9\xdb\xfd\xa2=a\xae\xbdv\xb9\x8e6\xb8\xde\xa1\xb9[\xc3\x16\xd6\xabo\xbaj3W\xd5\xaeSY\x13\xcdI\xfd\x87\x8ac]\xec*\x1fI\xe9!\xa7\xe1Y\xfb\xafct*\xf2\xbf-\x97\x9fi/\xeb\xca\xbe\x1643qA\xa8o\xfd=\x8cnL\xf4\x8b\x15\xc4T\xad\\C\xfb\x02\xd7\xf6\x0f\x95d\x8a\x0071)\xea~\xfe\x0f#\x02\x8a\x1e\xd2\xbc\xf57`@\xad/W\xbf~\xb8\xa1_\x90W\xb5\xaa\xb6v(\x9a\xa7\xda\xb4\xe81\xc0Qk\x97\xf1\xf1\xe7\x9b\x12\xefd\x06C=x{\xcdW\xd4%\xbfq\x1bB,\x14\xd5&\x03Y\xf4]K\xe6T\x0f\x9b\xf6\xf4\xef\x82*p\x81\x81\xda&\xf7\x99t\x9dP\xb5\x13}qF\x04\x03S\x82\x87\x9c\xe5q\xa1Av{\x82<\xb6\x11\x08~\xc2\xc7\xcb\x9aG\x90\x05\x8ag*\x18\xdb\xca\\\xe8X\xb4S\x8c\x8e\xe8\xe1\x9d\xef/\xf1\xf9t\x1bx\x88~\xc6\xb0\xc5\xc0\x04$\x84P\x1f\x05(j\x86\x1c\x80\xd7J\x94\xfc\xa3MTqz\xa0\xb0\x86:S\xef\xdeW\x02\xa8\xf9\xd7J\xab\x83\xea\xe5\xbf\x91\x0c\xc5*:x:\xa3k\n\x15yz\xbc\xa3\xf7"gH\x82Fb\x0cx\x9esP\xf5\xca\x05 A;\xba\xba\xd8\xfbWw\x0f)t4\xe9\xaa\x11\xce\x01K>\x88\x94\xba\xfd;\xcf\xd0\x08as\xb8\x02A\xfaa\x13\x15\xf7\xf1]\x8cwD\xd0\xfe\xce\xb1vZ5}\x8f\xa7t\xf93Lj\xf0\x8ea\x83\xf2\x0c\xdfZ\x97\xd7\x8b\xd3\xc4\xb9\x06\x8b\n\xc1\x8eksQ\xa8.\x11\xbe}DF\xff\xe6s\x84\xaa\x81&\n\x92\xe6\x87_\xaf3z\xabA\x972\\\x9dj\xf2Y\xb0I\x954\x9d4W\xc3\x89\x19:\x85\x92\xf47\xc1{\xceJ$\xcb|\x93\xf9d\xed@\xf5\xd0tW@\xe5Z\x98\xd2\xb1v\x9f\x8d44\xd3\x031z_e\xbe\xa0\xc4\xaa\xba\x04gI\x90\x17\xf5\xb8\x98\xe4\xc1\xbef\xb6%~"\xb4;,r\xb5\xed\x1bf\xb9\x08\x03)\xcas\xb9\xee\x89\x83\t\x89~<,KA\x8f\xe0\xc8\xb7\x1c\xa6I7\xfatA\x9d\xaa\xf8\xe0\xf2KU\xb0\x84hc\x15\x07\x04\x0e\xf8\xc0~\xa5\xd1\x0e\xb0cF\xc1\xc6\x92]\xe00m\xf7\x95X%\x0b\x81\xf9G\x9a(\x00T\x92v[\x85c\xb70\xac\x06f\x8a2\x93\x15d\x90\xde\\]\xd3\x16\xfe\xf0\x9fi<\xe3\x90\x83\xc7\x89\xa4\xd1\x12^1\x17E\x98r#\xdbK\xe0\xe8\xf0<L\xe20\xb7\x0e5\xafI4\xac\xebW\x83\x1e\x1eN\xd0#RK;\x93\x9d\xd3\xcd\xa6\x1e\nJ(0\x07\x0f\xb5\x0bL\xd9Y\xd4i1C+\xda\xfc\x03\x12\xff\x06\x1f0L\xfd\x0c!\xf2\xa2\xa7:7\xdeW\xa2\xda\xf9\xdb;fi#\x02D\xa7k\x82\xd20\xa5\x0cZ\x88/.y\x8e\x87l~\xdd?\xa4\xfc$y`\x89)m\x8a\x10)\x97\x18aI\xf2\xe4\xd3\x1e\x8b\x84\xcd\x0f\xdd\xe3s\xcd\x1a_\x8f)\xc7\x04k\x11\rS1\xc9\xd7g\xac\xd2m\xc9$0\x1a3^\x98?\x08\x92\xaf\xeb+2Q\x83\x95&\xbc\xb9\xd6%\xd9\xa0\xd2*l \xd9\xe3q\xc4w\xd0\xfd\xfc\xd3_\xf2N\xf4\x0fh\x97B\xb7\xba\x8bp\xfa\x0c\x0b\xc3g\xf0\xb2\xf3@\xc0\x16\x85\xce\x81K\xc8R\x90\x9d\\F\x85\x1a\xbc\x82c~\xf5D\xd3|\xa1\xf4\x155 +\x94\xfdf\x13\xec\xfc\xd0B\xca\xd9V\x81\xc2)\xbb\xcdU\x9fB\xfa\xf8Q\xa2\x9f\xd1U\x00_\xfdP\xbcm/1\xa3Q\x8c\xbf\x90\xe6RW\xc5$\x80r\xed\x15S4\xc8\x8d\xf6N\xe0\x08\xb2\x92\xa0\xa2`W,l\xa9<\x88l\xcaO\x19\xf0NVU\x9bK\x1a\x07\xb5\x08\xa5DzT\x85\x1bP\xbd\xba\x1b\xbd`\x06H\xb46`\xd6 \xf9]\xb3\xae\x99\xeez\x83\xfe\xc6c%\x84\xd9rr\xff\xa2\xd7\x9ba\xe5\xf0\x8a]I\xa8\x9eLp\xf6\xa2gW\xac\xe4\x94\xb6lz6\x94\x83\x81\xc0\xc5>\x1bW\xc4\x81\x01nt\xe5\xbeF\x83jq\xa2jV\xd2\xd6\x19\x12GQ\xe5\xa5\xa3=\xbeG\xd2%K\xac-\x1bL\x11\xa2dE\nR\x1bD\x90\xda\x1cb\x96gC\xc5e\x05x\xec\xe6\xd4\xfc\xe8\xd6S\x89\x9b;J\xa1\x18o\xa2J\xb9\x88\x01"i"q\xed\xc1+\xbeY$\xa1\x8e\x0f\xf0\xd9\xcd1\x13\xdd\x17\xeb\xda\xe6\x08\xab.\xe7\xdbkV\x0f\x00\x86\xa9\x0fZ\xedIr\xe0\x96\x7f\xf5P\xa1\x01O\x0e\xbf\x9f#*\xf7/\xf9zS\x8d\xbff\xe2!\x94\x1a\x04&:\x15\x9f\xbd\xd5\xaao^\x7f\xe0 kq\xe2\xdb7*\xc5\xf8\x8b\x0b\xb2>\xf0\xad\xba\xbeK?\xbdV\xb5@\x97\x95]\x86\xde\xa5\x1c%\xed\x12\x04*T.\x94\xad\x05\xcd\xde:\xbc\xfd\x9e\xf3\xc3\xf4\x9b|\x8b\xe7;\x95\xf7\xa5\xc3\x12\x96%\x9a\xf1\xdc\t\x13\xd2\xe79\x87\xd3$LB|\xa37`\x97\x04\xfcZ!K\xf1\xb2\xf8dG+(9\xb5\xae\xc6\x99v\xb5\xd7\x7f\xc2\xb8\xf3ir\xab\xcc\xbc-\xff\xbe\xed\xf5U\xe3\x97\x06\\\x14\xa4\xa7\xaa^\xa6\xb2\xa4\x80\x17W\xbf\xe9=\xe4[\xe7\x19,p\x93\xacn\x04vu\x8f\x10\x19\xef\x89+H\x07\x00i-B\xe6=\x1dv\xb2\xbf\x01\x81\xae\x9bRE\x03\x1d\x86P\xa6T1=k\xc7\xb4b%\xd3t\xa7\xab\xae T\x94s\x8b\x8a\x86J9D\x19ni.+\x9a\xf2\xebb\x9b\xc4\'\x98\xf7Sd4\xa1<U\xdd\xa5\xd3V\xa0S\x143\x8c\x8e\xc6->G\x86\xccB\xee.vx\xb1\xecU\x81\xe3\xbbaF\xa8\x8c\xe0\xcc\xe0V\xf7l$\xd2\xf1\xe2d\xc8Q~\xeby\xc9\xfa\xeb\xbe\x12\x03\xe1\xeb\x87\x10*Pz\xbdS=;\xd6\xb5k\x15Vt\xf5\xac\xad\x1e\xa9,k\xdf0\x86BB\xa2P\x17}\xa5/\xc3\x85\x9cz\xd8\x7f#\x02\xfe\\@\xc8\xcf\xcf\x19\xd2",\x01\t\xea\xc7\'%\x03\xc2\xab\x1eVg3kh5\xd2/k\x08\xe6\xb5km%\xf23\xc2\xbf\xd1\x05\x9f\x0e\x8c!\x96\xb7\xfe\x93\xe7\x8c,\x11\xcfP\x02\x92\xfbaU\x9d\xe4\x87\xbcx\x12\xd5J\x95D\xd7=U\x998c\x94\x84\xf4\xe7\x14\xcc\x86\x19\xd70\xa9\xacU\xfb\xe3\x17\x1b[\xfb\x13z\x13\xc2\n\xb3\xaa\xfd!\x11)\tk<\x92\xb4\x18\xa3\xf3s;S\x07\xb0:V\x14\x83\xdb\xfa\rG}\x86\xfd\xa4%\xb6\xcc^\x03\x14`\xefN\xda\xde\xb6\xd3L\xa4.|f\xf9j\xab\r\x8d\xe2\x86\xf7\xf8f\x8f\x15C\x96\xd1\xbb\xa3y\x0c6\x9c*\xe0\xab\x0c\x15\xb27\xdf5\xf5\xach\xcb\xc2\xce\xb1\xb8U\x1d?\x7fIk7\xc5\x12\x1c\xd7i\xaaw\x8al\xdaEK\xb0iF\x9bd\xf6\xec\x91\xb6O\xdd\xae\xaaR\x1d\x8d\x1aJ%Z\xf2\xef\x8cT\xc8q)\xe5\xeb\xf1)\x9c6N\xcdIzl\xd9\xc5p\xf3\x9c\xc0.UM\x9a\xc4d\xfd\x12\xb7\xa3\xb57\xf7\xf1&@^\x96\xc9c{:\xff\x8e\xac\xa2\x96\xad5\xa2\xbd\x1f\xab\xba\x9b\x16\xcaH\xb2m\xc5Lx\xbb\xd8d\xdaH\x1b\xa4\x9bB:m\x82DPI\xb5\xf1HT\xc0\xc6P@:\x9d\xeea\xf1\xbaS@\xb4\x16\xe0\r\x144\xe9\xd6T1 \x93\xc7\xb2o\x10\xa0\xe3\x9a\t\xc6\x9f\xac#\x9bG\x14\x96;\xc7\xf4\x175\xdc*[\xef\xce\xbf]\x11.\xb8\xea\x98"\xe2\x9b\x81vR\xb5\xca+\xe8\xfe\x9b\xb0\xa7"i"\xe0Da\xfb\x01\x9b=Y\xbf\xf3\xf4\x95D\xb1\xc0\x8avo\xc1\xadF\xf3\xf5\xf7U\x84I\x17\x97\xf0b\xacE\x02\x9c\xec\xd1\x04\x96\x8c\x93\x8doJA,\xf3NV\xf8\x92w\xd3+O\xb5Am{\xd7\xe95\xab\x9b\x93\xfa\xdf\xfe\xfcI{\nE\x83\x82."\xa7}\x9a\x90\xc4c\xe8\x82wE\xce\xfe]v\xafh!\x06\x086\xba\xd0"\xe2s\xaa\x9a\x8d\xc5\xe2\xb5SQ\xc1)\xabu\x05\n\xa5\x81\x96\xd1M\xd3\xcd\x9d\xae\xaa\x88H\xd5\xec\x9f\xc0\xbd30\xb5\x1d{\xce\x140\xed>\xa9@\xa7\xcb\x1fxW$\x0c\xd7)\x1fn5\xf0\x10W\xb2\x96#\x1a\xb3?\xc6\xc8\x0f\x987\xf0/\xf2B\xb8f\x86\xc5]\n\x1f\xd9ob\x9a\xa8\xe9\xa2Q&\xf5\xbe\x06W\x0eQ\xcd\xedJ\xe7\xd7\xd3\xd2\x85K\xb1\xd2\xed\xc0}\xd1e\x8b@-m\x07\xf8\xba\xb4\x10\xf9`\xe9\r\x89*H\x8d\xc9\xc7{\xd7nm\x93\xe3\x80\xaa\xe9\xd0l\xfc\xab\xebWss\x07\x18\xceW8\xfa?\xdd\xaf\xac\xf8\xaa\xd8+Z\xb9\xaa\x90&\x05\xf3i\x0e\xc8\xddd\xf1\xaf\xd9\xa0\xeb\x9c"m\xdb>^\xde\xbc\xff\x97Z\x90lH\x18\xee\xdcH\xaa\xb1eR@\xd1"\xa0Y\xc9\xe6\xb2L\xd3D\xe4\x91\x15\xce\xaaM\x7f\x92j\xe3,1e\xf0\x08q*\xb7\xeb\xe2\x81x\xa2\x99\xd6%\x0c{O\x17XJ\xd2\x92*\xbc\xfa\xf0\x872r]\xbd\x99\xc1\x16\x95\xec\x17|\xba\xaf\x05\x13\xd8_\xc9\xd6\xa0\xf7CQ\x89\xc1\'\xb4\xd0\xf3V\x87\xe6\xeb\x81*Ha\x8b\xd1\xefE\xbb\xfaI<\x18\xae\xd0\'\xb2\x9d*\x1d]P\x8e\x0c$@\xc7\xec\xd5R!_\xa6Q\x0c\x97\x90\xd1\xfe`W\x1cX\x03\x82\xdca\xcd\xd6\xea\xfa\x88\xcb\x07B\x9dz\xaa\xed\xb4\x1b\nxXB\xaeu\xa3\x00x\x8a\xc9\xff\xd2\x10\xc2T\x0b\xac2\x86\xf19\xed\xe4\xda\xde`\x92\t\x12\xb2\xed\xc3?*\x148\xdd\xfa\x15\xd2q\xddtVr\xfe"\x0f\x17g\xd8\xa8\x15\xa6\x18o]\xb5\xfa\tW\xaf\x1e!9\xa1\x10\xf8)>A\x08(\xf6\t\xd5\xe8\xfd\x1d\xf7=\xf5gX\r\xaf\x0f\x95\xddc\x11\xa6\xc9\xd7\xde(\n\x82\x90a\xb7\xd1\x10\xc3\x1b\xac\x88\x9a\xf4\xbb\x82F5Ms"\x97\x9a\xf4\x85\xe6;\x00<Q!N\x04\x1eY\xc0[E\xd5n\xd6\xd4\x19\xa5\ni\xdd5\x8b\x1fr\xa1\x15\x1d\xea\xf0\x0bV\xb5\xcc\x0b\xc8\xdf\xf5\xf3I\xc0\xf06\x07\x10I\x0b\xf6P4\x7f{\xbdo\x8a\xd8\xc9>Vh+\xa4\xa8,\xaf\xd5|\x8a+K\x98\x1b2\x06bD^\xdbt\xf3?\x08@"8y\xd2\xa1\xae\xc0\xf6\xa5\xfa>\x1b_Y\xa8\xae\x8e\xf6&\x94,\xc3\'\xc5=Z?ft\x8fp\x0b\xbf\xc2/\x8d\xeeCpB\x82\xe7\xf0\xea\xf5_Zct\xe9\xac-&{\xffn\x0b\x14\xb1Y\x16\xa3\xfe`\x19"\x1f\x91!>\xfe_DZU\xc5\x1a\xa5\x8a\xedpo\xa7\xec\x8cB?j~\x11\xc0\x84\xe0\xa5\'=AfDB\xbaL\x02#\xebg\xd0\xb9m\xf7u\x0e\xd3;E\xa1\x0c+\xa7\xdd\xb0iY\x1c\x85\xab\x17\xa6\x0e\x8f\xb5\xedh\xde\xc0|\xed\xd3\xb3\x15\xba\xca\xab\xfc&\xad%&.k[\x00:\xd9\x1c\xe1\x18\xf0\xc6\xae\x8eb+R\xd9\x9c|\xe1He\x81\xc7N\x12"eck\xf7\xd2)\x93\xf0\xfe\x1f2\x18\x9b\x1c\x0fn\xb0d\x9b@\xb0\xc8\xbf\x97$\x93^E\n\xd9\x02\x91\x07\x85\x90Z\xb5Im\x1c\x92t(\xb6i\x0e4\xc5\xf3\xf3\x19r@\x83M\xbaN\xd6\x1d\x01M)\x1a\x9fzbz\x11~\xfb\xcd\xcah:l(\xab\xdd\x8bI\xf0\x99\xea\x1d\xc4\x0e\xfb\xec[\x0eu\xad\xdbM&f\xf7TU\x14Yl\x961,K\x93\xe4\x08\xbd?\xf4\x8c,\x98&\t\xa4\xc6\xae\xdb\xd4\x8c\xf4\xc7\xbbo\x08\r\xb2\x8a5\xdc\x10-\x1b\xa1\x81T\xf6\xe1\xe61C\xbe\xd6]\x82^\x85v\xd1\x882\x06\\+\xdb\x08\xb6T\xb4(T\xdb\xc8\xbb\xf5\xef\xdaI\xfb\xde\xbf\x9b6$@\xe4!\x05\xcd#{\xe6\x80]\xf9K\xb4\xbf\x8djW\xb5{\t\x02\xf9\xe1\x19\x16L\xdc\x8a\xca\'\xaeY[ed\xc2^\x8d_y>\x81\x91\xde\xaa\x92 \x99\x03w\x99?\xb1=\xba\xe4\x0f\xd1\x17\xe1(XA\xf8\xa1\xac\xaebcQ>~\xa9|\xdc\xbe\xc2H\xc6\x96\xde^\x18\xcd\x10Y\xd1~\xc995\xbaq\xdb\x17\x1b\x92\xfd\x82\x85ON\xf8V\xa9\xefY\x07\xd1\xae\xbaO\xf8\x90\td\xd8&\x08\xa3\xc7\x8a\xd6\xcf\x95EwZ\xf0d\xcfL\xf7\xf6\x1291\xff\xfa\x10\xa6\x9e#?\x16\xdb\xb7\xbb\xdf\x1f\xe3\x95\xe7\x18\xc4\x0fM3\xab\xc1\x9d1_"\xab\xc4b@\xf5\xd8\xc8\x02#\xec\xe1\xf2)\x1dhX\x96f\x93\xe5\x19Gt\xb9\x13d\xcd\x7f\xbeL\xb0\x90c\xbe\xa9`\x8dAztT\xa2U\xfb\xd7*\xd2\x99;l?\xec\xc0c\xb0?3\x1a\xe1\xfa\x9c\xc9\x07\x7f!-d\'\xb9\xe8\xd6\xd3\xaaC\n\xf4\xdc!\xe4b\x19\xea\xbd_`\xcd\xed$\x8d\x1f1.\x1bY\xec\xd9\xba\x92\x02\x83R[T\xf7vXm\x1ap6\xa9\xcbN\xc7\xd0\n\x11\xeb?c\x80:\x11\xb64\xc1\x01\x91\xb28\xe8\xc6\xeet\x81Ch`\xb6\xc1\xb2\xdd8\x165\x91Y\x03\xd3\x0fQ#\x0b\x1enG{\x80rj\x846\x0fX\xc4\xa9E\xda:\xd6b\xa6+S6\x81\xc8\x0eQ\x05\xf8(\x1by\x02s\xcas[\xf1\\\xfe\xf0f\xb8\xb9\xab\xd0\x12\xe9\x0eG\x7f\x15\n\x08*^5\x1d\xf6\xeb9\xe82\xe9\xde\xee\xd7\xc3=\xd5r\xed!1\xca\xaa\xec\xd5R\xf6\xbc\x065\x0b\xd0\xd4\xbd\xa5\xd5\x8cHz\xe9\xba\xb8kI#!Qe\xd7\xe8\xc6\xc2\xae\xc6~\x83j\xfa=\x98{1\xfd\xe7\x1ds\xcfJ#VK\xeb\x91M=d)\xb1"\x8b\xb9\xad\x1f\xd86\xe0\x0eu\xfe\xba\xb1V\xf2\xa6\xd2\xba\xd1p\xacm\xf5eXnP\'\xd0\xe0\x85B\x16\x89@G\xec\xdd\'\xce\xd8u\xb3\x00\x97;\xc8\xcfA4\x9b\x8eF\xa6\x92\xaa\x81f$7\x1e\xcc\xb6\x17\xe7\x97\'g~j\xea\xff\x00M\xd6\xf0\x8d)\x12\xda\x03foo\xda\x03bar\xda\x02os\xda\nsubprocess\xda\x03sysr(\x00\x00\x00r)\x00\x00\x00Z\tlibraries\xda\x0ccheck_output\xda\x07environ\xda\x03get\xda\nexecutabler\'\x00\x00\x00Z\x13installed_librariesZ\x07library\xda\ncheck_call\xda\x04exec\xda\x07compiler,\x00\x00\x00r,\x00\x00\x00r,\x00\x00\x00r-\x00\x00\x00\xda\x08<module>\x02\x00\x00\x00s2\x00\x00\x00\x04\x01\x04\x01\x08\x01\x08\x01\x08\x01\x08\x04J\x02\x04\x01F\xff\x04\x01\x0e\xff\x04\x01\x0c\xff\x04\x02\x06\x01\x02\xff\x06\x03\x08\x01\x08\x01\x02\x01\x04\x01H\xff\x08\x02\x06\x01\x08\x02)\x0f\xda\x03foo\xda\x03bar\xda\x03sys\xda\x05bytes\xda\x06decode\xda\x04join\xda\x07version\xda\x05splitZ\x0ePYTHON_VERSION\xda\x05print\xda\x07replace\xda\x04exit\xda\x07marshal\xda\x04exec\xda\x05loads\xa9\x00r)\x00\x00\x00r)\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x12\x00\x00\x00\x04\x01\x04\x01\x08\x01\x08\x03B\x01\x14\x01>\x01\x08\x02\x08\x01)\x0f\xda\x03foo\xda\x03bar\xda\x03sys\xda\x05bytes\xda\x06decode\xda\x04join\xda\x07version\xda\x05splitZ\x0ePYTHON_VERSION\xda\x05print\xda\x07replace\xda\x04exit\xda\x07marshal\xda\x04exec\xda\x05loads\xa9\x00r)\x00\x00\x00r)\x00\x00\x00\xda\x06string\xda\x08<module>\x02\x00\x00\x00s\x12\x00\x00\x00\x04\x01\x04\x01\x08\x01\x08\x03B\x01\x14\x01>\x01\x08\x02\x08\x01'))