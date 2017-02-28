# Install pybombs via python-pip
sudo pip install PyBOMBS

# Add recipe lists from git repositories
pybombs recipes add gr-recipes git+https://github.com/gnuradio/gr-recipes.git  
pybombs recipes add gr-etcetera git+https://github.com/gnuradio/gr-etcetera.git

# Set installation folder to '~/Desktop/pybombs'
pybombs prefix init ~/Desktop/pybombs -a myprefix

# Enable documentation
pybombs config builddocs=ON

# Run gnuradio installation with verbose output
pybombs -vv install gnuradio

# Outputs list of Gnuradio enabled components
# Check that the following components are enabled:
#
# ######################################################
# # Gnuradio enabled components                         
# ######################################################
#   * python-support
#   * testing-support
#   * volk
#   * doxygen
#   * gnuradio-runtime
#   * gr-ctrlport
#   * * thrift
#   * gr-blocks
#   * gnuradio-companion
#   * gr-fec
#   * gr-fft
#   * gr-filter
#   * gr-analog
#   * gr-digital
#   * gr-audio
#   * * alsa
#   * gr-channels
#   * gr-qtgui
#   * gr-uhd
#   * gr-utils
#   * gr-wavelet
#   * gr-zeromq

# Publish install variables as environment variables
source ~/Desktop/pybombs/setup_env.sh

# Apply also after re-booting
echo 'source ~/Desktop/pybombs/setup_env.sh' >> ~/.profile
echo 'source ~/Desktop/pybombs/setup_env.sh' >> ~/.bashrc

# Run GNU Radio Companion
gnuradio-companion
