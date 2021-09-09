import cv2
import numpy as np

import tensorflow.lite as tflite

# import tflite_runtime.interpreter as tflite

from PIL import Image

CAMERA_WIDTH = 640
CAMERA_HEIGHT = 480


def load_labels(label_path):
    r"""Returns a list of labels"""
    with open(label_path, "r") as f:
        return [line.strip() for line in f.readlines()]


def load_model(model_path):
    r"""Load TFLite model, returns a Interpreter instance."""
    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter


def process_image(interpreter, image, input_index, k=3):
    r"""Process an image, Return top K result in a list of 2-Tuple(confidence_score, _id)"""
    input_data = np.expand_dims(image, axis=0)  # expand to 4-dim

    # Process
    interpreter.set_tensor(input_index, input_data)
    interpreter.invoke()

    # Get outputs
    output_details = interpreter.get_output_details()
    output_data = interpreter.get_tensor(output_details[0]["index"])
    # print(output_data.shape)  # (1, 1001)
    output_data = np.squeeze(output_data)

    # Get top K result
    top_k = output_data.argsort()[-k:][::-1]  # Top_k index
    result = []
    for _id in top_k:
        score = float(output_data[_id] / 255.0)
        result.append((_id, score))

    return result


def display_result(top_result, frame, labels):
    r"""Display top K result in top right corner"""
    font = cv2.FONT_HERSHEY_SIMPLEX
    size = 0.6
    color = (255, 0, 0)  # Blue color
    thickness = 1

    for idx, (_id, score) in enumerate(top_result):
        # print('{} - {:0.4f}'.format(label, score))
        x = 12
        y = 24 * idx + 24
        cv2.putText(
            frame,
            "{} - {:0.4f}".format(labels[_id], score),
            (x, y),
            font,
            size,
            color,
            thickness,
        )

    cv2.imshow("Image Classification", frame)


if __name__ == "__main__":

    model_path = "model/tflite/output/model.tflite"
    label_path = "model/tflite/output/labels.txt"

    cap = cv2.VideoCapture(0)
    cap.set(cv2.CAP_PROP_FRAME_WIDTH, CAMERA_WIDTH)
    cap.set(cv2.CAP_PROP_FRAME_HEIGHT, CAMERA_HEIGHT)
    cap.set(cv2.CAP_PROP_FPS, 15)

    interpreter = load_model(model_path)
    labels = load_labels(label_path)

    input_details = interpreter.get_input_details()

    # Get Width and Height
    input_shape = input_details[0]["shape"]
    height = input_shape[1]
    width = input_shape[2]

    # Get input index
    input_index = input_details[0]["index"]

    # Process Stream
    while True:
        ret, frame = cap.read()

        # image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = image.resize((width, height))

        top_result = process_image(interpreter, image, input_index)
        display_result(top_result, frame, labels)

        key = cv2.waitKey(1)
        if key == 27:  # esc
            break

    cap.release()
    cv2.destroyAllWindows()
