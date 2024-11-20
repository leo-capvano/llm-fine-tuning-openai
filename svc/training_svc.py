import os

from openai import OpenAI

client = OpenAI()


def training_job_status(job_id: str):
    return client.fine_tuning.jobs.retrieve(job_id)


def create_training_job(training_file: str, model: str):
    return client.fine_tuning.jobs.create(
        training_file=training_file,
        model=model
    )


def upload_training_file(training_file_name: str):
    with open(os.path.join("res", training_file_name), "rb") as training_data_file:
        return client.files.create(file=training_data_file, purpose="fine-tune")


if __name__ == '__main__':
    print(upload_training_file("training_data.jsonl"))
    job = create_training_job("file-gPWPxqdurKGfndZoJNSo2BpC", "gpt-4o-2024-08-06")
    print(job)
