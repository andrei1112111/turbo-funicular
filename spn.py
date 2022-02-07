def spn(toponym):
    a, b = [float(i) for i in toponym['boundedBy']['Envelope']['lowerCorner'].split()]
    a1, b1 = [float(i) for i in toponym['boundedBy']['Envelope']['upperCorner'].split()]
    return ",".join([str(a1 - a), str(b1 - b)])
