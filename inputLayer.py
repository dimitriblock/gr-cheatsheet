from gnuradio import blocks
from gnuradio import fft
from gnuradio import gr
from gnuradio.fft import window

class inputLayer(gr.hier_block2):
    def __init__(self, vlen=64):
        gr.hier_block2.__init__(
            self, "Input Layer",
            gr.io_signature(
                1, 1, 
                gr.sizeof_gr_complex*vlen
            ),
            gr.io_signature(
                1, 1, 
                gr.sizeof_float*vlen
            ),
        )

        # Blocks
        fft = fft.fft_vcc(
            vlen, True, 
            (window.rectangular(vlen)), 
            True, 8
        )
        log = blocks.nlog10_ff(20, vlen, 0)
        mag = blocks.complex_to_mag(vlen)
        mult = blocks.multiply_const_vcc(
            ([1./float(vlen), ]*vlen)
        )

        # Connections
        self.connect(self, mult)              
        self.connect(mult, fft)
        self.connect(fft, mag) 
        self.connect(mag, log) 
        self.connect(log, self)
