FROM python:2.7
ADD sum_nums.py /
RUN pip install Flask 
CMD ["python", "sum_nums.py"]
