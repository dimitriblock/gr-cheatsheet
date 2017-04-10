from gnuradio import analog
from gnuradio import audio
from gnuradio import eng_notation
from gnuradio import gr


class top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self, "Top Block")

        self.samp_rate = samp_rate = 32000

        # Blocks
        self.audio = audio.sink(samp_rate, '', True)
        self.noise = analog.noise_source_f(analog.GR_GAUSSIAN, 0.1, 0)

        # Connections
        self.connect(self.noise, self.audio)

def main(top_block_cls=top_block, options=None):

    tb = top_block_cls()
    tb.start()
    try:
        raw_input('Press Enter to quit: ')
    except EOFError:
        pass
    tb.stop()
    tb.wait()


if __name__ == '__main__':
    main()
