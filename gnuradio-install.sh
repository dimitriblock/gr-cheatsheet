# Install pybombs via python-pip
sudo pip install PyBOMBS

# Apply automatic configuration
pybombs auto-config

# Enable documentation
pybombs config builddocs=ON

# Add default recipe lists
pybombs recipes add-defaults

# Installation on Desktop folder
pybombs prefix init ~/Desktop/pybombs

# Run gnuradio installation
pybombs install gnuradio

# Publish install variables as environment variables
source ~/Desktop/pybombs/setup_env.sh

# Apply also after re-booting
echo 'source ~/Desktop/pybombs/setup_env.sh' >> ~/.profile
echo 'source ~/Desktop/pybombs/setup_env.sh' >> ~/.bashrc

# Run GNU Radio Companion
gnuradio-companion
