import flowd
import sys
# To install flowd, run the following commands:
# sudo apt-get install build-essential python-dev
# wget http://hollywood.colorado.edu/static/dpkg/flowd.0.9.1.dpkg
# dpkg -i flowd.0.9.1.dpkg
# wget http://flowd.googlecode.com/files/flowd-0.9.1.tar.gz
# tar xfvz flowd-0.9.1.tar.gz
# cd flowd-0.9.1
# sudo python setup.py install

log = flowd.FlowLog('/var/log/flowd')
for flow in log:
    print dir(flow)
    print flow.format()
    print flow.dst_port
    print flow.octets
    sys.exit(1)
