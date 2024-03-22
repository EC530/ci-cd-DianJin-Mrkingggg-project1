## Project 1 components:

1. Add matrice multiplication function and in proj1.py
   
2. Add unit tests for matrice multiplication in test_proj1.py

3. Add memory usage test using tracemalloc for all tests.
   
4. Add logging in each function with start level: INFO. Logging could report normal information and exception occurance using different logging level:
   info and exception( error )

5. Add CPU time test in conftest.py so that cpu run time: ncalls  tottime  percall  cumtime  percall could be observed.

6. Include coverage and flake configurations in py-ci.yml of .github/workflow and pass the Github Actions' build.

### Using pytest -s test_proj1.py to show complete information.


### Add Dockerfile for Container. To start the container, use 1. docker build -t project1:latest .  2. docker run -d --name cProj1 -p 8080:8080 project1:latest in terminal and then start the docker.

## Documentation for Dockerfile:

#### Base Image

The Dockerfile is based on the `python:3.9` image. This is an official Python Docker image that comes pre-installed with Python version 3.9. It's suitable for running applications developed with Python 3.9.

#### Working Directory:
The Dockerfile sets the working directory inside the container to `/app`. This means that all commands will be run in this directory, and it's where your application files will reside.

#### Python Dependencies：
To manage Python dependencies, the Dockerfile first copies a `requirements.txt` file into the `/app` directory of the container. Then, it installs these dependencies using `pip install`. This ensures that all the necessary Python libraries for your application are installed within the container.

#### Project Files：
The Dockerfile copies the contents of your project's current directory into the container's `/app` directory. This action includes your application code, resources, and any other files needed to run your application, except those specified in `.dockerignore`. It's important to maintain a properly configured `.dockerignore` file to prevent copying unnecessary or sensitive information into the container.

#### Exposing Ports：
The Dockerfile includes the `EXPOSE 8080` instruction, which tells Docker to expose port 8080 inside the container. This is crucial for allowing your application to communicate with the outside world.

### Startup Command
When the container starts, it executes the command `CMD ["python", "proj1.py"]`. This command tells Docker to run the application using the Python interpreter, with `proj1.py` being the entry point of your application.

### Building the Docker Image
To build the Docker image from this Dockerfile, run the following command in your terminal:

```bash
docker build -t my-python-app .
```

### Running the Container
```bash
docker run -d -p 8080:8080 my-python-app
```
requirements.txt includes all the necessary libraries


