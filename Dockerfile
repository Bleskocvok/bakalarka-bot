
FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y \
    apt-utils \
    protobuf-compiler \
    cmake \
    clang \
    python3 \
    python3-pip \
    wget \
    graphviz \
    imagemagick \
    openjdk-8-jdk


WORKDIR /usr/src/app

COPY . .

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
#RUN make cycl
WORKDIR ../../
RUN cp drag/bin/draw .
#RUN cp drag/bin/cycl .
RUN ls -la
RUN java -version

CMD ["python3", "result.py"]

