# Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
# Copyright (c) 2011, 2012 Open Networking Foundation
# Copyright (c) 2012, 2013 Big Switch Networks, Inc.
# See the file LICENSE.pyloxi which should have been included in the source distribution

# Automatically generated by LOXI from template module.py
# Do not modify

import struct
import loxi
import util
import loxi.generic_util

import sys
ofp = sys.modules['loxi.of14']

class port_desc_prop(loxi.OFObject):
    subtypes = {}


    def __init__(self, type=None):
        if type != None:
            self.type = type
        else:
            self.type = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!H', 0)
        subclass = port_desc_prop.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = port_desc_prop()
        obj.type = reader.read("!H")[0]
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.type != other.type: return False
        return True

    def pretty_print(self, q):
        q.text("port_desc_prop {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')


class experimenter(port_desc_prop):
    subtypes = {}

    type = 65535

    def __init__(self, experimenter=None):
        if experimenter != None:
            self.experimenter = experimenter
        else:
            self.experimenter = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.experimenter))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!L', 4)
        subclass = experimenter.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = experimenter()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        obj.experimenter = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.experimenter != other.experimenter: return False
        return True

    def pretty_print(self, q):
        q.text("experimenter {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

port_desc_prop.subtypes[65535] = experimenter

class bsn(experimenter):
    subtypes = {}

    type = 65535
    experimenter = 6035143

    def __init__(self, exp_type=None):
        if exp_type != None:
            self.exp_type = exp_type
        else:
            self.exp_type = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.exp_type))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        subtype, = reader.peek('!L', 8)
        subclass = bsn.subtypes.get(subtype)
        if subclass:
            return subclass.unpack(reader)

        obj = bsn()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        obj.exp_type = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.exp_type != other.exp_type: return False
        return True

    def pretty_print(self, q):
        q.text("bsn {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

experimenter.subtypes[6035143] = bsn

class bsn_breakout(bsn):
    type = 65535
    experimenter = 6035143
    exp_type = 3

    def __init__(self, sub_interface_count=None, sub_interface_speed_gbps=None):
        if sub_interface_count != None:
            self.sub_interface_count = sub_interface_count
        else:
            self.sub_interface_count = 0
        if sub_interface_speed_gbps != None:
            self.sub_interface_speed_gbps = sub_interface_speed_gbps
        else:
            self.sub_interface_speed_gbps = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.exp_type))
        packed.append(struct.pack("!H", self.sub_interface_count))
        packed.append(struct.pack("!H", self.sub_interface_speed_gbps))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_breakout()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _exp_type = reader.read("!L")[0]
        assert(_exp_type == 3)
        obj.sub_interface_count = reader.read("!H")[0]
        obj.sub_interface_speed_gbps = reader.read("!H")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.sub_interface_count != other.sub_interface_count: return False
        if self.sub_interface_speed_gbps != other.sub_interface_speed_gbps: return False
        return True

    def pretty_print(self, q):
        q.text("bsn_breakout {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("sub_interface_count = ");
                q.text("%#x" % self.sub_interface_count)
                q.text(","); q.breakable()
                q.text("sub_interface_speed_gbps = ");
                q.text("%#x" % self.sub_interface_speed_gbps)
            q.breakable()
        q.text('}')

bsn.subtypes[3] = bsn_breakout

class bsn_driver_info_json(bsn):
    type = 65535
    experimenter = 6035143
    exp_type = 7

    def __init__(self, driver_info_json=None):
        if driver_info_json != None:
            self.driver_info_json = driver_info_json
        else:
            self.driver_info_json = ''
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.exp_type))
        packed.append(self.driver_info_json)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_driver_info_json()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _exp_type = reader.read("!L")[0]
        assert(_exp_type == 7)
        obj.driver_info_json = str(reader.read_all())
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.driver_info_json != other.driver_info_json: return False
        return True

    def pretty_print(self, q):
        q.text("bsn_driver_info_json {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("driver_info_json = ");
                q.pp(self.driver_info_json)
            q.breakable()
        q.text('}')

bsn.subtypes[7] = bsn_driver_info_json

class bsn_forward_error_correction(bsn):
    type = 65535
    experimenter = 6035143
    exp_type = 2

    def __init__(self, configured=None, enabled=None):
        if configured != None:
            self.configured = configured
        else:
            self.configured = 0
        if enabled != None:
            self.enabled = enabled
        else:
            self.enabled = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.exp_type))
        packed.append(struct.pack("!L", self.configured))
        packed.append(struct.pack("!L", self.enabled))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_forward_error_correction()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _exp_type = reader.read("!L")[0]
        assert(_exp_type == 2)
        obj.configured = reader.read("!L")[0]
        obj.enabled = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.configured != other.configured: return False
        if self.enabled != other.enabled: return False
        return True

    def pretty_print(self, q):
        q.text("bsn_forward_error_correction {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("configured = ");
                q.text("%#x" % self.configured)
                q.text(","); q.breakable()
                q.text("enabled = ");
                q.text("%#x" % self.enabled)
            q.breakable()
        q.text('}')

bsn.subtypes[2] = bsn_forward_error_correction

class bsn_generation_id(bsn):
    type = 65535
    experimenter = 6035143
    exp_type = 1

    def __init__(self, generation_id=None):
        if generation_id != None:
            self.generation_id = generation_id
        else:
            self.generation_id = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.exp_type))
        packed.append(struct.pack("!Q", self.generation_id))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_generation_id()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _exp_type = reader.read("!L")[0]
        assert(_exp_type == 1)
        obj.generation_id = reader.read("!Q")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.generation_id != other.generation_id: return False
        return True

    def pretty_print(self, q):
        q.text("bsn_generation_id {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("generation_id = ");
                q.text("%#x" % self.generation_id)
            q.breakable()
        q.text('}')

bsn.subtypes[1] = bsn_generation_id

class bsn_misc_capabilities(bsn):
    type = 65535
    experimenter = 6035143
    exp_type = 5

    def __init__(self, current=None, available=None, supported=None):
        if current != None:
            self.current = current
        else:
            self.current = 0
        if available != None:
            self.available = available
        else:
            self.available = 0
        if supported != None:
            self.supported = supported
        else:
            self.supported = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.exp_type))
        packed.append(struct.pack("!Q", self.current))
        packed.append(struct.pack("!Q", self.available))
        packed.append(struct.pack("!Q", self.supported))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_misc_capabilities()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _exp_type = reader.read("!L")[0]
        assert(_exp_type == 5)
        obj.current = reader.read("!Q")[0]
        obj.available = reader.read("!Q")[0]
        obj.supported = reader.read("!Q")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.current != other.current: return False
        if self.available != other.available: return False
        if self.supported != other.supported: return False
        return True

    def pretty_print(self, q):
        q.text("bsn_misc_capabilities {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("current = ");
                q.text("%#x" % self.current)
                q.text(","); q.breakable()
                q.text("available = ");
                q.text("%#x" % self.available)
                q.text(","); q.breakable()
                q.text("supported = ");
                q.text("%#x" % self.supported)
            q.breakable()
        q.text('}')

bsn.subtypes[5] = bsn_misc_capabilities

class bsn_sff_json(bsn):
    type = 65535
    experimenter = 6035143
    exp_type = 6

    def __init__(self, data_json=None):
        if data_json != None:
            self.data_json = data_json
        else:
            self.data_json = ''
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.exp_type))
        packed.append(self.data_json)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_sff_json()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _exp_type = reader.read("!L")[0]
        assert(_exp_type == 6)
        obj.data_json = str(reader.read_all())
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.data_json != other.data_json: return False
        return True

    def pretty_print(self, q):
        q.text("bsn_sff_json {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("data_json = ");
                q.pp(self.data_json)
            q.breakable()
        q.text('}')

bsn.subtypes[6] = bsn_sff_json

class bsn_speed_capabilities(bsn):
    type = 65535
    experimenter = 6035143
    exp_type = 4

    def __init__(self, current=None, available=None, supported=None):
        if current != None:
            self.current = current
        else:
            self.current = 0
        if available != None:
            self.available = available
        else:
            self.available = 0
        if supported != None:
            self.supported = supported
        else:
            self.supported = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.exp_type))
        packed.append(struct.pack("!Q", self.current))
        packed.append(struct.pack("!Q", self.available))
        packed.append(struct.pack("!Q", self.supported))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_speed_capabilities()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _exp_type = reader.read("!L")[0]
        assert(_exp_type == 4)
        obj.current = reader.read("!Q")[0]
        obj.available = reader.read("!Q")[0]
        obj.supported = reader.read("!Q")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.current != other.current: return False
        if self.available != other.available: return False
        if self.supported != other.supported: return False
        return True

    def pretty_print(self, q):
        q.text("bsn_speed_capabilities {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("current = ");
                q.text("%#x" % self.current)
                q.text(","); q.breakable()
                q.text("available = ");
                q.text("%#x" % self.available)
                q.text(","); q.breakable()
                q.text("supported = ");
                q.text("%#x" % self.supported)
            q.breakable()
        q.text('}')

bsn.subtypes[4] = bsn_speed_capabilities

class bsn_uplink(bsn):
    type = 65535
    experimenter = 6035143
    exp_type = 0

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(struct.pack("!L", self.exp_type))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = bsn_uplink()
        _type = reader.read("!H")[0]
        assert(_type == 65535)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        _experimenter = reader.read("!L")[0]
        assert(_experimenter == 6035143)
        _exp_type = reader.read("!L")[0]
        assert(_exp_type == 0)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def pretty_print(self, q):
        q.text("bsn_uplink {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

bsn.subtypes[0] = bsn_uplink

class ethernet(port_desc_prop):
    type = 0

    def __init__(self, curr=None, advertised=None, supported=None, peer=None, curr_speed=None, max_speed=None):
        if curr != None:
            self.curr = curr
        else:
            self.curr = 0
        if advertised != None:
            self.advertised = advertised
        else:
            self.advertised = 0
        if supported != None:
            self.supported = supported
        else:
            self.supported = 0
        if peer != None:
            self.peer = peer
        else:
            self.peer = 0
        if curr_speed != None:
            self.curr_speed = curr_speed
        else:
            self.curr_speed = 0
        if max_speed != None:
            self.max_speed = max_speed
        else:
            self.max_speed = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append('\x00' * 4)
        packed.append(struct.pack("!L", self.curr))
        packed.append(struct.pack("!L", self.advertised))
        packed.append(struct.pack("!L", self.supported))
        packed.append(struct.pack("!L", self.peer))
        packed.append(struct.pack("!L", self.curr_speed))
        packed.append(struct.pack("!L", self.max_speed))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = ethernet()
        _type = reader.read("!H")[0]
        assert(_type == 0)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        reader.skip(4)
        obj.curr = reader.read("!L")[0]
        obj.advertised = reader.read("!L")[0]
        obj.supported = reader.read("!L")[0]
        obj.peer = reader.read("!L")[0]
        obj.curr_speed = reader.read("!L")[0]
        obj.max_speed = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.curr != other.curr: return False
        if self.advertised != other.advertised: return False
        if self.supported != other.supported: return False
        if self.peer != other.peer: return False
        if self.curr_speed != other.curr_speed: return False
        if self.max_speed != other.max_speed: return False
        return True

    def pretty_print(self, q):
        q.text("ethernet {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("curr = ");
                q.text("%#x" % self.curr)
                q.text(","); q.breakable()
                q.text("advertised = ");
                q.text("%#x" % self.advertised)
                q.text(","); q.breakable()
                q.text("supported = ");
                q.text("%#x" % self.supported)
                q.text(","); q.breakable()
                q.text("peer = ");
                q.text("%#x" % self.peer)
                q.text(","); q.breakable()
                q.text("curr_speed = ");
                q.text("%#x" % self.curr_speed)
                q.text(","); q.breakable()
                q.text("max_speed = ");
                q.text("%#x" % self.max_speed)
            q.breakable()
        q.text('}')

port_desc_prop.subtypes[0] = ethernet

class optical(port_desc_prop):
    type = 1

    def __init__(self, supported=None, tx_min_freq_lmda=None, tx_max_freq_lmda=None, tx_grid_freq_lmda=None, rx_min_freq_lmda=None, rx_max_freq_lmda=None, rx_grid_freq_lmda=None, tx_pwr_min=None, tx_pwr_max=None):
        if supported != None:
            self.supported = supported
        else:
            self.supported = 0
        if tx_min_freq_lmda != None:
            self.tx_min_freq_lmda = tx_min_freq_lmda
        else:
            self.tx_min_freq_lmda = 0
        if tx_max_freq_lmda != None:
            self.tx_max_freq_lmda = tx_max_freq_lmda
        else:
            self.tx_max_freq_lmda = 0
        if tx_grid_freq_lmda != None:
            self.tx_grid_freq_lmda = tx_grid_freq_lmda
        else:
            self.tx_grid_freq_lmda = 0
        if rx_min_freq_lmda != None:
            self.rx_min_freq_lmda = rx_min_freq_lmda
        else:
            self.rx_min_freq_lmda = 0
        if rx_max_freq_lmda != None:
            self.rx_max_freq_lmda = rx_max_freq_lmda
        else:
            self.rx_max_freq_lmda = 0
        if rx_grid_freq_lmda != None:
            self.rx_grid_freq_lmda = rx_grid_freq_lmda
        else:
            self.rx_grid_freq_lmda = 0
        if tx_pwr_min != None:
            self.tx_pwr_min = tx_pwr_min
        else:
            self.tx_pwr_min = 0
        if tx_pwr_max != None:
            self.tx_pwr_max = tx_pwr_max
        else:
            self.tx_pwr_max = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for length at index 1
        packed.append('\x00' * 4)
        packed.append(struct.pack("!L", self.supported))
        packed.append(struct.pack("!L", self.tx_min_freq_lmda))
        packed.append(struct.pack("!L", self.tx_max_freq_lmda))
        packed.append(struct.pack("!L", self.tx_grid_freq_lmda))
        packed.append(struct.pack("!L", self.rx_min_freq_lmda))
        packed.append(struct.pack("!L", self.rx_max_freq_lmda))
        packed.append(struct.pack("!L", self.rx_grid_freq_lmda))
        packed.append(struct.pack("!L", self.tx_pwr_min))
        packed.append(struct.pack("!L", self.tx_pwr_max))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(reader):
        obj = optical()
        _type = reader.read("!H")[0]
        assert(_type == 1)
        _length = reader.read("!H")[0]
        orig_reader = reader
        reader = orig_reader.slice(_length, 4)
        reader.skip(4)
        obj.supported = reader.read("!L")[0]
        obj.tx_min_freq_lmda = reader.read("!L")[0]
        obj.tx_max_freq_lmda = reader.read("!L")[0]
        obj.tx_grid_freq_lmda = reader.read("!L")[0]
        obj.rx_min_freq_lmda = reader.read("!L")[0]
        obj.rx_max_freq_lmda = reader.read("!L")[0]
        obj.rx_grid_freq_lmda = reader.read("!L")[0]
        obj.tx_pwr_min = reader.read("!L")[0]
        obj.tx_pwr_max = reader.read("!L")[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.supported != other.supported: return False
        if self.tx_min_freq_lmda != other.tx_min_freq_lmda: return False
        if self.tx_max_freq_lmda != other.tx_max_freq_lmda: return False
        if self.tx_grid_freq_lmda != other.tx_grid_freq_lmda: return False
        if self.rx_min_freq_lmda != other.rx_min_freq_lmda: return False
        if self.rx_max_freq_lmda != other.rx_max_freq_lmda: return False
        if self.rx_grid_freq_lmda != other.rx_grid_freq_lmda: return False
        if self.tx_pwr_min != other.tx_pwr_min: return False
        if self.tx_pwr_max != other.tx_pwr_max: return False
        return True

    def pretty_print(self, q):
        q.text("optical {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("supported = ");
                q.text("%#x" % self.supported)
                q.text(","); q.breakable()
                q.text("tx_min_freq_lmda = ");
                q.text("%#x" % self.tx_min_freq_lmda)
                q.text(","); q.breakable()
                q.text("tx_max_freq_lmda = ");
                q.text("%#x" % self.tx_max_freq_lmda)
                q.text(","); q.breakable()
                q.text("tx_grid_freq_lmda = ");
                q.text("%#x" % self.tx_grid_freq_lmda)
                q.text(","); q.breakable()
                q.text("rx_min_freq_lmda = ");
                q.text("%#x" % self.rx_min_freq_lmda)
                q.text(","); q.breakable()
                q.text("rx_max_freq_lmda = ");
                q.text("%#x" % self.rx_max_freq_lmda)
                q.text(","); q.breakable()
                q.text("rx_grid_freq_lmda = ");
                q.text("%#x" % self.rx_grid_freq_lmda)
                q.text(","); q.breakable()
                q.text("tx_pwr_min = ");
                q.text("%#x" % self.tx_pwr_min)
                q.text(","); q.breakable()
                q.text("tx_pwr_max = ");
                q.text("%#x" % self.tx_pwr_max)
            q.breakable()
        q.text('}')

port_desc_prop.subtypes[1] = optical


