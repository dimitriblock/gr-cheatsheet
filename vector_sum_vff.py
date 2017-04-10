import numpy
from gnuradio import gr

class vector_sum_vff(gr.sync_block):
    def __init__(self, vlen):
        self.vlen = vlen
        gr.sync_block.__init__(self,
            name="vector_sum_vff",
            # Input signature: Float vector values
            in_sig=[(numpy.float32, vlen)],
            # Output signature: Float value
            out_sig=[(numpy.float32, 1)])

    def work(self,input_items,output_items):
        in0 = input_items[0]
        out = output_items[0]
        out[:] = numpy.sum(in0[0:1], axis=1)
        return 1

