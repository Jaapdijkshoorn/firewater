#
#   firewater/service.py    WJ111
#
#   firewater by Walter de Jong <walter@heiho.net> (c) 2012
#
#   firewater COMES WITH NO WARRANTY. firewater IS FREE SOFTWARE.
#   firewater is distributed under terms described in the GNU General Public
#   License.
#

'''implements firewater service'''

import socket

class ServiceObject(object):
    '''object respresenting a service'''

    def __init__(self, name=None, port=0, endport=0, proto=None, iface=None):
        self.name = name
        self.proto = proto          # forced protocol
        self.port = port
        self.endport = endport      # it can be a port range
        self.iface = iface          # forced onto an interface

    def __repr__(self):
        return '<ServiceObject: %s,%s,%d,%d,%s>' % (self.name, self.proto,
                                                    self.port, self.endport,
                                                    self.iface)


def servbyname(name):
    '''Return service port number
    or None on error
    '''

    try:
        port = socket.getservbyname(name)
    except socket.error:
        return None

    return port


# EOB
