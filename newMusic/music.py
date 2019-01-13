import datetime, math
EPOCH = datetime.datetime(1970,1,1)

def remove_whitespace(node):
    to_kill = []
    # build list of nodes to remove WS from
    for child in node.childNodes:
        if child.nodeType == node.TEXT_NODE and not child.data.strip():
            to_kill.append(child)
        elif child.hasChildNodes():
            remove_whitespace(child)
    # Remove the items and unlink to save memory
    for node in to_kill:
        node.parentNode.removeChild(node)
        node.unlink()
		
def _isType(node, name):
    return node.hasChildNodes() and node.childNodes[0].nodeValue == name
	
def getItems(node, name):
    ch = node.childNodes
    items = [ ch[i] for i in xrange(1,len(ch)) if _isType(ch[i-1], name) ]
    return items[0].getElementsByTagName('dict')
	
def get_item(node, target):
    c = node.childNodes
    item = [ c[i+1] for i in xrange(0,len(c)-1) if _isType(c[i], target) ]
    if len(item) == 0:
        if target == 'Play Count':
            return 0
        return None
    result = _get_item_value(item[0])
    if target == 'Total Time':
        return math.floor(result / 1000)
    if result == None:
        print "No children for", target, " ... ", item[0]
    return result
	
def _get_item_value(item):
    ''' Convert the DOM item to a native type '''
    if not item.hasChildNodes():
        return None
    data = item.childNodes[0].nodeValue
    if item.nodeName == 'string':
		return data.replace('"', "'")
    if item.nodeName == 'integer':
        return int(data)
    # it's a date
    d = datetime.datetime.strptime(data, '%Y-%m-%dT%H:%M:%SZ')
    delta = d - EPOCH
	return delta.days
