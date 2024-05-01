# Captcha OCR Deployment
This repository focuses on deploying Machine Learning models, specifically the model I've built to crack those pesky Captcha images (Captcha Optical Character Recognition). You know the ones—those squiggly letters and distorted numbers that pop up when you're trying to log in somewhere. They're like the vigilant bouncers at the internet club, ensuring that sneaky bots don't crash the party.

![Untitled](https://github.com/ndy-s/captcha-ocr-deploy/assets/94002483/e9ca4056-ad72-47b5-aefb-03785ab85265)

The dataset I used is sourced from Kaggle, specifically the [Captcha Version 2 Images](https://www.kaggle.com/datasets/fournierp/captcha-version-2-images). However, here’s the catch: it’s a toy dataset. While it’s perfect for tinkering and learning, don’t expect it to handle real-world Captchas like a superhero.

Regarding the architecture, I've drawn inspiration from various sources. However, it seems there are some overfitting issues. Fear not—I might improve the model's performance in the future (hopefully...).

Okay, enough with the brief introduction. The deployment is divided into several parts. For now, I'm using tf-serving and flask deployment using the free deployment service [Railway](https://railway.app/). You'll get a free trial if you're new to Railway, so it's good for experimenting with deployment without worrying about costs. I might add some other deployment techniques and services like GCP or AWS in the future.
