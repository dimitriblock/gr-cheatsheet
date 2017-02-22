from gnuradio import gr, blocks, filter, analog

class my_topblock(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self)
        amp = 1
        taps = filter.firdes.low_pass(1, 1, 0.1, 0.01)
        self.src = analog.noise_source_c(analog.GR_GAUSSIAN, amp)
        self.flt = filter.fir_filter_ccf(1, taps)
        self.snk = blocks.null_sink(gr.sizeof_gr_complex)
        self.connect(self.src, self.flt, self.snk)

if __name__ == "__main__":
    tb = my_topblock()
    tb.start()
    tb.wait()
