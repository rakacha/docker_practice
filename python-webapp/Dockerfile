FROM python
WORKDIR /src
ADD . /src
# Install app dependencies
RUN pip install Flask
CMD ["python", "/src/simpleapp.py", "-p 8000"]