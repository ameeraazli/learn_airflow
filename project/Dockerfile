# FROM apache/airflow:2.7.0
FROM python:3.11

# COPY --chown=airflow:root dags/first_dag.py /opt/airflow/dags
# RUN mkdir airflow
# COPY dags/first_dag.py /opt/airflow/dags/
# COPY dags/ airflow/
COPY pyproject.toml /
COPY poetry.lock /
RUN pip3 install poetry
# RUN poetry add apache-airflow

# RUN poetry to install all dependencies
RUN poetry install

# Expose the required ports (if needed)
# EXPOSE 8080

# # Set the entry point for the container
# CMD ["airflow", "webserver"]

