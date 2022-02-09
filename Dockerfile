FROM ubuntu:20.04 
RUN apt-get update && apt-get install -y build-essential \
    autotools-dev \ 
    autoconf \
    automake \
    vim \
    git \
    python3 \
    curl \
    gcc \
    g++ \
    gfortran \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && git clone https://github.com/spack/spack.git \
    && cd spack \
    && git checkout v0.16.3 \
    && . ./share/spack/setup-env.sh \
    && env=nekbone \
    && spack env create ${env}\
    && spack env activate ${env}\
    && spack install nekbone
COPY ./build_example.py /spack
RUN python3 /spack/build_example.py
