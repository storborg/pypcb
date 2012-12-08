from lxml import etree

from .. import model, drawing


def read(fname):
    assert fname.endswith('.lbr')
    f = open(fname, 'r')
    tree = etree.parse(f)
    doc = tree.getroot()
    return parse_library(doc)


def parse_drawing_element(el):
    tag = el.tag
    layer = int(el.attrib['layer'])
    if tag == 'wire':
        return drawing.Line(start=(float(el.attrib['x1']),
                                   float(el.attrib['y1'])),
                            end=(float(el.attrib['x2']),
                                 float(el.attrib['y2'])),
                            width=float(el.attrib['width']),
                            layer=layer)

    elif tag == 'text':
        if 'ratio' in el.attrib:
            ratio = int(el.attrib['ratio'])
        else:
            ratio = '?'
        return drawing.Text(position=(float(el.attrib['x']),
                                      float(el.attrib['y'])),
                            size=float(el.attrib['size']),
                            ratio=ratio,
                            s=el.text,
                            layer=layer)
    elif tag == 'rectangle':
        return drawing.Rectangle(topleft=(float(el.attrib['x1']),
                                          float(el.attrib['y1'])),
                                 bottomright=(float(el.attrib['x2']),
                                              float(el.attrib['y2'])),
                                 layer=layer)
    elif tag == 'circle':
        return drawing.Circle(position=(float(el.attrib['x']),
                                        float(el.attrib['y'])),
                              radius=float(el.attrib['radius']),
                              width=float(el.attrib['width']),
                              layer=layer)


def parse_package(doc):
    package = model.Package(name=doc.attrib['name'])

    for el in doc.getchildren():
        tag = el.tag
        if tag == 'description':
            package.description = el.text
        elif tag == 'smd':
            package.pads.append(model.SMDPad(
                name=el.attrib['name'],
                position=(float(el.attrib['x']),
                          float(el.attrib['y'])),
                dimensions=(float(el.attrib['dx']),
                            float(el.attrib['dy'])),
                layer=int(el.attrib['layer']),
            ))
        elif tag == 'pad':
            if 'shape' in el.attrib:
                shape = el.attrib['shape']
            else:
                shape = '?'
            if 'rot' in el.attrib:
                rotation = int(el.attrib['rot'][1:])
            else:
                rotation = '?'
            package.pads.append(model.ThroughHolePad(
                name=el.attrib['name'],
                position=(float(el.attrib['x']),
                          float(el.attrib['y'])),
                diameter=float(el.attrib['drill']),
                shape=shape,
                rotation=rotation,
            ))
        else:
            package.drawing.append(parse_drawing_element(el))

    return package



def parse_library(doc):
    library_doc = doc.xpath('.//library')[0]
    description = library_doc.xpath('.//description')[0].text
    library = model.Library(description=description)
    packages_doc = library_doc.xpath('.//packages')[0]

    for package_doc in packages_doc.xpath('.//package'):
        library.packages.append(parse_package(package_doc))

    return library
