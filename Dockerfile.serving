# Use the official TensorFlow Serving image as the base image
FROM tensorflow/serving:latest

# Copy the TensorFlow SavedModel into the container
COPY ./models /models

# Set environment variables
ENV MODEL_NAME=captcha-ocr-model
ENV PORT=8501

# Create a custom entrypoint script for TensorFlow Serving
RUN echo '#!/bin/bash \n\n\
env \n\
tensorflow_model_server --port=8500 --rest_api_port=${PORT} \
--model_name=${MODEL_NAME} --model_base_path=${MODEL_BASE_PATH}/${MODEL_NAME} \
"$@"' > /usr/bin/tf_serving_entrypoint.sh \
&& chmod +x /usr/bin/tf_serving_entrypoint.sh