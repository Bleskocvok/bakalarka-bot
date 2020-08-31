
FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y \
    protobuf-compiler \
    cmake \
    clang \
    python3 \
    python3-pip \
    wget \
    npm \
    graphviz

WORKDIR /usr/src/app

COPY . .


# install svgexport
npm install svgexport -g

# install DAGmar
RUN wget "http://www.graphdrawing.org/download/DAGmar.tgz"
RUN tar -xvzf DAGmar.tgz

# bot requirements
RUN pip3 install -r requirements.txt

# compile drag
ENV CC=/usr/bin/clang
ENV CXX=/usr/bin/clang++
WORKDIR drag/bin
RUN cmake ..
RUN make draw # drag bug, cannot compile target 'cycl', only 'draw'
WORKDIR ../../
RUN cp -r drag/bin/ .


CMD ["python3", "result.py"]

