# CodeQL Analysis Using Docker

This guide outlines the steps to set up and run CodeQL analysis using Docker.

## 1) Install Docker

Install Docker using the snap command:

`sudo snap install docker`


## 2) Set Up Directory for Running Experiments

Create a directory for running the experiments. For example, `aise_codeql`:

`mkdir aise_codeql`

`cd aise_codeql`


## 3) Copy Files into the Directory

Copy the `run.sh` script and the `Dockerfile` into the `aise_codeql` directory:

``` cp /path/to/run.sh /path/to/Dockerfile . ```


## 4) Prepare Source Code

Create a directory called `src` inside `aise_codeql`. This directory should contain the scripts that need to be analyzed.


## 5) Build Docker Image

Build the Docker image using the following command:

```sudo docker build -t analysis_container . ```


## 6) Run Docker Container

Run the Docker container interactively:

``` sudo docker run -it analysis_container ```


This command will start the Docker container and provide an interactive shell where you can perform CodeQL analysis.





