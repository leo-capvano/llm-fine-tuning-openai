import time

from svc.training_svc import upload_training_file, create_training_job, training_job_status

BASE_MODEL = "gpt-4o-2024-08-06"


def main():
    print("This is your OpenAI fine-tuning pipeline.")
    training_file_name = input("Choose the training file name. It must be placed into the res/ folder -> ")
    training_file = upload_training_file(training_file_name)
    prompt = input("A new Fine-Tuning job will be created. Do you confirm? [y/N] -> ")
    if prompt.lower() == "y":
        job = create_training_job(training_file.id, BASE_MODEL)
        start_time = time.time()
        while training_job_status(job.id).fine_tuned_model is None:
            time.sleep(5)
            print(
                f"The fine tuning job is in progress, wait until it finishes ... {int(time.time() - start_time)}s elapsed")
        print(f"Fine Tuning completed, your custom model id is: {training_job_status(job.id).fine_tuned_model}")


if __name__ == "__main__":
    main()
